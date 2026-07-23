# Import libraries required for connecting to mysql

import mysql.connector

# Import libraries required for connecting to DB2 or PostgreSql

import psycopg2


# Other libraries


from dotenv import load_dotenv
import os
load_dotenv()

# Connect to MySQL

mysql_conn =  mysql.connector.connect(user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'),host=os.getenv('MYSQL_HOST'),database='sales')

# Connect to DB2 or PostgreSql

dsn_hostname = os.getenv('DSN_HOSTNAME')
dsn_user= os.getenv('DSN_USER')
dsn_pwd = os.getenv('DSN_PWD')
dsn_port = os.getenv('DSN_PORT')
dsn_database = os.getenv('DSN_DATABASE')


# create connection

psql_conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   password=dsn_pwd,
   host=dsn_hostname, 
   port= dsn_port
)


# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    cursor = psql_conn.cursor()
    cursor.execute('SELECT MAX(rowid) FROM sales_data')
    return  cursor.fetchone()[0]

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)


# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    cursor = mysql_conn.cursor()
    cursor.execute(f'SELECT rowid,product_id,customer_id,quantity FROM sales.sales_data WHERE rowid >= {rowid}')
    return cursor.fetchall()

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))


# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
    cursor = psql_conn.cursor()
    query = '''INSERT INTO sales_data (rowid,product_id,customer_id,quantity) VALUES (%s, %s, %s, %s)'''
    cursor.executemany(query,records)
    psql_conn.commit()
    cursor.close()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program



