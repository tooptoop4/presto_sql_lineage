import sys, traceback, os
import pandas as pd
from lineage import format_sparksql, capitalize_sparksql, parse_sparksql, analyse_sparksql
from sqlalchemy import create_engine


def get_all_paths(node, path=None):
    paths = []
    if path is None:
        path = []
    path.append(node)
    if len(node._children) > 0:
        for child in node._children:
            actual_child = v.nodes[child['id']]
            paths.extend(get_all_paths(actual_child, path[:]))
    else:
        paths.append(path)
    return paths


out_folder = '/home/someuser/output_sql_lineage/'
for f in os.listdir(out_folder):
    os.remove(os.path.join(out_folder, f))

query_cert = '/home/someuser/bundle_truststore.pem'
presto_username = sys.argv[1]
presto_password = sys.argv[2]
presto_dns = sys.argv[3]

presto_url = 'presto://' + presto_username + ':' + presto_password + '@' + presto_dns + ':443'
engine = create_engine(presto_url, connect_args={'protocol': 'https', 'requests_kwargs': {'verify': query_cert},
                                                 'source': 'view_lineage', 'poll_interval': 0.1})

schemas_data = engine.execute("show schemas like '%%'")
schemas_res = pd.DataFrame(schemas_data.fetchall(), columns=schemas_data.keys())

