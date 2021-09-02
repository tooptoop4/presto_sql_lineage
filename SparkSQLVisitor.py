# Generated from SparkSQL/SparkSQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparkSQLParser import SparkSQLParser
else:
    from SparkSQLParser import SparkSQLParser

# This class defines a complete generic visitor for a parse tree produced by SparkSQLParser.

class SparkSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SparkSQLParser#singleStatement.
    def visitSingleStatement(self, ctx:SparkSQLParser.SingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleExpression.
    def visitSingleExpression(self, ctx:SparkSQLParser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleTableIdentifier.
    def visitSingleTableIdentifier(self, ctx:SparkSQLParser.SingleTableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleMultipartIdentifier.
    def visitSingleMultipartIdentifier(self, ctx:SparkSQLParser.SingleMultipartIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleFunctionIdentifier.
    def visitSingleFunctionIdentifier(self, ctx:SparkSQLParser.SingleFunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleDataType.
    def visitSingleDataType(self, ctx:SparkSQLParser.SingleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleTableSchema.
    def visitSingleTableSchema(self, ctx:SparkSQLParser.SingleTableSchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#statementDefault.
    def visitStatementDefault(self, ctx:SparkSQLParser.StatementDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dmlStatement.
    def visitDmlStatement(self, ctx:SparkSQLParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#use.
    def visitUse(self, ctx:SparkSQLParser.UseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createNamespace.
    def visitCreateNamespace(self, ctx:SparkSQLParser.CreateNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setNamespaceProperties.
    def visitSetNamespaceProperties(self, ctx:SparkSQLParser.SetNamespacePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setNamespaceLocation.
    def visitSetNamespaceLocation(self, ctx:SparkSQLParser.SetNamespaceLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropNamespace.
    def visitDropNamespace(self, ctx:SparkSQLParser.DropNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showNamespaces.
    def visitShowNamespaces(self, ctx:SparkSQLParser.ShowNamespacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createTable.
    def visitCreateTable(self, ctx:SparkSQLParser.CreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createHiveTable.
    def visitCreateHiveTable(self, ctx:SparkSQLParser.CreateHiveTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createTableLike.
    def visitCreateTableLike(self, ctx:SparkSQLParser.CreateTableLikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#replaceTable.
    def visitReplaceTable(self, ctx:SparkSQLParser.ReplaceTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#analyze.
    def visitAnalyze(self, ctx:SparkSQLParser.AnalyzeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#addTableColumns.
    def visitAddTableColumns(self, ctx:SparkSQLParser.AddTableColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#renameTableColumn.
    def visitRenameTableColumn(self, ctx:SparkSQLParser.RenameTableColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropTableColumns.
    def visitDropTableColumns(self, ctx:SparkSQLParser.DropTableColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#renameTable.
    def visitRenameTable(self, ctx:SparkSQLParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setTableProperties.
    def visitSetTableProperties(self, ctx:SparkSQLParser.SetTablePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#unsetTableProperties.
    def visitUnsetTableProperties(self, ctx:SparkSQLParser.UnsetTablePropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#alterTableAlterColumn.
    def visitAlterTableAlterColumn(self, ctx:SparkSQLParser.AlterTableAlterColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#hiveChangeColumn.
    def visitHiveChangeColumn(self, ctx:SparkSQLParser.HiveChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#hiveReplaceColumns.
    def visitHiveReplaceColumns(self, ctx:SparkSQLParser.HiveReplaceColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setTableSerDe.
    def visitSetTableSerDe(self, ctx:SparkSQLParser.SetTableSerDeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#addTablePartition.
    def visitAddTablePartition(self, ctx:SparkSQLParser.AddTablePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#renameTablePartition.
    def visitRenameTablePartition(self, ctx:SparkSQLParser.RenameTablePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropTablePartitions.
    def visitDropTablePartitions(self, ctx:SparkSQLParser.DropTablePartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setTableLocation.
    def visitSetTableLocation(self, ctx:SparkSQLParser.SetTableLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#recoverPartitions.
    def visitRecoverPartitions(self, ctx:SparkSQLParser.RecoverPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropTable.
    def visitDropTable(self, ctx:SparkSQLParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropView.
    def visitDropView(self, ctx:SparkSQLParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createView.
    def visitCreateView(self, ctx:SparkSQLParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createTempViewUsing.
    def visitCreateTempViewUsing(self, ctx:SparkSQLParser.CreateTempViewUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#alterViewQuery.
    def visitAlterViewQuery(self, ctx:SparkSQLParser.AlterViewQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createFunction.
    def visitCreateFunction(self, ctx:SparkSQLParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dropFunction.
    def visitDropFunction(self, ctx:SparkSQLParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#explain.
    def visitExplain(self, ctx:SparkSQLParser.ExplainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showTables.
    def visitShowTables(self, ctx:SparkSQLParser.ShowTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showTable.
    def visitShowTable(self, ctx:SparkSQLParser.ShowTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showTblProperties.
    def visitShowTblProperties(self, ctx:SparkSQLParser.ShowTblPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showColumns.
    def visitShowColumns(self, ctx:SparkSQLParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showViews.
    def visitShowViews(self, ctx:SparkSQLParser.ShowViewsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showPartitions.
    def visitShowPartitions(self, ctx:SparkSQLParser.ShowPartitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showFunctions.
    def visitShowFunctions(self, ctx:SparkSQLParser.ShowFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showCreateTable.
    def visitShowCreateTable(self, ctx:SparkSQLParser.ShowCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#showCurrentNamespace.
    def visitShowCurrentNamespace(self, ctx:SparkSQLParser.ShowCurrentNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeFunction.
    def visitDescribeFunction(self, ctx:SparkSQLParser.DescribeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeNamespace.
    def visitDescribeNamespace(self, ctx:SparkSQLParser.DescribeNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeRelation.
    def visitDescribeRelation(self, ctx:SparkSQLParser.DescribeRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeQuery.
    def visitDescribeQuery(self, ctx:SparkSQLParser.DescribeQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#commentNamespace.
    def visitCommentNamespace(self, ctx:SparkSQLParser.CommentNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#commentTable.
    def visitCommentTable(self, ctx:SparkSQLParser.CommentTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#refreshTable.
    def visitRefreshTable(self, ctx:SparkSQLParser.RefreshTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#refreshFunction.
    def visitRefreshFunction(self, ctx:SparkSQLParser.RefreshFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#refreshResource.
    def visitRefreshResource(self, ctx:SparkSQLParser.RefreshResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#cacheTable.
    def visitCacheTable(self, ctx:SparkSQLParser.CacheTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#uncacheTable.
    def visitUncacheTable(self, ctx:SparkSQLParser.UncacheTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#clearCache.
    def visitClearCache(self, ctx:SparkSQLParser.ClearCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#loadData.
    def visitLoadData(self, ctx:SparkSQLParser.LoadDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#truncateTable.
    def visitTruncateTable(self, ctx:SparkSQLParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#repairTable.
    def visitRepairTable(self, ctx:SparkSQLParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#manageResource.
    def visitManageResource(self, ctx:SparkSQLParser.ManageResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#failNativeCommand.
    def visitFailNativeCommand(self, ctx:SparkSQLParser.FailNativeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setTimeZone.
    def visitSetTimeZone(self, ctx:SparkSQLParser.SetTimeZoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setQuotedConfiguration.
    def visitSetQuotedConfiguration(self, ctx:SparkSQLParser.SetQuotedConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setConfiguration.
    def visitSetConfiguration(self, ctx:SparkSQLParser.SetConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#resetQuotedConfiguration.
    def visitResetQuotedConfiguration(self, ctx:SparkSQLParser.ResetQuotedConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#resetConfiguration.
    def visitResetConfiguration(self, ctx:SparkSQLParser.ResetConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#configKey.
    def visitConfigKey(self, ctx:SparkSQLParser.ConfigKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#unsupportedHiveNativeCommands.
    def visitUnsupportedHiveNativeCommands(self, ctx:SparkSQLParser.UnsupportedHiveNativeCommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createTableHeader.
    def visitCreateTableHeader(self, ctx:SparkSQLParser.CreateTableHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#replaceTableHeader.
    def visitReplaceTableHeader(self, ctx:SparkSQLParser.ReplaceTableHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#bucketSpec.
    def visitBucketSpec(self, ctx:SparkSQLParser.BucketSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#skewSpec.
    def visitSkewSpec(self, ctx:SparkSQLParser.SkewSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#locationSpec.
    def visitLocationSpec(self, ctx:SparkSQLParser.LocationSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#commentSpec.
    def visitCommentSpec(self, ctx:SparkSQLParser.CommentSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#query.
    def visitQuery(self, ctx:SparkSQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#insertOverwriteTable.
    def visitInsertOverwriteTable(self, ctx:SparkSQLParser.InsertOverwriteTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#insertIntoTable.
    def visitInsertIntoTable(self, ctx:SparkSQLParser.InsertIntoTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#insertOverwriteHiveDir.
    def visitInsertOverwriteHiveDir(self, ctx:SparkSQLParser.InsertOverwriteHiveDirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#insertOverwriteDir.
    def visitInsertOverwriteDir(self, ctx:SparkSQLParser.InsertOverwriteDirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#partitionSpecLocation.
    def visitPartitionSpecLocation(self, ctx:SparkSQLParser.PartitionSpecLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#partitionSpec.
    def visitPartitionSpec(self, ctx:SparkSQLParser.PartitionSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#partitionVal.
    def visitPartitionVal(self, ctx:SparkSQLParser.PartitionValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#namespace.
    def visitNamespace(self, ctx:SparkSQLParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeFuncName.
    def visitDescribeFuncName(self, ctx:SparkSQLParser.DescribeFuncNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#describeColName.
    def visitDescribeColName(self, ctx:SparkSQLParser.DescribeColNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#ctes.
    def visitCtes(self, ctx:SparkSQLParser.CtesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#namedQuery.
    def visitNamedQuery(self, ctx:SparkSQLParser.NamedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableProvider.
    def visitTableProvider(self, ctx:SparkSQLParser.TableProviderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createTableClauses.
    def visitCreateTableClauses(self, ctx:SparkSQLParser.CreateTableClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tablePropertyList.
    def visitTablePropertyList(self, ctx:SparkSQLParser.TablePropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableProperty.
    def visitTableProperty(self, ctx:SparkSQLParser.TablePropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tablePropertyKey.
    def visitTablePropertyKey(self, ctx:SparkSQLParser.TablePropertyKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tablePropertyValue.
    def visitTablePropertyValue(self, ctx:SparkSQLParser.TablePropertyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#constantList.
    def visitConstantList(self, ctx:SparkSQLParser.ConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#nestedConstantList.
    def visitNestedConstantList(self, ctx:SparkSQLParser.NestedConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#createFileFormat.
    def visitCreateFileFormat(self, ctx:SparkSQLParser.CreateFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableFileFormat.
    def visitTableFileFormat(self, ctx:SparkSQLParser.TableFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#genericFileFormat.
    def visitGenericFileFormat(self, ctx:SparkSQLParser.GenericFileFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#storageHandler.
    def visitStorageHandler(self, ctx:SparkSQLParser.StorageHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#resource.
    def visitResource(self, ctx:SparkSQLParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#singleInsertQuery.
    def visitSingleInsertQuery(self, ctx:SparkSQLParser.SingleInsertQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#multiInsertQuery.
    def visitMultiInsertQuery(self, ctx:SparkSQLParser.MultiInsertQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#deleteFromTable.
    def visitDeleteFromTable(self, ctx:SparkSQLParser.DeleteFromTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#updateTable.
    def visitUpdateTable(self, ctx:SparkSQLParser.UpdateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#mergeIntoTable.
    def visitMergeIntoTable(self, ctx:SparkSQLParser.MergeIntoTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#queryOrganization.
    def visitQueryOrganization(self, ctx:SparkSQLParser.QueryOrganizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#multiInsertQueryBody.
    def visitMultiInsertQueryBody(self, ctx:SparkSQLParser.MultiInsertQueryBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#queryTermDefault.
    def visitQueryTermDefault(self, ctx:SparkSQLParser.QueryTermDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setOperation.
    def visitSetOperation(self, ctx:SparkSQLParser.SetOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#queryPrimaryDefault.
    def visitQueryPrimaryDefault(self, ctx:SparkSQLParser.QueryPrimaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#fromStmt.
    def visitFromStmt(self, ctx:SparkSQLParser.FromStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#table.
    def visitTable(self, ctx:SparkSQLParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#inlineTableDefault1.
    def visitInlineTableDefault1(self, ctx:SparkSQLParser.InlineTableDefault1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#subquery.
    def visitSubquery(self, ctx:SparkSQLParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sortItem.
    def visitSortItem(self, ctx:SparkSQLParser.SortItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#fromStatement.
    def visitFromStatement(self, ctx:SparkSQLParser.FromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#fromStatementBody.
    def visitFromStatementBody(self, ctx:SparkSQLParser.FromStatementBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#transformQuerySpecification.
    def visitTransformQuerySpecification(self, ctx:SparkSQLParser.TransformQuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#regularQuerySpecification.
    def visitRegularQuerySpecification(self, ctx:SparkSQLParser.RegularQuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#transformClause.
    def visitTransformClause(self, ctx:SparkSQLParser.TransformClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#selectClause.
    def visitSelectClause(self, ctx:SparkSQLParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setClause.
    def visitSetClause(self, ctx:SparkSQLParser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#matchedClause.
    def visitMatchedClause(self, ctx:SparkSQLParser.MatchedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#notMatchedClause.
    def visitNotMatchedClause(self, ctx:SparkSQLParser.NotMatchedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#matchedAction.
    def visitMatchedAction(self, ctx:SparkSQLParser.MatchedActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#notMatchedAction.
    def visitNotMatchedAction(self, ctx:SparkSQLParser.NotMatchedActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#assignmentList.
    def visitAssignmentList(self, ctx:SparkSQLParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#assignment.
    def visitAssignment(self, ctx:SparkSQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#whereClause.
    def visitWhereClause(self, ctx:SparkSQLParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#havingClause.
    def visitHavingClause(self, ctx:SparkSQLParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#hint.
    def visitHint(self, ctx:SparkSQLParser.HintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#hintStatement.
    def visitHintStatement(self, ctx:SparkSQLParser.HintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#fromClause.
    def visitFromClause(self, ctx:SparkSQLParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#aggregationClause.
    def visitAggregationClause(self, ctx:SparkSQLParser.AggregationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#groupingSet.
    def visitGroupingSet(self, ctx:SparkSQLParser.GroupingSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#pivotClause.
    def visitPivotClause(self, ctx:SparkSQLParser.PivotClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#pivotColumn.
    def visitPivotColumn(self, ctx:SparkSQLParser.PivotColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#pivotValue.
    def visitPivotValue(self, ctx:SparkSQLParser.PivotValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#lateralView.
    def visitLateralView(self, ctx:SparkSQLParser.LateralViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#setQuantifier.
    def visitSetQuantifier(self, ctx:SparkSQLParser.SetQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#relation.
    def visitRelation(self, ctx:SparkSQLParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#joinRelation.
    def visitJoinRelation(self, ctx:SparkSQLParser.JoinRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#joinType.
    def visitJoinType(self, ctx:SparkSQLParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#joinCriteria.
    def visitJoinCriteria(self, ctx:SparkSQLParser.JoinCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sample.
    def visitSample(self, ctx:SparkSQLParser.SampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sampleByPercentile.
    def visitSampleByPercentile(self, ctx:SparkSQLParser.SampleByPercentileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sampleByRows.
    def visitSampleByRows(self, ctx:SparkSQLParser.SampleByRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sampleByBucket.
    def visitSampleByBucket(self, ctx:SparkSQLParser.SampleByBucketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#sampleByBytes.
    def visitSampleByBytes(self, ctx:SparkSQLParser.SampleByBytesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identifierList.
    def visitIdentifierList(self, ctx:SparkSQLParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identifierSeq.
    def visitIdentifierSeq(self, ctx:SparkSQLParser.IdentifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#orderedIdentifierList.
    def visitOrderedIdentifierList(self, ctx:SparkSQLParser.OrderedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#orderedIdentifier.
    def visitOrderedIdentifier(self, ctx:SparkSQLParser.OrderedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identifierCommentList.
    def visitIdentifierCommentList(self, ctx:SparkSQLParser.IdentifierCommentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identifierComment.
    def visitIdentifierComment(self, ctx:SparkSQLParser.IdentifierCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableName.
    def visitTableName(self, ctx:SparkSQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#aliasedQuery.
    def visitAliasedQuery(self, ctx:SparkSQLParser.AliasedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#aliasedRelation.
    def visitAliasedRelation(self, ctx:SparkSQLParser.AliasedRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#inlineTableDefault2.
    def visitInlineTableDefault2(self, ctx:SparkSQLParser.InlineTableDefault2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableValuedFunction.
    def visitTableValuedFunction(self, ctx:SparkSQLParser.TableValuedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#inlineTable.
    def visitInlineTable(self, ctx:SparkSQLParser.InlineTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#functionTable.
    def visitFunctionTable(self, ctx:SparkSQLParser.FunctionTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableAlias.
    def visitTableAlias(self, ctx:SparkSQLParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#rowFormatSerde.
    def visitRowFormatSerde(self, ctx:SparkSQLParser.RowFormatSerdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#rowFormatDelimited.
    def visitRowFormatDelimited(self, ctx:SparkSQLParser.RowFormatDelimitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#multipartIdentifierList.
    def visitMultipartIdentifierList(self, ctx:SparkSQLParser.MultipartIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#multipartIdentifier.
    def visitMultipartIdentifier(self, ctx:SparkSQLParser.MultipartIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tableIdentifier.
    def visitTableIdentifier(self, ctx:SparkSQLParser.TableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#functionIdentifier.
    def visitFunctionIdentifier(self, ctx:SparkSQLParser.FunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#namedExpression.
    def visitNamedExpression(self, ctx:SparkSQLParser.NamedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#namedExpressionSeq.
    def visitNamedExpressionSeq(self, ctx:SparkSQLParser.NamedExpressionSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#transformList.
    def visitTransformList(self, ctx:SparkSQLParser.TransformListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identityTransform.
    def visitIdentityTransform(self, ctx:SparkSQLParser.IdentityTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#applyTransform.
    def visitApplyTransform(self, ctx:SparkSQLParser.ApplyTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#transformArgument.
    def visitTransformArgument(self, ctx:SparkSQLParser.TransformArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#expression.
    def visitExpression(self, ctx:SparkSQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#logicalNot.
    def visitLogicalNot(self, ctx:SparkSQLParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#predicated.
    def visitPredicated(self, ctx:SparkSQLParser.PredicatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#exists.
    def visitExists(self, ctx:SparkSQLParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#logicalBinary.
    def visitLogicalBinary(self, ctx:SparkSQLParser.LogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#bewteen.
    def visitBewteen(self, ctx:SparkSQLParser.BewteenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#inList.
    def visitInList(self, ctx:SparkSQLParser.InListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#inSubquery.
    def visitInSubquery(self, ctx:SparkSQLParser.InSubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#rlike.
    def visitRlike(self, ctx:SparkSQLParser.RlikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#likeList.
    def visitLikeList(self, ctx:SparkSQLParser.LikeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#likeValue.
    def visitLikeValue(self, ctx:SparkSQLParser.LikeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#nullPredicate.
    def visitNullPredicate(self, ctx:SparkSQLParser.NullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#booleanPredicate.
    def visitBooleanPredicate(self, ctx:SparkSQLParser.BooleanPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#distinctFrom.
    def visitDistinctFrom(self, ctx:SparkSQLParser.DistinctFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#valueExpressionDefault.
    def visitValueExpressionDefault(self, ctx:SparkSQLParser.ValueExpressionDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#comparison.
    def visitComparison(self, ctx:SparkSQLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#arithmeticBinary.
    def visitArithmeticBinary(self, ctx:SparkSQLParser.ArithmeticBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#arithmeticUnary.
    def visitArithmeticUnary(self, ctx:SparkSQLParser.ArithmeticUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#struct.
    def visitStruct(self, ctx:SparkSQLParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#dereference.
    def visitDereference(self, ctx:SparkSQLParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#simpleCase.
    def visitSimpleCase(self, ctx:SparkSQLParser.SimpleCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#columnReference.
    def visitColumnReference(self, ctx:SparkSQLParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#rowConstructor.
    def visitRowConstructor(self, ctx:SparkSQLParser.RowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#last.
    def visitLast(self, ctx:SparkSQLParser.LastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#star.
    def visitStar(self, ctx:SparkSQLParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#overlay.
    def visitOverlay(self, ctx:SparkSQLParser.OverlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#subscript.
    def visitSubscript(self, ctx:SparkSQLParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#subqueryExpression.
    def visitSubqueryExpression(self, ctx:SparkSQLParser.SubqueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#substring.
    def visitSubstring(self, ctx:SparkSQLParser.SubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#currentDatetime.
    def visitCurrentDatetime(self, ctx:SparkSQLParser.CurrentDatetimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#cast.
    def visitCast(self, ctx:SparkSQLParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#constantDefault.
    def visitConstantDefault(self, ctx:SparkSQLParser.ConstantDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#lambda.
    def visitLambda(self, ctx:SparkSQLParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:SparkSQLParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#extract.
    def visitExtract(self, ctx:SparkSQLParser.ExtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#trim.
    def visitTrim(self, ctx:SparkSQLParser.TrimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#functionCall.
    def visitFunctionCall(self, ctx:SparkSQLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#searchedCase.
    def visitSearchedCase(self, ctx:SparkSQLParser.SearchedCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#position.
    def visitPosition(self, ctx:SparkSQLParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#first.
    def visitFirst(self, ctx:SparkSQLParser.FirstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#nullLiteral.
    def visitNullLiteral(self, ctx:SparkSQLParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:SparkSQLParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#typeConstructor.
    def visitTypeConstructor(self, ctx:SparkSQLParser.TypeConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#numericLiteral.
    def visitNumericLiteral(self, ctx:SparkSQLParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:SparkSQLParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#stringLiteral.
    def visitStringLiteral(self, ctx:SparkSQLParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:SparkSQLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:SparkSQLParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#predicateOperator.
    def visitPredicateOperator(self, ctx:SparkSQLParser.PredicateOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#booleanValue.
    def visitBooleanValue(self, ctx:SparkSQLParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#interval.
    def visitInterval(self, ctx:SparkSQLParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#errorCapturingMultiUnitsInterval.
    def visitErrorCapturingMultiUnitsInterval(self, ctx:SparkSQLParser.ErrorCapturingMultiUnitsIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#multiUnitsInterval.
    def visitMultiUnitsInterval(self, ctx:SparkSQLParser.MultiUnitsIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#errorCapturingUnitToUnitInterval.
    def visitErrorCapturingUnitToUnitInterval(self, ctx:SparkSQLParser.ErrorCapturingUnitToUnitIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#unitToUnitInterval.
    def visitUnitToUnitInterval(self, ctx:SparkSQLParser.UnitToUnitIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#intervalValue.
    def visitIntervalValue(self, ctx:SparkSQLParser.IntervalValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#colPosition.
    def visitColPosition(self, ctx:SparkSQLParser.ColPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#complexDataType.
    def visitComplexDataType(self, ctx:SparkSQLParser.ComplexDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#primitiveDataType.
    def visitPrimitiveDataType(self, ctx:SparkSQLParser.PrimitiveDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#qualifiedColTypeWithPositionList.
    def visitQualifiedColTypeWithPositionList(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#qualifiedColTypeWithPosition.
    def visitQualifiedColTypeWithPosition(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#colTypeList.
    def visitColTypeList(self, ctx:SparkSQLParser.ColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#colType.
    def visitColType(self, ctx:SparkSQLParser.ColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#complexColTypeList.
    def visitComplexColTypeList(self, ctx:SparkSQLParser.ComplexColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#complexColType.
    def visitComplexColType(self, ctx:SparkSQLParser.ComplexColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#whenClause.
    def visitWhenClause(self, ctx:SparkSQLParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#windowClause.
    def visitWindowClause(self, ctx:SparkSQLParser.WindowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#namedWindow.
    def visitNamedWindow(self, ctx:SparkSQLParser.NamedWindowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#windowRef.
    def visitWindowRef(self, ctx:SparkSQLParser.WindowRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#windowDef.
    def visitWindowDef(self, ctx:SparkSQLParser.WindowDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#windowFrame.
    def visitWindowFrame(self, ctx:SparkSQLParser.WindowFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#frameBound.
    def visitFrameBound(self, ctx:SparkSQLParser.FrameBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:SparkSQLParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#functionName.
    def visitFunctionName(self, ctx:SparkSQLParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#qualifiedName.
    def visitQualifiedName(self, ctx:SparkSQLParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#errorCapturingIdentifier.
    def visitErrorCapturingIdentifier(self, ctx:SparkSQLParser.ErrorCapturingIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#identifier.
    def visitIdentifier(self, ctx:SparkSQLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#unquotedIdentifier.
    def visitUnquotedIdentifier(self, ctx:SparkSQLParser.UnquotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#quotedIdentifierAlternative.
    def visitQuotedIdentifierAlternative(self, ctx:SparkSQLParser.QuotedIdentifierAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#quotedIdentifier.
    def visitQuotedIdentifier(self, ctx:SparkSQLParser.QuotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#exponentLiteral.
    def visitExponentLiteral(self, ctx:SparkSQLParser.ExponentLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:SparkSQLParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:SparkSQLParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#bigIntLiteral.
    def visitBigIntLiteral(self, ctx:SparkSQLParser.BigIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#smallIntLiteral.
    def visitSmallIntLiteral(self, ctx:SparkSQLParser.SmallIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#tinyIntLiteral.
    def visitTinyIntLiteral(self, ctx:SparkSQLParser.TinyIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#doubleLiteral.
    def visitDoubleLiteral(self, ctx:SparkSQLParser.DoubleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#floatLiteral.
    def visitFloatLiteral(self, ctx:SparkSQLParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#bigDecimalLiteral.
    def visitBigDecimalLiteral(self, ctx:SparkSQLParser.BigDecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#alterColumnAction.
    def visitAlterColumnAction(self, ctx:SparkSQLParser.AlterColumnActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#strictNonReserved.
    def visitStrictNonReserved(self, ctx:SparkSQLParser.StrictNonReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparkSQLParser#nonReserved.
    def visitNonReserved(self, ctx:SparkSQLParser.NonReservedContext):
        return self.visitChildren(ctx)



del SparkSQLParser