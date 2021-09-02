from SparkSQL.SparkSQLVisitor import SparkSQLVisitor
from graphviz import Digraph


def flatten(S):
    """
        Util function that flatten multiple-level array.
    """
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


class Node:
    def __init__(self, id, text):
        self._id = id
        self._text = text
        self._children = []

    def add_child(self, child_id, child_label):
        child = {"id": child_id, "label": child_label}
        if child not in self._children:
            self._children.append(child)

    def remove_child(self, child_label):
        self._children = [
            child for child in self._children if child["label"] != child_label]

    def get_child_id(self, child_label):
        child_ids = [child["id"]
                     for child in self._children if child["label"] == child_label]
        if len(child_ids) > 0:
            return child_ids

    def is_all_children(self, child_label):
        has_label = self.get_child_id(child_label)
        return has_label and len(has_label) == len(self.children)

    def get_first_child_id(self):
        if len(self._children) > 0:
            return self._children[0]["id"]

    def has_child_label(self, child_label):
        has_label = self.get_child_id(child_label)
        return has_label and len(has_label) > 0

    def get_children(self, solid_only=True):
        if not solid_only:
            return self._children
        else:
            return [child for child in self.children
                    if child["label"] is None
                    or (child["label"] is not None and not child["label"].startswith("_"))]

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    @property
    def children(self):
        return self._children