for schemas_index, schemas_row in schemas_res.iterrows():
    list_vw_sql = "select * from information_schema.views where table_catalog = 'hive' and table_schema = '" + \
                  schemas_row["Schema"] + "'"
    data = engine.execute(list_vw_sql)
    res = pd.DataFrame(data.fetchall(), columns=data.keys())
    for index, row in res.iterrows():
        target_view_name = row["table_schema"] + '.' + row["table_name"]
        trg_cols_qry = "select column_name from information_schema.columns where table_catalog = 'hive' and table_name = '" + \
                       row["table_name"].lower() + "' and table_schema = '" + row[
                           "table_schema"].lower() + "' order by ordinal_position"
        trg_cols_data = engine.execute(trg_cols_qry)
        trg_cols_res = [i[0].lower() for i in trg_cols_data.fetchall()]

        q = row["view_definition"]
        q = q.replace('WITH ORDINALITY ', ' ').replace("ESCAPE '\\'", " ").rstrip("\n").rstrip("\r").rstrip(" ")
        if q[0] == '(' and q[-1] == ')':
            q = q[1:-1]
        q_formated = format_sparksql(q)
        q_cap = capitalize_sparksql(q_formated)
        try:
            tree, rule_names = parse_sparksql(q_cap)
            v = analyse_sparksql(tree, rule_names)
            src_tables_count = 0
            src_tables_list = []
            src_table_alias = {}
            cols_in_src_tbl_dict = {}
            for d in v.dependency:
                find_cols_qry = "select column_name from information_schema.columns where table_catalog = 'hive' and table_name = '" + \
                                d['Table'].lower() + "' and table_schema = '" + d[
                                    'Database'].lower() + "' order by ordinal_position"
                find_cols_data = engine.execute(find_cols_qry)
                find_cols_tbl = d['Database'].lower() + '.' + d['Table'].lower()
                src_tables_list.append(find_cols_tbl)
                find_cols_res = [i[0] for i in find_cols_data.fetchall()]
                cols_in_src_tbl_dict[find_cols_tbl] = find_cols_res
                src_tables_count = src_tables_count + 1
            counter = 1
            how_many_paths = 0
            max_how_many_paths = 0
            for n in v.nodes:
                if v.nodes[n]._text == 'REGULAR_QUERY_SPECIFICATION':
                    how_many_paths = len(get_all_paths(v.nodes[n]))
                    if how_many_paths >= max_how_many_paths:
                        initial_query_spec_node = v.nodes[n]
                        max_how_many_paths = how_many_paths

            paths = get_all_paths(initial_query_spec_node)
            deref_lookup = {}
            raw_lineage = []
            fmt_lineage = []
            prior_id = ''
            prior_text = ''
            for n in v.nodes:
                if "primaryExpression" in v.nodes[n]._id and v.nodes[n]._text == "DEREFERENCE":
                    base_path = ''
                    field_path = ''
                    for c in v.nodes[n]._children:
                        if len(v.nodes[c['id']]._children) == 0:
                            field_path = c['id']
                        else:
                            base_path = c['id']

                    if field_path != '' and base_path != '':
                        deref_lookup[base_path] = field_path
                if prior_id and prior_text and "multipartIdentifier" in prior_id and prior_text.lower() in src_tables_list and "strictIdentifier" in \
                        v.nodes[n]._id:
                    src_table_alias[v.nodes[n]._text] = prior_text
                prior_id = v.nodes[n]._id
                prior_text = v.nodes[n]._text
            for path in paths:
                x = 0
                identifier_list = []
                circ_tbl_found = ''
                should_skip = False
                for p in path:
                    if "Identifier" in p._id:
                        if x > 0 and path[x - 1]:
                            for chil in v.nodes[path[x - 1]._id].children:
                                if chil['label'] == 'BASE' and chil['id'] != p._id:
                                    try:
                                        circ_tbl_found = src_table_alias[v.nodes[chil['id']]._text.lower()]
                                    except:
                                        pass
                        text_name = p._text
                        if p._id in deref_lookup:
                            text_name = v.nodes[deref_lookup[p._id]]._text
                        if not any(
                                e['id'] == p._id and e['label'] == 'JOIN' for e in v.nodes[path[x - 1]._id].children):
                            identifier_list.append(text_name)
                    if circ_tbl_found != '' and len(identifier_list) <= 2:
                        identifier_list.append(circ_tbl_found)
                        circ_tbl_found = ''
                    if "querySpecification" in p._id and p._text == "REGULAR_QUERY_SPECIFICATION":
                        if len(identifier_list) > 0 and len(path) > x + 1 and v.nodes[path[x + 1]._id]._text != \
                                identifier_list[-1] and v.nodes[path[x + 1]._id]._text != "*":
                            should_skip = True
                            continue
                    x = x + 1
                counter = counter + 1
                if len(identifier_list) > 0 and identifier_list[0].lower() in trg_cols_res:
                    if len(identifier_list) >= 3 and '.' in identifier_list[-1] and not should_skip and identifier_list[
                        -2].lower() in cols_in_src_tbl_dict[identifier_list[-1].lower()]:
                        raw_lineage.append(identifier_list[0] + "=" + identifier_list[-1] + "/" + identifier_list[-2])
                    elif len(identifier_list) == 2 and '.' in identifier_list[-1] and not should_skip and \
                            identifier_list[0].lower() in cols_in_src_tbl_dict[identifier_list[-1].lower()]:
                        raw_lineage.append(identifier_list[0] + "=" + identifier_list[-1] + "/" + identifier_list[0])
                elif len(identifier_list) == 2 and '.' in identifier_list[-1] and not should_skip:
                    for sss in src_table_alias:
                        if identifier_list[0].lower() == sss.lower() and identifier_list[-1].lower() == src_table_alias[
                            sss]:
                            for cc in cols_in_src_tbl_dict[identifier_list[-1].lower()]:
                                if cc in trg_cols_res:
                                    raw_lineage.append(cc + "=" + identifier_list[-1].lower() + "/" + cc)
                elif len(identifier_list) == 3 and '.' in identifier_list[-1] and identifier_list[
                    1].lower() in trg_cols_res and identifier_list[-1].lower() == src_table_alias[
                    identifier_list[0].lower()] and identifier_list[1].lower() in cols_in_src_tbl_dict[
                    identifier_list[-1].lower()]:
                    raw_lineage.append(identifier_list[1] + "=" + identifier_list[-1] + "/" + identifier_list[1])
            for elem in raw_lineage:
                if elem.lower() not in fmt_lineage:
                    fmt_lineage.append(elem.lower())
            with open(out_folder + target_view_name + '.txt', 'w') as myfile:
                lineage_count = 0
                for e in fmt_lineage:
                    myfile.write(e + '\n')
                    lineage_count = lineage_count + 1
                if lineage_count == 0:
                    if src_tables_count == 1:
                        for c in trg_cols_res:
                            myfile.write(c + "=" + find_cols_tbl + "/" + c + '\n')
                    elif 'union' in q.lower() and q.lower().count('union') == src_tables_count - 1 and q.lower().count(
                        '*') == src_tables_count:
                        for src_tbl in src_tables_list:
                            if cols_in_src_tbl_dict[src_tbl] == trg_cols_res:
                                for c in trg_cols_res:
                                    myfile.write(c + "=" + src_tbl + "/" + c + '\n')
        except:
            print(target_view_name + " failed")
            print(traceback.format_exc())
            pass

