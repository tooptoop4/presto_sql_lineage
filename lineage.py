from antlr4.error.ErrorListener import ErrorListener
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl
from antlr4.error.ErrorListener import ErrorListener

import re
from typing import *

import SparkSQL
from SparkSQL.SparkSQLLexer import SparkSQLLexer
from SparkSQL.SparkSQLParser import SparkSQLParser
from SparkSQL.visitor import SparkSQLVisitor

STRICT_NONRESERVED = ["ANTI", "CROSS", "EXCEPT", "FULL", "INNER", "INTERSECT",
                      "JOIN", "LEFT", "NATURAL", "ON", "RIGHT", "SEMI", "SETMINUS", "UNION", "USING"]

NONRESERVED = ["ADD", "AFTER", "ALL", "ALTER", "ANALYZE", "AND", "ANY", "ARCHIVE", "ARRAY", "AS", "ASC", "AT", "AUTHORIZATION", "BETWEEN", "BOTH", "BUCKET", "BUCKETS", "BY", "CACHE", "CASCADE", "CASE", "CAST", "CHANGE", "CHECK", "CLEAR", "CLUSTER", "CLUSTERED", "CODEGEN", "COLLATE", "COLLECTION", "COLUMN", "COLUMNS", "COMMENT", "COMMIT", "COMPACT", "COMPACTIONS", "COMPUTE", "CONCATENATE", "CONSTRAINT", "COST", "CREATE", "CUBE", "CURRENT", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "DATA", "DATABASE", "DATABASES", "DBPROPERTIES", "DEFINED", "DELETE", "DELIMITED", "DESC", "DESCRIBE", "DFS", "DIRECTORIES", "DIRECTORY", "DISTINCT", "DISTRIBUTE", "DIV", "DROP", "ELSE", "END", "ESCAPE", "ESCAPED", "EXCHANGE", "EXISTS", "EXPLAIN", "EXPORT", "EXTENDED", "EXTERNAL", "EXTRACT", "FALSE", "FETCH", "FILTER", "FIELDS", "FILEFORMAT", "FIRST", "FOLLOWING", "FOR", "FOREIGN", "FORMAT", "FORMATTED", "FROM", "FUNCTION", "FUNCTIONS", "GLOBAL", "GRANT", "GROUP", "GROUPING", "HAVING", "IF", "IGNORE", "IMPORT", "IN", "INDEX", "INDEXES", "INPATH", "INPUTFORMAT", "INSERT", "INTERVAL", "INTO", "IS", "ITEMS", "KEYS", "LAST", "LATERAL", "LAZY", "LEADING", "LIKE", "LIMIT", "LINES", "LIST", "LOAD", "LOCAL",
               "LOCATION", "LOCK", "LOCKS", "LOGICAL", "MACRO", "MAP", "MATCHED", "MERGE", "MSCK", "NAMESPACE", "NAMESPACES", "NO", "NOT", "NULL", "NULLS", "OF", "ONLY", "OPTION", "OPTIONS", "OR", "ORDER", "OUT", "OUTER", "OUTPUTFORMAT", "OVER", "OVERLAPS", "OVERLAY", "OVERWRITE", "PARTITION", "PARTITIONED", "PARTITIONS", "PERCENTLIT", "PIVOT", "PLACING", "POSITION", "PRECEDING", "PRIMARY", "PRINCIPALS", "PROPERTIES", "PURGE", "QUERY", "RANGE", "RECORDREADER", "RECORDWRITER", "RECOVER", "REDUCE", "REFERENCES", "REFRESH", "RENAME", "REPAIR", "REPLACE", "RESET", "RESTRICT", "REVOKE", "RLIKE", "ROLE", "ROLES", "ROLLBACK", "ROLLUP", "ROW", "ROWS", "SCHEMA", "SELECT", "SEPARATED", "SERDE", "SERDEPROPERTIES", "SESSION_USER", "SET", "SETS", "SHOW", "SKEWED", "SOME", "SORT", "SORTED", "START", "STATISTICS", "STORED", "STRATIFY", "STRUCT", "SUBSTR", "SUBSTRING", "TABLE", "TABLES", "TABLESAMPLE", "TBLPROPERTIES", "TEMPORARY", "TERMINATED", "THEN", "TIME", "TO", "TOUCH", "TRAILING", "TRANSACTION", "TRANSACTIONS", "TRANSFORM", "TRIM", "TRUE", "TRUNCATE", "TYPE", "UNARCHIVE", "UNBOUNDED", "UNCACHE", "UNIQUE", "UNKNOWN", "UNLOCK", "UNSET", "UPDATE", "USE", "USER", "VALUES", "VIEW", "VIEWS", "WHEN", "WHERE", "WINDOW", "WITH", "ZONE"]

KEYWORDS = dict.fromkeys(set(STRICT_NONRESERVED+NONRESERVED), 1)


def format_sparksql(query: str) -> str:
    """
        format query string
    """

    # remove inline comment --
    q = re.sub(r"\-\-.*", "", query)

    # remove embedded or multi-line comment /* */ in a non-greedy fashion
    q = re.sub(r"\/\*[\s\S]*?\*\/", "", q)

    # remove \n
    q = re.sub(r"\n", " ", q)

    # replace multiple whitespace with one whitespace
    q = re.sub(r"\s+", " ", q.strip())

    # remove hints
    q = re.sub(r"\/\*\+[\s\S]*?\*\/", "", q)

    return q


def capitalize_sparksql(query: str) -> str:
    """
        capitalize keywords
    """

    # uppcase all reserved words
    tokens = re.split(r"([^A-Za-z0-9\+\-\"'`_@:%])", query)
    for i in range(len(tokens)):
        # ignre identifers after AS
        if i > 2 and tokens[i-1] == " " and tokens[i - 2] == "AS":
            continue
        up = tokens[i].upper()
        if up in KEYWORDS:
            tokens[i] = up

    return "".join(tokens)


class RaiseExceptionListner(ErrorListener):
    def __init__(self):
        super(RaiseExceptionListner, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(msg)


def parse_sparksql(query: str):
    """
        parse query using SparkSQL parser
    """
    input_stream = InputStream(query)
    lexer = SparkSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SparkSQLParser(stream)
    parser.addErrorListener(RaiseExceptionListner())
    tree = parser.query()
    rule_names = parser.ruleNames
    return tree, rule_names


def analyse_sparksql(tree, rule_names):
    """
        analyse dependency and field
    """
    visitor = SparkSQLVisitor(rule_names)
    visitor.visit(tree)

    visitor.compute_lineage_nodes()
    visitor.build_lineage_graph()
    visitor.compute_field()

    return visitor
