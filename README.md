# presto_sql_lineage
Get column-level lineage from Presto SQL Views


# Requirements:
Python 3.7

PrestoSQL 336 (other version will likely work too)

pip3 install PyHive==0.6.4 sqlalchemy==1.3.24 pandasql==0.7.3 antlr4-python3-runtime==4.8 graphviz==0.15

# Usage:

Download this repo to any folder and cd to it

mkdir /home/someuser/output_sql_lineage/

Place presto cert on /home/someuser/bundle_truststore.pem


python3 column_lineage_from_view.py 'my_presto_username' 'my_presto_password' 'my_presto_endpoint'

ie

python3 column_lineage_from_view.py 'bob' 'S@cr7t' 'some.server.com'






For every presto view, a file will be written to /home/someuser/output_sql_lineage/ showing all the source to target column relationships (target columns derived from just literals will not be shown).


ie myschema.viewXYZ.txt file (for myschema.viewXYZ view) will show:

city=schemaA.table1/metro

address=schemaA.table1/street

address=schemaB.table2/postcode

