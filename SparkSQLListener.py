# Generated from SparkSQL/SparkSQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparkSQLParser import SparkSQLParser
else:
    from SparkSQLParser import SparkSQLParser

# This class defines a complete listener for a parse tree produced by SparkSQLParser.
class SparkSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SparkSQLParser#singleStatement.
    def enterSingleStatement(self, ctx:SparkSQLParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleStatement.
    def exitSingleStatement(self, ctx:SparkSQLParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleExpression.
    def enterSingleExpression(self, ctx:SparkSQLParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleExpression.
    def exitSingleExpression(self, ctx:SparkSQLParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleTableIdentifier.
    def enterSingleTableIdentifier(self, ctx:SparkSQLParser.SingleTableIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleTableIdentifier.
    def exitSingleTableIdentifier(self, ctx:SparkSQLParser.SingleTableIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleMultipartIdentifier.
    def enterSingleMultipartIdentifier(self, ctx:SparkSQLParser.SingleMultipartIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleMultipartIdentifier.
    def exitSingleMultipartIdentifier(self, ctx:SparkSQLParser.SingleMultipartIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleFunctionIdentifier.
    def enterSingleFunctionIdentifier(self, ctx:SparkSQLParser.SingleFunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleFunctionIdentifier.
    def exitSingleFunctionIdentifier(self, ctx:SparkSQLParser.SingleFunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleDataType.
    def enterSingleDataType(self, ctx:SparkSQLParser.SingleDataTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleDataType.
    def exitSingleDataType(self, ctx:SparkSQLParser.SingleDataTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleTableSchema.
    def enterSingleTableSchema(self, ctx:SparkSQLParser.SingleTableSchemaContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleTableSchema.
    def exitSingleTableSchema(self, ctx:SparkSQLParser.SingleTableSchemaContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#statementDefault.
    def enterStatementDefault(self, ctx:SparkSQLParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#statementDefault.
    def exitStatementDefault(self, ctx:SparkSQLParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dmlStatement.
    def enterDmlStatement(self, ctx:SparkSQLParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dmlStatement.
    def exitDmlStatement(self, ctx:SparkSQLParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#use.
    def enterUse(self, ctx:SparkSQLParser.UseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#use.
    def exitUse(self, ctx:SparkSQLParser.UseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createNamespace.
    def enterCreateNamespace(self, ctx:SparkSQLParser.CreateNamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createNamespace.
    def exitCreateNamespace(self, ctx:SparkSQLParser.CreateNamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setNamespaceProperties.
    def enterSetNamespaceProperties(self, ctx:SparkSQLParser.SetNamespacePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setNamespaceProperties.
    def exitSetNamespaceProperties(self, ctx:SparkSQLParser.SetNamespacePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setNamespaceLocation.
    def enterSetNamespaceLocation(self, ctx:SparkSQLParser.SetNamespaceLocationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setNamespaceLocation.
    def exitSetNamespaceLocation(self, ctx:SparkSQLParser.SetNamespaceLocationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropNamespace.
    def enterDropNamespace(self, ctx:SparkSQLParser.DropNamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropNamespace.
    def exitDropNamespace(self, ctx:SparkSQLParser.DropNamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showNamespaces.
    def enterShowNamespaces(self, ctx:SparkSQLParser.ShowNamespacesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showNamespaces.
    def exitShowNamespaces(self, ctx:SparkSQLParser.ShowNamespacesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createTable.
    def enterCreateTable(self, ctx:SparkSQLParser.CreateTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createTable.
    def exitCreateTable(self, ctx:SparkSQLParser.CreateTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createHiveTable.
    def enterCreateHiveTable(self, ctx:SparkSQLParser.CreateHiveTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createHiveTable.
    def exitCreateHiveTable(self, ctx:SparkSQLParser.CreateHiveTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createTableLike.
    def enterCreateTableLike(self, ctx:SparkSQLParser.CreateTableLikeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createTableLike.
    def exitCreateTableLike(self, ctx:SparkSQLParser.CreateTableLikeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#replaceTable.
    def enterReplaceTable(self, ctx:SparkSQLParser.ReplaceTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#replaceTable.
    def exitReplaceTable(self, ctx:SparkSQLParser.ReplaceTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#analyze.
    def enterAnalyze(self, ctx:SparkSQLParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#analyze.
    def exitAnalyze(self, ctx:SparkSQLParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#addTableColumns.
    def enterAddTableColumns(self, ctx:SparkSQLParser.AddTableColumnsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#addTableColumns.
    def exitAddTableColumns(self, ctx:SparkSQLParser.AddTableColumnsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#renameTableColumn.
    def enterRenameTableColumn(self, ctx:SparkSQLParser.RenameTableColumnContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#renameTableColumn.
    def exitRenameTableColumn(self, ctx:SparkSQLParser.RenameTableColumnContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropTableColumns.
    def enterDropTableColumns(self, ctx:SparkSQLParser.DropTableColumnsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropTableColumns.
    def exitDropTableColumns(self, ctx:SparkSQLParser.DropTableColumnsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#renameTable.
    def enterRenameTable(self, ctx:SparkSQLParser.RenameTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#renameTable.
    def exitRenameTable(self, ctx:SparkSQLParser.RenameTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setTableProperties.
    def enterSetTableProperties(self, ctx:SparkSQLParser.SetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setTableProperties.
    def exitSetTableProperties(self, ctx:SparkSQLParser.SetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#unsetTableProperties.
    def enterUnsetTableProperties(self, ctx:SparkSQLParser.UnsetTablePropertiesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#unsetTableProperties.
    def exitUnsetTableProperties(self, ctx:SparkSQLParser.UnsetTablePropertiesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#alterTableAlterColumn.
    def enterAlterTableAlterColumn(self, ctx:SparkSQLParser.AlterTableAlterColumnContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#alterTableAlterColumn.
    def exitAlterTableAlterColumn(self, ctx:SparkSQLParser.AlterTableAlterColumnContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#hiveChangeColumn.
    def enterHiveChangeColumn(self, ctx:SparkSQLParser.HiveChangeColumnContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#hiveChangeColumn.
    def exitHiveChangeColumn(self, ctx:SparkSQLParser.HiveChangeColumnContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#hiveReplaceColumns.
    def enterHiveReplaceColumns(self, ctx:SparkSQLParser.HiveReplaceColumnsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#hiveReplaceColumns.
    def exitHiveReplaceColumns(self, ctx:SparkSQLParser.HiveReplaceColumnsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setTableSerDe.
    def enterSetTableSerDe(self, ctx:SparkSQLParser.SetTableSerDeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setTableSerDe.
    def exitSetTableSerDe(self, ctx:SparkSQLParser.SetTableSerDeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#addTablePartition.
    def enterAddTablePartition(self, ctx:SparkSQLParser.AddTablePartitionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#addTablePartition.
    def exitAddTablePartition(self, ctx:SparkSQLParser.AddTablePartitionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#renameTablePartition.
    def enterRenameTablePartition(self, ctx:SparkSQLParser.RenameTablePartitionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#renameTablePartition.
    def exitRenameTablePartition(self, ctx:SparkSQLParser.RenameTablePartitionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropTablePartitions.
    def enterDropTablePartitions(self, ctx:SparkSQLParser.DropTablePartitionsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropTablePartitions.
    def exitDropTablePartitions(self, ctx:SparkSQLParser.DropTablePartitionsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setTableLocation.
    def enterSetTableLocation(self, ctx:SparkSQLParser.SetTableLocationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setTableLocation.
    def exitSetTableLocation(self, ctx:SparkSQLParser.SetTableLocationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#recoverPartitions.
    def enterRecoverPartitions(self, ctx:SparkSQLParser.RecoverPartitionsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#recoverPartitions.
    def exitRecoverPartitions(self, ctx:SparkSQLParser.RecoverPartitionsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropTable.
    def enterDropTable(self, ctx:SparkSQLParser.DropTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropTable.
    def exitDropTable(self, ctx:SparkSQLParser.DropTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropView.
    def enterDropView(self, ctx:SparkSQLParser.DropViewContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropView.
    def exitDropView(self, ctx:SparkSQLParser.DropViewContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createView.
    def enterCreateView(self, ctx:SparkSQLParser.CreateViewContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createView.
    def exitCreateView(self, ctx:SparkSQLParser.CreateViewContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createTempViewUsing.
    def enterCreateTempViewUsing(self, ctx:SparkSQLParser.CreateTempViewUsingContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createTempViewUsing.
    def exitCreateTempViewUsing(self, ctx:SparkSQLParser.CreateTempViewUsingContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#alterViewQuery.
    def enterAlterViewQuery(self, ctx:SparkSQLParser.AlterViewQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#alterViewQuery.
    def exitAlterViewQuery(self, ctx:SparkSQLParser.AlterViewQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createFunction.
    def enterCreateFunction(self, ctx:SparkSQLParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createFunction.
    def exitCreateFunction(self, ctx:SparkSQLParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dropFunction.
    def enterDropFunction(self, ctx:SparkSQLParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dropFunction.
    def exitDropFunction(self, ctx:SparkSQLParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#explain.
    def enterExplain(self, ctx:SparkSQLParser.ExplainContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#explain.
    def exitExplain(self, ctx:SparkSQLParser.ExplainContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showTables.
    def enterShowTables(self, ctx:SparkSQLParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showTables.
    def exitShowTables(self, ctx:SparkSQLParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showTable.
    def enterShowTable(self, ctx:SparkSQLParser.ShowTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showTable.
    def exitShowTable(self, ctx:SparkSQLParser.ShowTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showTblProperties.
    def enterShowTblProperties(self, ctx:SparkSQLParser.ShowTblPropertiesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showTblProperties.
    def exitShowTblProperties(self, ctx:SparkSQLParser.ShowTblPropertiesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showColumns.
    def enterShowColumns(self, ctx:SparkSQLParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showColumns.
    def exitShowColumns(self, ctx:SparkSQLParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showViews.
    def enterShowViews(self, ctx:SparkSQLParser.ShowViewsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showViews.
    def exitShowViews(self, ctx:SparkSQLParser.ShowViewsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showPartitions.
    def enterShowPartitions(self, ctx:SparkSQLParser.ShowPartitionsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showPartitions.
    def exitShowPartitions(self, ctx:SparkSQLParser.ShowPartitionsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showFunctions.
    def enterShowFunctions(self, ctx:SparkSQLParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showFunctions.
    def exitShowFunctions(self, ctx:SparkSQLParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showCreateTable.
    def enterShowCreateTable(self, ctx:SparkSQLParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showCreateTable.
    def exitShowCreateTable(self, ctx:SparkSQLParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#showCurrentNamespace.
    def enterShowCurrentNamespace(self, ctx:SparkSQLParser.ShowCurrentNamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#showCurrentNamespace.
    def exitShowCurrentNamespace(self, ctx:SparkSQLParser.ShowCurrentNamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeFunction.
    def enterDescribeFunction(self, ctx:SparkSQLParser.DescribeFunctionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeFunction.
    def exitDescribeFunction(self, ctx:SparkSQLParser.DescribeFunctionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeNamespace.
    def enterDescribeNamespace(self, ctx:SparkSQLParser.DescribeNamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeNamespace.
    def exitDescribeNamespace(self, ctx:SparkSQLParser.DescribeNamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeRelation.
    def enterDescribeRelation(self, ctx:SparkSQLParser.DescribeRelationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeRelation.
    def exitDescribeRelation(self, ctx:SparkSQLParser.DescribeRelationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeQuery.
    def enterDescribeQuery(self, ctx:SparkSQLParser.DescribeQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeQuery.
    def exitDescribeQuery(self, ctx:SparkSQLParser.DescribeQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#commentNamespace.
    def enterCommentNamespace(self, ctx:SparkSQLParser.CommentNamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#commentNamespace.
    def exitCommentNamespace(self, ctx:SparkSQLParser.CommentNamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#commentTable.
    def enterCommentTable(self, ctx:SparkSQLParser.CommentTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#commentTable.
    def exitCommentTable(self, ctx:SparkSQLParser.CommentTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#refreshTable.
    def enterRefreshTable(self, ctx:SparkSQLParser.RefreshTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#refreshTable.
    def exitRefreshTable(self, ctx:SparkSQLParser.RefreshTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#refreshFunction.
    def enterRefreshFunction(self, ctx:SparkSQLParser.RefreshFunctionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#refreshFunction.
    def exitRefreshFunction(self, ctx:SparkSQLParser.RefreshFunctionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#refreshResource.
    def enterRefreshResource(self, ctx:SparkSQLParser.RefreshResourceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#refreshResource.
    def exitRefreshResource(self, ctx:SparkSQLParser.RefreshResourceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#cacheTable.
    def enterCacheTable(self, ctx:SparkSQLParser.CacheTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#cacheTable.
    def exitCacheTable(self, ctx:SparkSQLParser.CacheTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#uncacheTable.
    def enterUncacheTable(self, ctx:SparkSQLParser.UncacheTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#uncacheTable.
    def exitUncacheTable(self, ctx:SparkSQLParser.UncacheTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#clearCache.
    def enterClearCache(self, ctx:SparkSQLParser.ClearCacheContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#clearCache.
    def exitClearCache(self, ctx:SparkSQLParser.ClearCacheContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#loadData.
    def enterLoadData(self, ctx:SparkSQLParser.LoadDataContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#loadData.
    def exitLoadData(self, ctx:SparkSQLParser.LoadDataContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#truncateTable.
    def enterTruncateTable(self, ctx:SparkSQLParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#truncateTable.
    def exitTruncateTable(self, ctx:SparkSQLParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#repairTable.
    def enterRepairTable(self, ctx:SparkSQLParser.RepairTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#repairTable.
    def exitRepairTable(self, ctx:SparkSQLParser.RepairTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#manageResource.
    def enterManageResource(self, ctx:SparkSQLParser.ManageResourceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#manageResource.
    def exitManageResource(self, ctx:SparkSQLParser.ManageResourceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#failNativeCommand.
    def enterFailNativeCommand(self, ctx:SparkSQLParser.FailNativeCommandContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#failNativeCommand.
    def exitFailNativeCommand(self, ctx:SparkSQLParser.FailNativeCommandContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setTimeZone.
    def enterSetTimeZone(self, ctx:SparkSQLParser.SetTimeZoneContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setTimeZone.
    def exitSetTimeZone(self, ctx:SparkSQLParser.SetTimeZoneContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setQuotedConfiguration.
    def enterSetQuotedConfiguration(self, ctx:SparkSQLParser.SetQuotedConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setQuotedConfiguration.
    def exitSetQuotedConfiguration(self, ctx:SparkSQLParser.SetQuotedConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setConfiguration.
    def enterSetConfiguration(self, ctx:SparkSQLParser.SetConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setConfiguration.
    def exitSetConfiguration(self, ctx:SparkSQLParser.SetConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#resetQuotedConfiguration.
    def enterResetQuotedConfiguration(self, ctx:SparkSQLParser.ResetQuotedConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#resetQuotedConfiguration.
    def exitResetQuotedConfiguration(self, ctx:SparkSQLParser.ResetQuotedConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#resetConfiguration.
    def enterResetConfiguration(self, ctx:SparkSQLParser.ResetConfigurationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#resetConfiguration.
    def exitResetConfiguration(self, ctx:SparkSQLParser.ResetConfigurationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#configKey.
    def enterConfigKey(self, ctx:SparkSQLParser.ConfigKeyContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#configKey.
    def exitConfigKey(self, ctx:SparkSQLParser.ConfigKeyContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#unsupportedHiveNativeCommands.
    def enterUnsupportedHiveNativeCommands(self, ctx:SparkSQLParser.UnsupportedHiveNativeCommandsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#unsupportedHiveNativeCommands.
    def exitUnsupportedHiveNativeCommands(self, ctx:SparkSQLParser.UnsupportedHiveNativeCommandsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createTableHeader.
    def enterCreateTableHeader(self, ctx:SparkSQLParser.CreateTableHeaderContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createTableHeader.
    def exitCreateTableHeader(self, ctx:SparkSQLParser.CreateTableHeaderContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#replaceTableHeader.
    def enterReplaceTableHeader(self, ctx:SparkSQLParser.ReplaceTableHeaderContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#replaceTableHeader.
    def exitReplaceTableHeader(self, ctx:SparkSQLParser.ReplaceTableHeaderContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#bucketSpec.
    def enterBucketSpec(self, ctx:SparkSQLParser.BucketSpecContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#bucketSpec.
    def exitBucketSpec(self, ctx:SparkSQLParser.BucketSpecContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#skewSpec.
    def enterSkewSpec(self, ctx:SparkSQLParser.SkewSpecContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#skewSpec.
    def exitSkewSpec(self, ctx:SparkSQLParser.SkewSpecContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#locationSpec.
    def enterLocationSpec(self, ctx:SparkSQLParser.LocationSpecContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#locationSpec.
    def exitLocationSpec(self, ctx:SparkSQLParser.LocationSpecContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#commentSpec.
    def enterCommentSpec(self, ctx:SparkSQLParser.CommentSpecContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#commentSpec.
    def exitCommentSpec(self, ctx:SparkSQLParser.CommentSpecContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#query.
    def enterQuery(self, ctx:SparkSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#query.
    def exitQuery(self, ctx:SparkSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#insertOverwriteTable.
    def enterInsertOverwriteTable(self, ctx:SparkSQLParser.InsertOverwriteTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#insertOverwriteTable.
    def exitInsertOverwriteTable(self, ctx:SparkSQLParser.InsertOverwriteTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#insertIntoTable.
    def enterInsertIntoTable(self, ctx:SparkSQLParser.InsertIntoTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#insertIntoTable.
    def exitInsertIntoTable(self, ctx:SparkSQLParser.InsertIntoTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#insertOverwriteHiveDir.
    def enterInsertOverwriteHiveDir(self, ctx:SparkSQLParser.InsertOverwriteHiveDirContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#insertOverwriteHiveDir.
    def exitInsertOverwriteHiveDir(self, ctx:SparkSQLParser.InsertOverwriteHiveDirContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#insertOverwriteDir.
    def enterInsertOverwriteDir(self, ctx:SparkSQLParser.InsertOverwriteDirContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#insertOverwriteDir.
    def exitInsertOverwriteDir(self, ctx:SparkSQLParser.InsertOverwriteDirContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#partitionSpecLocation.
    def enterPartitionSpecLocation(self, ctx:SparkSQLParser.PartitionSpecLocationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#partitionSpecLocation.
    def exitPartitionSpecLocation(self, ctx:SparkSQLParser.PartitionSpecLocationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#partitionSpec.
    def enterPartitionSpec(self, ctx:SparkSQLParser.PartitionSpecContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#partitionSpec.
    def exitPartitionSpec(self, ctx:SparkSQLParser.PartitionSpecContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#partitionVal.
    def enterPartitionVal(self, ctx:SparkSQLParser.PartitionValContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#partitionVal.
    def exitPartitionVal(self, ctx:SparkSQLParser.PartitionValContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#namespace.
    def enterNamespace(self, ctx:SparkSQLParser.NamespaceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#namespace.
    def exitNamespace(self, ctx:SparkSQLParser.NamespaceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeFuncName.
    def enterDescribeFuncName(self, ctx:SparkSQLParser.DescribeFuncNameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeFuncName.
    def exitDescribeFuncName(self, ctx:SparkSQLParser.DescribeFuncNameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#describeColName.
    def enterDescribeColName(self, ctx:SparkSQLParser.DescribeColNameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#describeColName.
    def exitDescribeColName(self, ctx:SparkSQLParser.DescribeColNameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#ctes.
    def enterCtes(self, ctx:SparkSQLParser.CtesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#ctes.
    def exitCtes(self, ctx:SparkSQLParser.CtesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#namedQuery.
    def enterNamedQuery(self, ctx:SparkSQLParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#namedQuery.
    def exitNamedQuery(self, ctx:SparkSQLParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableProvider.
    def enterTableProvider(self, ctx:SparkSQLParser.TableProviderContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableProvider.
    def exitTableProvider(self, ctx:SparkSQLParser.TableProviderContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createTableClauses.
    def enterCreateTableClauses(self, ctx:SparkSQLParser.CreateTableClausesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createTableClauses.
    def exitCreateTableClauses(self, ctx:SparkSQLParser.CreateTableClausesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tablePropertyList.
    def enterTablePropertyList(self, ctx:SparkSQLParser.TablePropertyListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tablePropertyList.
    def exitTablePropertyList(self, ctx:SparkSQLParser.TablePropertyListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableProperty.
    def enterTableProperty(self, ctx:SparkSQLParser.TablePropertyContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableProperty.
    def exitTableProperty(self, ctx:SparkSQLParser.TablePropertyContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tablePropertyKey.
    def enterTablePropertyKey(self, ctx:SparkSQLParser.TablePropertyKeyContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tablePropertyKey.
    def exitTablePropertyKey(self, ctx:SparkSQLParser.TablePropertyKeyContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tablePropertyValue.
    def enterTablePropertyValue(self, ctx:SparkSQLParser.TablePropertyValueContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tablePropertyValue.
    def exitTablePropertyValue(self, ctx:SparkSQLParser.TablePropertyValueContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#constantList.
    def enterConstantList(self, ctx:SparkSQLParser.ConstantListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#constantList.
    def exitConstantList(self, ctx:SparkSQLParser.ConstantListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#nestedConstantList.
    def enterNestedConstantList(self, ctx:SparkSQLParser.NestedConstantListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#nestedConstantList.
    def exitNestedConstantList(self, ctx:SparkSQLParser.NestedConstantListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#createFileFormat.
    def enterCreateFileFormat(self, ctx:SparkSQLParser.CreateFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#createFileFormat.
    def exitCreateFileFormat(self, ctx:SparkSQLParser.CreateFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableFileFormat.
    def enterTableFileFormat(self, ctx:SparkSQLParser.TableFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableFileFormat.
    def exitTableFileFormat(self, ctx:SparkSQLParser.TableFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#genericFileFormat.
    def enterGenericFileFormat(self, ctx:SparkSQLParser.GenericFileFormatContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#genericFileFormat.
    def exitGenericFileFormat(self, ctx:SparkSQLParser.GenericFileFormatContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#storageHandler.
    def enterStorageHandler(self, ctx:SparkSQLParser.StorageHandlerContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#storageHandler.
    def exitStorageHandler(self, ctx:SparkSQLParser.StorageHandlerContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#resource.
    def enterResource(self, ctx:SparkSQLParser.ResourceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#resource.
    def exitResource(self, ctx:SparkSQLParser.ResourceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#singleInsertQuery.
    def enterSingleInsertQuery(self, ctx:SparkSQLParser.SingleInsertQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#singleInsertQuery.
    def exitSingleInsertQuery(self, ctx:SparkSQLParser.SingleInsertQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#multiInsertQuery.
    def enterMultiInsertQuery(self, ctx:SparkSQLParser.MultiInsertQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#multiInsertQuery.
    def exitMultiInsertQuery(self, ctx:SparkSQLParser.MultiInsertQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#deleteFromTable.
    def enterDeleteFromTable(self, ctx:SparkSQLParser.DeleteFromTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#deleteFromTable.
    def exitDeleteFromTable(self, ctx:SparkSQLParser.DeleteFromTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#updateTable.
    def enterUpdateTable(self, ctx:SparkSQLParser.UpdateTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#updateTable.
    def exitUpdateTable(self, ctx:SparkSQLParser.UpdateTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#mergeIntoTable.
    def enterMergeIntoTable(self, ctx:SparkSQLParser.MergeIntoTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#mergeIntoTable.
    def exitMergeIntoTable(self, ctx:SparkSQLParser.MergeIntoTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#queryOrganization.
    def enterQueryOrganization(self, ctx:SparkSQLParser.QueryOrganizationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#queryOrganization.
    def exitQueryOrganization(self, ctx:SparkSQLParser.QueryOrganizationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#multiInsertQueryBody.
    def enterMultiInsertQueryBody(self, ctx:SparkSQLParser.MultiInsertQueryBodyContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#multiInsertQueryBody.
    def exitMultiInsertQueryBody(self, ctx:SparkSQLParser.MultiInsertQueryBodyContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:SparkSQLParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:SparkSQLParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setOperation.
    def enterSetOperation(self, ctx:SparkSQLParser.SetOperationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setOperation.
    def exitSetOperation(self, ctx:SparkSQLParser.SetOperationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:SparkSQLParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:SparkSQLParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#fromStmt.
    def enterFromStmt(self, ctx:SparkSQLParser.FromStmtContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#fromStmt.
    def exitFromStmt(self, ctx:SparkSQLParser.FromStmtContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#table.
    def enterTable(self, ctx:SparkSQLParser.TableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#table.
    def exitTable(self, ctx:SparkSQLParser.TableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#inlineTableDefault1.
    def enterInlineTableDefault1(self, ctx:SparkSQLParser.InlineTableDefault1Context):
        pass

    # Exit a parse tree produced by SparkSQLParser#inlineTableDefault1.
    def exitInlineTableDefault1(self, ctx:SparkSQLParser.InlineTableDefault1Context):
        pass


    # Enter a parse tree produced by SparkSQLParser#subquery.
    def enterSubquery(self, ctx:SparkSQLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#subquery.
    def exitSubquery(self, ctx:SparkSQLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sortItem.
    def enterSortItem(self, ctx:SparkSQLParser.SortItemContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sortItem.
    def exitSortItem(self, ctx:SparkSQLParser.SortItemContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#fromStatement.
    def enterFromStatement(self, ctx:SparkSQLParser.FromStatementContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#fromStatement.
    def exitFromStatement(self, ctx:SparkSQLParser.FromStatementContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#fromStatementBody.
    def enterFromStatementBody(self, ctx:SparkSQLParser.FromStatementBodyContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#fromStatementBody.
    def exitFromStatementBody(self, ctx:SparkSQLParser.FromStatementBodyContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#transformQuerySpecification.
    def enterTransformQuerySpecification(self, ctx:SparkSQLParser.TransformQuerySpecificationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#transformQuerySpecification.
    def exitTransformQuerySpecification(self, ctx:SparkSQLParser.TransformQuerySpecificationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#regularQuerySpecification.
    def enterRegularQuerySpecification(self, ctx:SparkSQLParser.RegularQuerySpecificationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#regularQuerySpecification.
    def exitRegularQuerySpecification(self, ctx:SparkSQLParser.RegularQuerySpecificationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#transformClause.
    def enterTransformClause(self, ctx:SparkSQLParser.TransformClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#transformClause.
    def exitTransformClause(self, ctx:SparkSQLParser.TransformClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#selectClause.
    def enterSelectClause(self, ctx:SparkSQLParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#selectClause.
    def exitSelectClause(self, ctx:SparkSQLParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setClause.
    def enterSetClause(self, ctx:SparkSQLParser.SetClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setClause.
    def exitSetClause(self, ctx:SparkSQLParser.SetClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#matchedClause.
    def enterMatchedClause(self, ctx:SparkSQLParser.MatchedClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#matchedClause.
    def exitMatchedClause(self, ctx:SparkSQLParser.MatchedClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#notMatchedClause.
    def enterNotMatchedClause(self, ctx:SparkSQLParser.NotMatchedClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#notMatchedClause.
    def exitNotMatchedClause(self, ctx:SparkSQLParser.NotMatchedClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#matchedAction.
    def enterMatchedAction(self, ctx:SparkSQLParser.MatchedActionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#matchedAction.
    def exitMatchedAction(self, ctx:SparkSQLParser.MatchedActionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#notMatchedAction.
    def enterNotMatchedAction(self, ctx:SparkSQLParser.NotMatchedActionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#notMatchedAction.
    def exitNotMatchedAction(self, ctx:SparkSQLParser.NotMatchedActionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#assignmentList.
    def enterAssignmentList(self, ctx:SparkSQLParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#assignmentList.
    def exitAssignmentList(self, ctx:SparkSQLParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#assignment.
    def enterAssignment(self, ctx:SparkSQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#assignment.
    def exitAssignment(self, ctx:SparkSQLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#whereClause.
    def enterWhereClause(self, ctx:SparkSQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#whereClause.
    def exitWhereClause(self, ctx:SparkSQLParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#havingClause.
    def enterHavingClause(self, ctx:SparkSQLParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#havingClause.
    def exitHavingClause(self, ctx:SparkSQLParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#hint.
    def enterHint(self, ctx:SparkSQLParser.HintContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#hint.
    def exitHint(self, ctx:SparkSQLParser.HintContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#hintStatement.
    def enterHintStatement(self, ctx:SparkSQLParser.HintStatementContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#hintStatement.
    def exitHintStatement(self, ctx:SparkSQLParser.HintStatementContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#fromClause.
    def enterFromClause(self, ctx:SparkSQLParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#fromClause.
    def exitFromClause(self, ctx:SparkSQLParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#aggregationClause.
    def enterAggregationClause(self, ctx:SparkSQLParser.AggregationClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#aggregationClause.
    def exitAggregationClause(self, ctx:SparkSQLParser.AggregationClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#groupingSet.
    def enterGroupingSet(self, ctx:SparkSQLParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#groupingSet.
    def exitGroupingSet(self, ctx:SparkSQLParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#pivotClause.
    def enterPivotClause(self, ctx:SparkSQLParser.PivotClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#pivotClause.
    def exitPivotClause(self, ctx:SparkSQLParser.PivotClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#pivotColumn.
    def enterPivotColumn(self, ctx:SparkSQLParser.PivotColumnContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#pivotColumn.
    def exitPivotColumn(self, ctx:SparkSQLParser.PivotColumnContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#pivotValue.
    def enterPivotValue(self, ctx:SparkSQLParser.PivotValueContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#pivotValue.
    def exitPivotValue(self, ctx:SparkSQLParser.PivotValueContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#lateralView.
    def enterLateralView(self, ctx:SparkSQLParser.LateralViewContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#lateralView.
    def exitLateralView(self, ctx:SparkSQLParser.LateralViewContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#setQuantifier.
    def enterSetQuantifier(self, ctx:SparkSQLParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#setQuantifier.
    def exitSetQuantifier(self, ctx:SparkSQLParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#relation.
    def enterRelation(self, ctx:SparkSQLParser.RelationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#relation.
    def exitRelation(self, ctx:SparkSQLParser.RelationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#joinRelation.
    def enterJoinRelation(self, ctx:SparkSQLParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#joinRelation.
    def exitJoinRelation(self, ctx:SparkSQLParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#joinType.
    def enterJoinType(self, ctx:SparkSQLParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#joinType.
    def exitJoinType(self, ctx:SparkSQLParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#joinCriteria.
    def enterJoinCriteria(self, ctx:SparkSQLParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#joinCriteria.
    def exitJoinCriteria(self, ctx:SparkSQLParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sample.
    def enterSample(self, ctx:SparkSQLParser.SampleContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sample.
    def exitSample(self, ctx:SparkSQLParser.SampleContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sampleByPercentile.
    def enterSampleByPercentile(self, ctx:SparkSQLParser.SampleByPercentileContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sampleByPercentile.
    def exitSampleByPercentile(self, ctx:SparkSQLParser.SampleByPercentileContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sampleByRows.
    def enterSampleByRows(self, ctx:SparkSQLParser.SampleByRowsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sampleByRows.
    def exitSampleByRows(self, ctx:SparkSQLParser.SampleByRowsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sampleByBucket.
    def enterSampleByBucket(self, ctx:SparkSQLParser.SampleByBucketContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sampleByBucket.
    def exitSampleByBucket(self, ctx:SparkSQLParser.SampleByBucketContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#sampleByBytes.
    def enterSampleByBytes(self, ctx:SparkSQLParser.SampleByBytesContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#sampleByBytes.
    def exitSampleByBytes(self, ctx:SparkSQLParser.SampleByBytesContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identifierList.
    def enterIdentifierList(self, ctx:SparkSQLParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identifierList.
    def exitIdentifierList(self, ctx:SparkSQLParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identifierSeq.
    def enterIdentifierSeq(self, ctx:SparkSQLParser.IdentifierSeqContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identifierSeq.
    def exitIdentifierSeq(self, ctx:SparkSQLParser.IdentifierSeqContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#orderedIdentifierList.
    def enterOrderedIdentifierList(self, ctx:SparkSQLParser.OrderedIdentifierListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#orderedIdentifierList.
    def exitOrderedIdentifierList(self, ctx:SparkSQLParser.OrderedIdentifierListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#orderedIdentifier.
    def enterOrderedIdentifier(self, ctx:SparkSQLParser.OrderedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#orderedIdentifier.
    def exitOrderedIdentifier(self, ctx:SparkSQLParser.OrderedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identifierCommentList.
    def enterIdentifierCommentList(self, ctx:SparkSQLParser.IdentifierCommentListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identifierCommentList.
    def exitIdentifierCommentList(self, ctx:SparkSQLParser.IdentifierCommentListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identifierComment.
    def enterIdentifierComment(self, ctx:SparkSQLParser.IdentifierCommentContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identifierComment.
    def exitIdentifierComment(self, ctx:SparkSQLParser.IdentifierCommentContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableName.
    def enterTableName(self, ctx:SparkSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableName.
    def exitTableName(self, ctx:SparkSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#aliasedQuery.
    def enterAliasedQuery(self, ctx:SparkSQLParser.AliasedQueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#aliasedQuery.
    def exitAliasedQuery(self, ctx:SparkSQLParser.AliasedQueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:SparkSQLParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:SparkSQLParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#inlineTableDefault2.
    def enterInlineTableDefault2(self, ctx:SparkSQLParser.InlineTableDefault2Context):
        pass

    # Exit a parse tree produced by SparkSQLParser#inlineTableDefault2.
    def exitInlineTableDefault2(self, ctx:SparkSQLParser.InlineTableDefault2Context):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableValuedFunction.
    def enterTableValuedFunction(self, ctx:SparkSQLParser.TableValuedFunctionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableValuedFunction.
    def exitTableValuedFunction(self, ctx:SparkSQLParser.TableValuedFunctionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#inlineTable.
    def enterInlineTable(self, ctx:SparkSQLParser.InlineTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#inlineTable.
    def exitInlineTable(self, ctx:SparkSQLParser.InlineTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#functionTable.
    def enterFunctionTable(self, ctx:SparkSQLParser.FunctionTableContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#functionTable.
    def exitFunctionTable(self, ctx:SparkSQLParser.FunctionTableContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableAlias.
    def enterTableAlias(self, ctx:SparkSQLParser.TableAliasContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableAlias.
    def exitTableAlias(self, ctx:SparkSQLParser.TableAliasContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#rowFormatSerde.
    def enterRowFormatSerde(self, ctx:SparkSQLParser.RowFormatSerdeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#rowFormatSerde.
    def exitRowFormatSerde(self, ctx:SparkSQLParser.RowFormatSerdeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#rowFormatDelimited.
    def enterRowFormatDelimited(self, ctx:SparkSQLParser.RowFormatDelimitedContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#rowFormatDelimited.
    def exitRowFormatDelimited(self, ctx:SparkSQLParser.RowFormatDelimitedContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#multipartIdentifierList.
    def enterMultipartIdentifierList(self, ctx:SparkSQLParser.MultipartIdentifierListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#multipartIdentifierList.
    def exitMultipartIdentifierList(self, ctx:SparkSQLParser.MultipartIdentifierListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#multipartIdentifier.
    def enterMultipartIdentifier(self, ctx:SparkSQLParser.MultipartIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#multipartIdentifier.
    def exitMultipartIdentifier(self, ctx:SparkSQLParser.MultipartIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tableIdentifier.
    def enterTableIdentifier(self, ctx:SparkSQLParser.TableIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tableIdentifier.
    def exitTableIdentifier(self, ctx:SparkSQLParser.TableIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:SparkSQLParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:SparkSQLParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#namedExpression.
    def enterNamedExpression(self, ctx:SparkSQLParser.NamedExpressionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#namedExpression.
    def exitNamedExpression(self, ctx:SparkSQLParser.NamedExpressionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#namedExpressionSeq.
    def enterNamedExpressionSeq(self, ctx:SparkSQLParser.NamedExpressionSeqContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#namedExpressionSeq.
    def exitNamedExpressionSeq(self, ctx:SparkSQLParser.NamedExpressionSeqContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#transformList.
    def enterTransformList(self, ctx:SparkSQLParser.TransformListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#transformList.
    def exitTransformList(self, ctx:SparkSQLParser.TransformListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identityTransform.
    def enterIdentityTransform(self, ctx:SparkSQLParser.IdentityTransformContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identityTransform.
    def exitIdentityTransform(self, ctx:SparkSQLParser.IdentityTransformContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#applyTransform.
    def enterApplyTransform(self, ctx:SparkSQLParser.ApplyTransformContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#applyTransform.
    def exitApplyTransform(self, ctx:SparkSQLParser.ApplyTransformContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#transformArgument.
    def enterTransformArgument(self, ctx:SparkSQLParser.TransformArgumentContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#transformArgument.
    def exitTransformArgument(self, ctx:SparkSQLParser.TransformArgumentContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#expression.
    def enterExpression(self, ctx:SparkSQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#expression.
    def exitExpression(self, ctx:SparkSQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#logicalNot.
    def enterLogicalNot(self, ctx:SparkSQLParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#logicalNot.
    def exitLogicalNot(self, ctx:SparkSQLParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#predicated.
    def enterPredicated(self, ctx:SparkSQLParser.PredicatedContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#predicated.
    def exitPredicated(self, ctx:SparkSQLParser.PredicatedContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#exists.
    def enterExists(self, ctx:SparkSQLParser.ExistsContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#exists.
    def exitExists(self, ctx:SparkSQLParser.ExistsContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#logicalBinary.
    def enterLogicalBinary(self, ctx:SparkSQLParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#logicalBinary.
    def exitLogicalBinary(self, ctx:SparkSQLParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#bewteen.
    def enterBewteen(self, ctx:SparkSQLParser.BewteenContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#bewteen.
    def exitBewteen(self, ctx:SparkSQLParser.BewteenContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#inList.
    def enterInList(self, ctx:SparkSQLParser.InListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#inList.
    def exitInList(self, ctx:SparkSQLParser.InListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#inSubquery.
    def enterInSubquery(self, ctx:SparkSQLParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#inSubquery.
    def exitInSubquery(self, ctx:SparkSQLParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#rlike.
    def enterRlike(self, ctx:SparkSQLParser.RlikeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#rlike.
    def exitRlike(self, ctx:SparkSQLParser.RlikeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#likeList.
    def enterLikeList(self, ctx:SparkSQLParser.LikeListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#likeList.
    def exitLikeList(self, ctx:SparkSQLParser.LikeListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#likeValue.
    def enterLikeValue(self, ctx:SparkSQLParser.LikeValueContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#likeValue.
    def exitLikeValue(self, ctx:SparkSQLParser.LikeValueContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#nullPredicate.
    def enterNullPredicate(self, ctx:SparkSQLParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#nullPredicate.
    def exitNullPredicate(self, ctx:SparkSQLParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#booleanPredicate.
    def enterBooleanPredicate(self, ctx:SparkSQLParser.BooleanPredicateContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#booleanPredicate.
    def exitBooleanPredicate(self, ctx:SparkSQLParser.BooleanPredicateContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#distinctFrom.
    def enterDistinctFrom(self, ctx:SparkSQLParser.DistinctFromContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#distinctFrom.
    def exitDistinctFrom(self, ctx:SparkSQLParser.DistinctFromContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:SparkSQLParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:SparkSQLParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#comparison.
    def enterComparison(self, ctx:SparkSQLParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#comparison.
    def exitComparison(self, ctx:SparkSQLParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:SparkSQLParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:SparkSQLParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:SparkSQLParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:SparkSQLParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#struct.
    def enterStruct(self, ctx:SparkSQLParser.StructContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#struct.
    def exitStruct(self, ctx:SparkSQLParser.StructContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#dereference.
    def enterDereference(self, ctx:SparkSQLParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#dereference.
    def exitDereference(self, ctx:SparkSQLParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#simpleCase.
    def enterSimpleCase(self, ctx:SparkSQLParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#simpleCase.
    def exitSimpleCase(self, ctx:SparkSQLParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#columnReference.
    def enterColumnReference(self, ctx:SparkSQLParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#columnReference.
    def exitColumnReference(self, ctx:SparkSQLParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#rowConstructor.
    def enterRowConstructor(self, ctx:SparkSQLParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#rowConstructor.
    def exitRowConstructor(self, ctx:SparkSQLParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#last.
    def enterLast(self, ctx:SparkSQLParser.LastContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#last.
    def exitLast(self, ctx:SparkSQLParser.LastContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#star.
    def enterStar(self, ctx:SparkSQLParser.StarContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#star.
    def exitStar(self, ctx:SparkSQLParser.StarContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#overlay.
    def enterOverlay(self, ctx:SparkSQLParser.OverlayContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#overlay.
    def exitOverlay(self, ctx:SparkSQLParser.OverlayContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#subscript.
    def enterSubscript(self, ctx:SparkSQLParser.SubscriptContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#subscript.
    def exitSubscript(self, ctx:SparkSQLParser.SubscriptContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:SparkSQLParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:SparkSQLParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#substring.
    def enterSubstring(self, ctx:SparkSQLParser.SubstringContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#substring.
    def exitSubstring(self, ctx:SparkSQLParser.SubstringContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#currentDatetime.
    def enterCurrentDatetime(self, ctx:SparkSQLParser.CurrentDatetimeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#currentDatetime.
    def exitCurrentDatetime(self, ctx:SparkSQLParser.CurrentDatetimeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#cast.
    def enterCast(self, ctx:SparkSQLParser.CastContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#cast.
    def exitCast(self, ctx:SparkSQLParser.CastContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#constantDefault.
    def enterConstantDefault(self, ctx:SparkSQLParser.ConstantDefaultContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#constantDefault.
    def exitConstantDefault(self, ctx:SparkSQLParser.ConstantDefaultContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#lambda.
    def enterLambda(self, ctx:SparkSQLParser.LambdaContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#lambda.
    def exitLambda(self, ctx:SparkSQLParser.LambdaContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:SparkSQLParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:SparkSQLParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#extract.
    def enterExtract(self, ctx:SparkSQLParser.ExtractContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#extract.
    def exitExtract(self, ctx:SparkSQLParser.ExtractContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#trim.
    def enterTrim(self, ctx:SparkSQLParser.TrimContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#trim.
    def exitTrim(self, ctx:SparkSQLParser.TrimContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#functionCall.
    def enterFunctionCall(self, ctx:SparkSQLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#functionCall.
    def exitFunctionCall(self, ctx:SparkSQLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#searchedCase.
    def enterSearchedCase(self, ctx:SparkSQLParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#searchedCase.
    def exitSearchedCase(self, ctx:SparkSQLParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#position.
    def enterPosition(self, ctx:SparkSQLParser.PositionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#position.
    def exitPosition(self, ctx:SparkSQLParser.PositionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#first.
    def enterFirst(self, ctx:SparkSQLParser.FirstContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#first.
    def exitFirst(self, ctx:SparkSQLParser.FirstContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#nullLiteral.
    def enterNullLiteral(self, ctx:SparkSQLParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#nullLiteral.
    def exitNullLiteral(self, ctx:SparkSQLParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:SparkSQLParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:SparkSQLParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#typeConstructor.
    def enterTypeConstructor(self, ctx:SparkSQLParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#typeConstructor.
    def exitTypeConstructor(self, ctx:SparkSQLParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SparkSQLParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SparkSQLParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SparkSQLParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SparkSQLParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#stringLiteral.
    def enterStringLiteral(self, ctx:SparkSQLParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#stringLiteral.
    def exitStringLiteral(self, ctx:SparkSQLParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SparkSQLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SparkSQLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:SparkSQLParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:SparkSQLParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#predicateOperator.
    def enterPredicateOperator(self, ctx:SparkSQLParser.PredicateOperatorContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#predicateOperator.
    def exitPredicateOperator(self, ctx:SparkSQLParser.PredicateOperatorContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#booleanValue.
    def enterBooleanValue(self, ctx:SparkSQLParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#booleanValue.
    def exitBooleanValue(self, ctx:SparkSQLParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#interval.
    def enterInterval(self, ctx:SparkSQLParser.IntervalContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#interval.
    def exitInterval(self, ctx:SparkSQLParser.IntervalContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#errorCapturingMultiUnitsInterval.
    def enterErrorCapturingMultiUnitsInterval(self, ctx:SparkSQLParser.ErrorCapturingMultiUnitsIntervalContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#errorCapturingMultiUnitsInterval.
    def exitErrorCapturingMultiUnitsInterval(self, ctx:SparkSQLParser.ErrorCapturingMultiUnitsIntervalContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#multiUnitsInterval.
    def enterMultiUnitsInterval(self, ctx:SparkSQLParser.MultiUnitsIntervalContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#multiUnitsInterval.
    def exitMultiUnitsInterval(self, ctx:SparkSQLParser.MultiUnitsIntervalContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#errorCapturingUnitToUnitInterval.
    def enterErrorCapturingUnitToUnitInterval(self, ctx:SparkSQLParser.ErrorCapturingUnitToUnitIntervalContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#errorCapturingUnitToUnitInterval.
    def exitErrorCapturingUnitToUnitInterval(self, ctx:SparkSQLParser.ErrorCapturingUnitToUnitIntervalContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#unitToUnitInterval.
    def enterUnitToUnitInterval(self, ctx:SparkSQLParser.UnitToUnitIntervalContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#unitToUnitInterval.
    def exitUnitToUnitInterval(self, ctx:SparkSQLParser.UnitToUnitIntervalContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#intervalValue.
    def enterIntervalValue(self, ctx:SparkSQLParser.IntervalValueContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#intervalValue.
    def exitIntervalValue(self, ctx:SparkSQLParser.IntervalValueContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#colPosition.
    def enterColPosition(self, ctx:SparkSQLParser.ColPositionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#colPosition.
    def exitColPosition(self, ctx:SparkSQLParser.ColPositionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#complexDataType.
    def enterComplexDataType(self, ctx:SparkSQLParser.ComplexDataTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#complexDataType.
    def exitComplexDataType(self, ctx:SparkSQLParser.ComplexDataTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#primitiveDataType.
    def enterPrimitiveDataType(self, ctx:SparkSQLParser.PrimitiveDataTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#primitiveDataType.
    def exitPrimitiveDataType(self, ctx:SparkSQLParser.PrimitiveDataTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#qualifiedColTypeWithPositionList.
    def enterQualifiedColTypeWithPositionList(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#qualifiedColTypeWithPositionList.
    def exitQualifiedColTypeWithPositionList(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#qualifiedColTypeWithPosition.
    def enterQualifiedColTypeWithPosition(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#qualifiedColTypeWithPosition.
    def exitQualifiedColTypeWithPosition(self, ctx:SparkSQLParser.QualifiedColTypeWithPositionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#colTypeList.
    def enterColTypeList(self, ctx:SparkSQLParser.ColTypeListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#colTypeList.
    def exitColTypeList(self, ctx:SparkSQLParser.ColTypeListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#colType.
    def enterColType(self, ctx:SparkSQLParser.ColTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#colType.
    def exitColType(self, ctx:SparkSQLParser.ColTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#complexColTypeList.
    def enterComplexColTypeList(self, ctx:SparkSQLParser.ComplexColTypeListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#complexColTypeList.
    def exitComplexColTypeList(self, ctx:SparkSQLParser.ComplexColTypeListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#complexColType.
    def enterComplexColType(self, ctx:SparkSQLParser.ComplexColTypeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#complexColType.
    def exitComplexColType(self, ctx:SparkSQLParser.ComplexColTypeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#whenClause.
    def enterWhenClause(self, ctx:SparkSQLParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#whenClause.
    def exitWhenClause(self, ctx:SparkSQLParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#windowClause.
    def enterWindowClause(self, ctx:SparkSQLParser.WindowClauseContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#windowClause.
    def exitWindowClause(self, ctx:SparkSQLParser.WindowClauseContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#namedWindow.
    def enterNamedWindow(self, ctx:SparkSQLParser.NamedWindowContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#namedWindow.
    def exitNamedWindow(self, ctx:SparkSQLParser.NamedWindowContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#windowRef.
    def enterWindowRef(self, ctx:SparkSQLParser.WindowRefContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#windowRef.
    def exitWindowRef(self, ctx:SparkSQLParser.WindowRefContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#windowDef.
    def enterWindowDef(self, ctx:SparkSQLParser.WindowDefContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#windowDef.
    def exitWindowDef(self, ctx:SparkSQLParser.WindowDefContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#windowFrame.
    def enterWindowFrame(self, ctx:SparkSQLParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#windowFrame.
    def exitWindowFrame(self, ctx:SparkSQLParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#frameBound.
    def enterFrameBound(self, ctx:SparkSQLParser.FrameBoundContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#frameBound.
    def exitFrameBound(self, ctx:SparkSQLParser.FrameBoundContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:SparkSQLParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:SparkSQLParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#functionName.
    def enterFunctionName(self, ctx:SparkSQLParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#functionName.
    def exitFunctionName(self, ctx:SparkSQLParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#qualifiedName.
    def enterQualifiedName(self, ctx:SparkSQLParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#qualifiedName.
    def exitQualifiedName(self, ctx:SparkSQLParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#errorCapturingIdentifier.
    def enterErrorCapturingIdentifier(self, ctx:SparkSQLParser.ErrorCapturingIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#errorCapturingIdentifier.
    def exitErrorCapturingIdentifier(self, ctx:SparkSQLParser.ErrorCapturingIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#identifier.
    def enterIdentifier(self, ctx:SparkSQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#identifier.
    def exitIdentifier(self, ctx:SparkSQLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:SparkSQLParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:SparkSQLParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#quotedIdentifierAlternative.
    def enterQuotedIdentifierAlternative(self, ctx:SparkSQLParser.QuotedIdentifierAlternativeContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#quotedIdentifierAlternative.
    def exitQuotedIdentifierAlternative(self, ctx:SparkSQLParser.QuotedIdentifierAlternativeContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:SparkSQLParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:SparkSQLParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#exponentLiteral.
    def enterExponentLiteral(self, ctx:SparkSQLParser.ExponentLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#exponentLiteral.
    def exitExponentLiteral(self, ctx:SparkSQLParser.ExponentLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SparkSQLParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SparkSQLParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SparkSQLParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SparkSQLParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#bigIntLiteral.
    def enterBigIntLiteral(self, ctx:SparkSQLParser.BigIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#bigIntLiteral.
    def exitBigIntLiteral(self, ctx:SparkSQLParser.BigIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#smallIntLiteral.
    def enterSmallIntLiteral(self, ctx:SparkSQLParser.SmallIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#smallIntLiteral.
    def exitSmallIntLiteral(self, ctx:SparkSQLParser.SmallIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#tinyIntLiteral.
    def enterTinyIntLiteral(self, ctx:SparkSQLParser.TinyIntLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#tinyIntLiteral.
    def exitTinyIntLiteral(self, ctx:SparkSQLParser.TinyIntLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:SparkSQLParser.DoubleLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:SparkSQLParser.DoubleLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#floatLiteral.
    def enterFloatLiteral(self, ctx:SparkSQLParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#floatLiteral.
    def exitFloatLiteral(self, ctx:SparkSQLParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#bigDecimalLiteral.
    def enterBigDecimalLiteral(self, ctx:SparkSQLParser.BigDecimalLiteralContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#bigDecimalLiteral.
    def exitBigDecimalLiteral(self, ctx:SparkSQLParser.BigDecimalLiteralContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#alterColumnAction.
    def enterAlterColumnAction(self, ctx:SparkSQLParser.AlterColumnActionContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#alterColumnAction.
    def exitAlterColumnAction(self, ctx:SparkSQLParser.AlterColumnActionContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#strictNonReserved.
    def enterStrictNonReserved(self, ctx:SparkSQLParser.StrictNonReservedContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#strictNonReserved.
    def exitStrictNonReserved(self, ctx:SparkSQLParser.StrictNonReservedContext):
        pass


    # Enter a parse tree produced by SparkSQLParser#nonReserved.
    def enterNonReserved(self, ctx:SparkSQLParser.NonReservedContext):
        pass

    # Exit a parse tree produced by SparkSQLParser#nonReserved.
    def exitNonReserved(self, ctx:SparkSQLParser.NonReservedContext):
        pass



del SparkSQLParser