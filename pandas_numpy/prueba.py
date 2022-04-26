import pandas as pd
import psycopg2

sql_conn = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')


query_sql = '''
select *
from table_name
limit 10
'''
df = pd.read_sql(query_sql, sql_conn)
df.head(5)