class SparkSQLVisitor(SparkSQLVisitor):

    def __init__(self, rule_names):
        super().__init__()
        self._rule_names = rule_names
        self._nodes = {}  # {id: Node object,...}
        self._root_id = None
        self._syntax_graph = Digraph(format="png")
        self._lineage_nodes = None
        self._lineage_graph = Digraph(format="png")
        self._dependency = {}  # {"db.table": {db,table},{table}...}
        self._alias = {}  # {alias_identifier: refered node key,...}
        self._lateral_view_alias = {}
        self._field = []
        self._has_pivot_clause = False
        self._syntax_node_text = ["QUERY", "CTES", "REGULAR_QUERY_SPECIFICATION",
                                  "FROM_CLAUSE", "RELATION", "LATERAL_VIEW", "INLINE_TABLE",
                                  "FUNCTION_TABLE", "FUNCTION_CALL", "DEREFERENCE",
                                  "CURRENT_DATETIME", "CONSTANT_DEFAULT", "GENERATOR_FUNCTION"]
        self._alias_node_text = ["TABLE_NAME_ALIAS", "INLINE_TABLE_ALIAS", "ALIAS_QUERY_ALIAS", "LATERAL_VIEW_ALIAS",
                                 "ALIAS_RELATION_ALIAS", "FUNCTION_TABLE_ALIAS", "NAMED_QUERY_ALIAS"]

    @property
    def nodes(self):
        return self._nodes

    @property
    def syntax_graph(self):
        return self._syntax_graph

    @property
    def lineage_nodes(self):
        return self._lineage_nodes

    @property
    def lineage_graph(self):
        return self._lineage_graph

    @property
    def dependency(self):
        return list(self._dependency.values())

    @property
    def alias(self):
        return self._alias

    @property
    def field(self):
        return self._field

    def node_id(self, ctx):
        id = hex(hash(ctx))
        rule_name = self._rule_names[ctx.getRuleIndex()]
        return "{1}@{0}".format(id, rule_name)

    def add_node(self, ctx, text=""):
        """
            add node to _nodes and _syntac_graph simultaneously
        """
        id = self.node_id(ctx)
        rule_name = self._rule_names[ctx.getRuleIndex()]

        if id not in self._nodes:
            self._syntax_graph.node(id, text)
            self._nodes[id] = Node(id, text)
        return id

    def add_edge(self, parent_id, children_id, label=None):
        """
            add parent-children edge to _syntax_graph
            add children_id to parent node's children
        """

        def add(pid, cid, l):
            self._syntax_graph.edge(pid, cid, l)
            self._nodes[pid].add_child(cid, l)

        if isinstance(children_id, list):
            if len(children_id) == 0:
                return
            children_id = flatten(children_id)
            for child_id in children_id:
                if child_id is not None:
                    add(parent_id, child_id, label)
        else:
            if not children_id:
                return
            child_id = children_id
            add(parent_id, child_id, label)

    def add_dependency(self, database, table):
        dt = database + "." + table
        self._dependency[dt] = {
             "Database": database,
             "Table": table
        }

    def add_alias(self, alias_identifier, node_id):
        """
            A dict to store alias relationship.
            Call when visit tree edges of _alias_node_text except LATERAL_VIEW_ALIAS

            Note: Alias_identifier nodes are kept in syntax_graph for completeness.
            But to avoid infinite recursion, they are removed in lineage_graph
            before doing any recursion and relinking nodes
        """
        if alias_identifier not in self._alias:
            self._alias[alias_identifier] = {
                "node": node_id,
                "text": self._nodes[node_id].text
            }

    def add_lateral_view_alias(self, alias, node_id):
        """
            similar to add_alias
            Call only when visit lateral view clause
        """
        if alias not in self._lateral_view_alias:
            self._lateral_view_alias[alias] = {
                "node": node_id,
                "text": self._nodes[node_id].text
            }

    def add_field(self, field):
        f = {"Name": field}
        if f not in self._field:
            self._field.append(f)

    def build_lineage_graph(self):
        """
            traverse _lineage_nodes from root_id
            add node and edges with style to _lineage_graph Digraph
            render both solid and dashed edges
        """
        g = self._lineage_graph

        g.clear()

        # use a map to store visited node_id, avoid error caused by
        # potential loop in nodes
        visited = {}

        def traverse(node):
            nonlocal visited
            if node.id in visited:
                return

            # set node style
            if node.text in self._syntax_node_text:
                g.attr("node", shape="plaintext")
            elif node.text in self._dependency:
                g.attr("node", shape="ellipse")
            else:
                g.attr("node", shape="box")
            # add node
            g.node(node.id, node.text)

            # visit child
            if len(node.children) > 0:
                for child in node.children:
                    traverse(self._lineage_nodes[child['id']])

                    # add edge to child
                    if child["label"] and child["label"].startswith("_"):
                        g.attr("edge", style="dashed")
                        g.edge(node.id, child["id"])
                    else:
                        g.attr("edge", style="solid")
                        g.edge(node.id, child["id"], child["label"])
            visited[node.id] = 1

        traverse(self._lineage_nodes[self._root_id])

    def traverse_with_funcs(self, nodes, node, funcs, solid_only=True):
        """
            Traverse nodes from node as starting node.
            On every node, passing nodes and node as arg and excute all funcs by sequence.
            If one func return true, early stop execution and stop traverse any deeper,
            otherwise, traverse children.
        """
        ret = False
        for f in funcs:
            r = f(nodes, node)
            ret = ret and r
            if ret:
                return
        if not ret:
            children = node.get_children(solid_only)
            for child in children:
                self.traverse_with_funcs(nodes, nodes[child["id"]], funcs)

    def find_leaf_node(self, nodes, node, solid_only=True):
        """
            yield all leaf node
        """
        children = node.get_children(solid_only)

        if len(children) > 0:
            for child in children:
                yield from self.find_leaf_node(nodes, nodes[child["id"]])
        else:
            yield node

    def recursive_remove_child(self, nodes, node, label_to_remove):
        """
            traverse nodes from node
            remove child in node's children if match label_to_remove
        """
        children = node.get_children()
        for child in node.children:
            self.recursive_remove_child(
                nodes, nodes[child["id"]], label_to_remove)
        for label in label_to_remove:
            node.remove_child(label)

    def compute_lineage_nodes(self):
        """
        Reorganize self._nodes to compute lineage_nodes
        This is quite complex and hard to debug. It can easily cause reaching
        max recursion depth error when add_child accidently create a cycle.
        """
        # copy nodes
        self._lineage_nodes = self._nodes.copy()

        # remove MULTIPART_IDENTIFIER edge
        self.recursive_remove_child(self._lineage_nodes,
                                    self._lineage_nodes[self._root_id],
                                    ["MULTIPART_IDENTIFIER"])

        # remove alias edge so that alias name node is isolated thus not
        # ploted in lineage_graph. The actual referred node is kept
        self.recursive_remove_child(
            self._lineage_nodes, self._lineage_nodes[self._root_id], self._alias_node_text)

        # exam all REGULAR_QUERY_SPECIFICATION, relink alias and from_clause

        def onRegularQuerySpecification(nodes, rqs_node):
            if rqs_node.text == "REGULAR_QUERY_SPECIFICATION":

                from_clause_node_id = rqs_node.get_child_id("FROM_CLAUSE")[0]

                # 1.exam all select nodes
                for select_node_id in rqs_node.get_child_id("SELECT"):

                    # 1.1 for all dereference node, link them to its actual node via alias
                    has_dereference = False

                    def onDereference(nodes, der_node):
                        if der_node.text == "DEREFERENCE":
                            nonlocal has_dereference
                            has_dereference = True
                            base_node_id = der_node.get_child_id("BASE")[0]
                            base_node = nodes[base_node_id]
                            if base_node.text in self._alias:
                                actual_node_id = self._alias[base_node.text]["node"]
                                base_node.add_child(
                                    actual_node_id, "_DEREFERENCE")
                            # else:
                            #     raise Exception(
                            #         "DEREFERENCE {} is not defined.".format(base_node.text))
                            return True

                    self.traverse_with_funcs(
                        nodes, nodes[select_node_id], [onDereference])

                    # 1.2 for normal select node
                    # if leaf is in lateral view alias, link them to its actual node via alias
                    # otherwise link them to FROM_CALUSE node
                    if not has_dereference:
                        for leaf_node in self.find_leaf_node(nodes, nodes[select_node_id]):
                            if leaf_node.text not in self._syntax_node_text:
                                if leaf_node.text in self._lateral_view_alias:
                                    actual_node_id = self._lateral_view_alias[leaf_node.text]["node"]
                                    leaf_node.add_child(
                                        actual_node_id, "_LATERAL_VIEW_ALIAS")
                                else:
                                    leaf_node.add_child(
                                        from_clause_node_id, "_FROM_CLAUSE")

                # 2. exam relation node
                def onRelation(nodes, rel_node):
                    if rel_node.text == "RELATION":
                        relation_primary_node_id = rel_node.get_child_id("RELATION_PRIMARY")[
                                                                         0]
                        relation_primary_node = nodes[relation_primary_node_id]

                        # 2.1 for tableName, if it is alias, link to its actual node
                        if relation_primary_node.text in self._alias:
                            actual_node_id = self._alias[relation_primary_node.text]["node"]
                            relation_primary_node.add_child(
                                actual_node_id, "_RELATION_PRIMARY")
                        return True

                self.traverse_with_funcs(
                    nodes, nodes[from_clause_node_id], [onRelation])

                # Lateral view expression node are not further examed. They usually
                # relate to a FROM_CLAUSE, but linking to that FROM CLAUSE node might
                # create a cycle in the lineage_graph to cause program error

                return True

        self.traverse_with_funcs(self._lineage_nodes, self._lineage_nodes[self._root_id], [
                 onRegularQuerySpecification])

        # delete FROM_CLAUSE and CTES edge
        self.recursive_remove_child(self._lineage_nodes,
                                    self._lineage_nodes[self._root_id], ["FROM_CLAUSE", "CTES"])

    def compute_field(self):
        if self._has_pivot_clause:
            raise Exception(
                "Code has pivot clause. Therefore field is value dependent and not computable directly.")

        self._field = []

        # field are extracted from 3 options
        def recursive_rqs(nodes, node):
            if node.text == "REGULAR_QUERY_SPECIFICATION":
                column_number = 0
                for select_node_id in node.get_child_id("SELECT"):
                    select_node = nodes[select_node_id]

                    # option 1 from field_name
                    if select_node.text == "DEREFERENCE":
                        field_name_node_ids = select_node.get_child_id(
                            "FIELD_NAME")
                        field_name_node = nodes[field_name_node_ids[0]]
                        self.add_field(field_name_node.text)
                    # option 2 not defined, use _col*
                    elif select_node.text == "FUNCTION_CALL":
                        self.add_field("_col" + str(column_number))
                        column_number += 1
                    # option 3 from name itself
                    else:
                        self.add_field(select_node.text)
            else:
                # exam root level REGULAR_QUERY_SPECIFICATION only
                children = node.get_children(solid_only=True)
                for child in children:
                    recursive_rqs(nodes, nodes[child["id"]])

        recursive_rqs(self._lineage_nodes, self._lineage_nodes[self._root_id])

    def visit(self, ctx):
        """
            basic visit node function wrapper
        """

        # skip None ctx
        if ctx is None:
            return None

        # add root node
        if self._root_id is None:
            self._root_id = self.node_id(ctx)

        return super().visit(ctx)

    # custom visit functions

    # 282
    def visitQuery(self, ctx):
        this = self.add_node(ctx, "QUERY")
        if ctx.ctes():
            ctes_node = self.visit(ctx.ctes())
            self.add_edge(this, ctes_node, "CTES")
        query_term_node = self.visit(ctx.queryTerm())
        self.add_edge(this, query_term_node)

        # ignore queryOrganization
        # query_organization = self.visit(ctx.queryOrganization())

        return this

    # 323
    def visitCtes(self, ctx):
        this = self.add_node(ctx, "CTES")
        named_query_node = [self.visit(i) for i in ctx.namedQuery()]
        self.add_edge(this, named_query_node, "CTES")
        return this

    # 327
    def visitNamedQuery(self, ctx):
        name_node = self.visit(ctx.name)
        query_node = self.visit(ctx.query())
        self.add_edge(query_node, name_node, "NAMED_QUERY_ALIAS")

        # add alias
        self.add_alias(self._nodes[name_node].text, query_node)

        # add columnAliases
        column_aliases_node = self.visit(ctx.columnAliases)
        self.add_edge(query_node, column_aliases_node, "COLUMN_ALIASES")

        return query_node

    # 417
    def visitQueryTermDefault(self, ctx):
        return self.visit(ctx.queryPrimary())

    # 418-419
    def visitSetOperation(self, ctx):
        this = self.add_node(ctx, ctx.operator.text)
        self.add_edge(this, [self.visit(i) for i in ctx.queryTerm()])

        return this

    # 461
    def visitRegularQuerySpecification(self, ctx):
        this = self.add_node(ctx, "REGULAR_QUERY_SPECIFICATION")

        # selectClause
        select_node = self.visit(ctx.selectClause())
        self.add_edge(this, select_node, "SELECT")

        # fromClause
        if ctx.fromClause():
            from_clause_node = self.visit(ctx.fromClause())
            self.add_edge(this, from_clause_node, "FROM_CLAUSE")

        # lateralView
        if ctx.lateralView():
            lateral_view_node = [self.visit(i) for i in ctx.lateralView()]
            self.add_edge(this, lateral_view_node, "LATERAL_VIEW")

        return this

    # 476
    def visitSelectClause(self, ctx):
        return self.visit(ctx.namedExpressionSeq())

    # 528
    def visitFromClause(self, ctx):
        this = self.add_node(ctx, "FROM_CLAUSE")
        # relation
        relation_node = [self.visit(i) for i in ctx.relation()]
        self.add_edge(this, relation_node, "RELATION")

        # lateral view
        if ctx.lateralView():
            lateral_view_node = [self.visit(i) for i in ctx.lateralView()]
            self.add_edge(this, lateral_view_node, "LATERAL_VIEW")

        # pivotClause
        if ctx.pivotClause():
            self._has_pivot_clause = True
            pivot_clause_node = self.visit(ctx.pivotClause())
            self.add_edge(this, pivot_clause_node,
                          "PIVOT_CLAUSE")

        return this

    # 545
    # def visitPivotClause(self, ctx):

    # 567
    def visitRelation(self, ctx):
        this = self.add_node(ctx, "RELATION")
        relation_node = self.visit(ctx.relationPrimary())
        self.add_edge(this, relation_node, "RELATION_PRIMARY")

        # join
        if ctx.joinRelation():
            join_relation_node = [self.visit(i) for i in ctx.joinRelation()]
            self.add_edge(this, join_relation_node, "JOIN")

        return this

    # 571
    def visitJoinRelation(self, ctx):
        return self.visit(ctx.relationPrimary())

    # 588
    def visitLateralView(self, ctx):
        this = self.add_node(ctx, "LATERAL_VIEW")
        expression_node = [self.visit(i) for i in ctx.expression()]
        self.add_edge(this, expression_node, "EXPRESSION")

        # alias
        if ctx.colName:
            col_name_node = [self.visit(i) for i in ctx.colName]
            self.add_edge(this, col_name_node, "LATERAL_VIEW_ALIAS")

            for c in col_name_node:
                self.add_lateral_view_alias(self._nodes[c].text, this)

        return this

    # 607
    # def visitIdentifierSeq(self, ctx):

    # 627 relationPrimary

    # 628
    def visitTableName(self, ctx):
        multipart_identifier_node = self.visit(ctx.multipartIdentifier())
        text = self._nodes[multipart_identifier_node].text
        dt = text.split(".")
        if len(dt) == 2:
            # database.table
            self.add_dependency(dt[0], dt[1])
        elif len(dt) == 0 or len(dt) > 2:
            # invalid
            raise Exception(
                "Table name '{}' is not in format DATABASE.TABLE thus unresolvable.".format(text))
        elif len(dt) == 1:
            # alias name, refer to another
            name = dt[0]
            if name not in self._alias:
                raise Exception(
                    "Table name '{}' is not in format DATABASE.TABLE thus unresolvable.".format(name))

        # add alias if there is one
        table_alias_node = self.visit(ctx.tableAlias())
        if table_alias_node:
            self.add_edge(multipart_identifier_node, table_alias_node,
                          "TABLE_NAME_ALIAS")
            self.add_alias(
                self._nodes[table_alias_node].text, multipart_identifier_node)
            # return table_alias_node

        return multipart_identifier_node

    # 629
    def visitAliasedQuery(self, ctx):
        query_node = self.visit(ctx.query())

        table_alias_node = self.visit(ctx.tableAlias())
        if table_alias_node:
            self.add_edge(query_node, table_alias_node, "ALIAS_QUERY_ALIAS")
            self.add_alias(self._nodes[table_alias_node].text, query_node)

        return query_node

    # 630
    def visitAliasedRelation(self, ctx):
        relation_node = self.visit(ctx.relation())

        table_alias_node = self.visit(ctx.tableAlias())
        if table_alias_node:
            self.add_edge(relation_node, table_alias_node,
                          "ALIAS_RELATION_ALIAS")
            self.add_alias(self._nodes[table_alias_node].text, relation_node)

        return relation_node

    # 635
    def visitInlineTable(self, ctx):
        this = self.add_node(ctx, "INLINE_TABLE")
        expression_node = [self.visit(i) for i in ctx.expression()]
        self.add_edge(this, expression_node)

        table_alias_node = self.visit(ctx.tableAlias())
        if table_alias_node:
            self.add_edge(this, table_alias_node, "INLINE_TABLE_ALIAS")
            self.add_alias(self._nodes[table_alias_node].text, this)
        return this

    # 639
    def visitFunctionTable(self, ctx):
        this = self.add_node(ctx, "FUNCTION_TABLE")
        expression_node = [self.visit(i) for i in ctx.expression()]
        self.add_edge(this, expression_node)

        table_alias_node = self.visit(ctx.tableAlias())
        if table_alias_node:
            self.add_edge(this, table_alias_node, "FUNCTION_TABLE_ALIAS")
            self.add_alias(self._nodes[table_alias_node].text, this)
        return this

    # 643
    def visitTableAlias(self, ctx):
        if not ctx.strictIdentifier():
            return
        # table name
        strict_identifier_node = self.visit(ctx.strictIdentifier())

        # table column
        if ctx.identifierList():
            identifier_list_node = self.visit(ctx.identifierList())
            self.add_edge(strict_identifier_node,
                          identifier_list_node, "TABLE_ALIAS_COLUMN")

        return strict_identifier_node

    # 661

    def visitMultipartIdentifier(self, ctx):
        parts_node = [self.visit(p) for p in ctx.parts]
        texts = ".".join([self._nodes[n].text for n in parts_node])
        this = self.add_node(ctx, texts)
        self.add_edge(this, parts_node, "MULTIPART_IDENTIFIER")
        return this

    # 673

    def visitNamedExpression(self, ctx):
        expression_node = self.visit(ctx.expression())
        # AS
        if ctx.name:
            name_node = self.visit(ctx.name)
            self.add_edge(name_node, expression_node)
            return name_node
        else:
            return expression_node

    # 677
    def visitNamedExpressionSeq(self, ctx):
        return [self.visit(i) for i in ctx.namedExpression()]

    # 700 booleanExpression
    # 701
    def visitLogicalNot(self, ctx):
        return self.visit(ctx.booleanExpression())
    # 702

    def visitExists(self, ctx):
        return self.visit(ctx.query())

    # 703
    def visitPredicated(self, ctx):
        this = [self.visit(ctx.valueExpression())]
        if ctx.predicate():
            this.append(self.visit(ctx.predicate()))
        return this
    # 704-705

    def visitLogicalBinary(self, ctx):
        return [self.visit(i) for i in ctx.booleanExpression()]

    # 708 predict

    # 709
    def visitBetween(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitInList(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    def visitInSubquery(self, ctx):
        return self.visit(ctx.query())

    def visitRlike(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitLikeList(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitLikeValue(self, ctx):
        return self.visit(ctx.valueExpression())

    # def visitNullPredicate(self, ctx):
    # def visitBooleanPredicate(self, ctx):

    # 717
    def visitDistinctFrom(self, ctx):
        return self.visit(ctx.valueExpression())

    # 720 valueExpression

    # 721
    def visitValueExpressionDefault(self, ctx):
        return self.visit(ctx.primaryExpression())

    # 722
    def visitArithmeticUnary(self, ctx):
        return self.visit(ctx.valueExpression())

    def visitArithmeticBinary(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    def visitComparison(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 731 primaryExpression start

    # 732 currentDatetime
    def visitCurrentDatetime(self, ctx):
        return self.add_node(ctx, "CURRENT_DATETIME")

    # 733
    def visitSearchedCase(self, ctx):
        this = [self.visit(i) for i in ctx.whenClause()]
        if ctx.elseExpression:
            this.append(self.visit(ctx.expression()))
        return this

    # 734
    def visitSimpleCase(self, ctx):
        return [self.visit(ctx.value)] \
            + [self.visit(i) for i in ctx.whenClause()] \
            + [self.visit(ctx.elseExpression)]

    # 735
    def visitCast(self, ctx):
        return self.visit(ctx.expression())

    # 736
    def visitStruct(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 737
    def visitFirst(self, ctx):
        return self.visit(ctx.expression())

    # 738
    def visitLast(self, ctx):
        return self.visit(ctx.expression())

    # 739
    def visitPosition(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 740
    def visitConstantDefault(self, ctx):
        return self.add_node(ctx, "CONSTANT_DEFAULT")

    # 741-742
    def visitStar(self, ctx):
        if ctx.qualifiedName():
            qualified_name_node = self.visit(ctx.qualifiedName())
            this = self.add_node(
                ctx, self._nodes[qualified_name_node].text + ".*")
            self.add_edge(this, qualified_name_node)
        else:
            this = self.add_node(ctx, "*")
        return this

    # 743
    def visitRowConstructor(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    # 744
    def visitSubqueryExpression(self, ctx):
        return self.visit(ctx.query())

    # 745
    def visitFunctionCall(self, ctx):
        this = self.add_node(ctx, "FUNCTION_CALL")
        # parse expression only
        if ctx.expression():
            expression_node = [self.visit(i) for i in ctx.expression()]
            self.add_edge(this, expression_node)
        return this

    # 747-748
    def visitLambda(self, ctx):
        return [self.visit(i) for i in ctx.identifier()] + \
            [self.visit(i) for i in ctx.expression()]
    # 749

    def visitSubscript(self, ctx):
        return [self.visit(ctx.primaryExpression())] \
            + [self.visit(ctx.valueExpression())]
    # 750

    def visitColumnReference(self, ctx):
        return self.visit(ctx.identifier())

    # 751
    def visitDereference(self, ctx):
        primary_expression_node = self.visit(ctx.primaryExpression())
        identifier_node = self.visit(ctx.identifier())
        this = self.add_node(ctx, "DEREFERENCE")
        self.add_edge(this, primary_expression_node, "BASE")
        self.add_edge(this, identifier_node, "FIELD_NAME")

        return this

    # 752
    def visitParenthesizedExpression(self, ctx):
        return self.visit(ctx.expression())

    # 753
    def visitExtract(self, ctx):
        # ignore field
        return self.visit(ctx.valueExpression())

    # 754
    def visitSubstring(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 757
    def visitTrim(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 759
    def visitOverlay(self, ctx):
        return [self.visit(i) for i in ctx.valueExpression()]

    # 847
    def visitWhenClause(self, ctx):
        return [self.visit(i) for i in ctx.expression()]

    # 911
    def visitErrorCapturingIdentifier(self, ctx):
        return self.visit(ctx.identifier())

    # 916
    def visitIdentifier(self, ctx):
        if ctx.strictIdentifier():
            return self.visit(ctx.strictIdentifier())
        elif ctx.strictNonReserved():
            return self.visit(ctx.strictNonReserved())

    # 921, 923
    def visitUnquotedIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText())

    # 926
    def visitQuotedIdentifier(self, ctx):
        return self.add_node(ctx, ctx.getText()[1:-1])
