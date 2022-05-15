"""
"""
from modules.init_tables import tables
# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
import datetime
from dotenv import load_dotenv


load_dotenv('credentials.env')

complete_tablesList = ['Customers','Events','Companies','Suites','Services','Users','Employees','Transactions','Surveys','Products','RFIDLog','LocationLog']
users_tableList = ['Users','Surveys','LocationLog',]
customers_tableList = complete_tablesList
employees_tableList = ['Employees','Transactions','Products','Surveys','Users','Services']

db_host = os.environ['MYSQL_HOST']
db_name = os.environ['MYSQL_DATABASE']

db_root = os.environ['MYSQL_ROOT']
db_root_pass = os.environ['MYSQL_ROOT_PASSWORD']

db_user = os.environ['MYSQL_USER']
db_user_pass = os.environ['MYSQL_USER_PASSWORD']

db_customer = os.environ['MYSQL_CUSTOMER']
db_customer_pass = os.environ['MYSQL_CUSTOMER_PASSWORD']

db_employee = os.environ['MYSQL_EMPLOYEE']
db_employee_pass = os.environ['MYSQL_EMPLOYEE_PASSWORD']

root_db = mysql.connect(user=db_root, password=db_root_pass, host=db_host)
root_cursor = root_db.cursor()

# create database
root_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
print(f"Do you want to overwrite ALL the contents within the database {db_name}?(y/n)")
response_val = input()
if(response_val=="y"):
  for table in complete_tablesList:
    root_cursor.execute(f"drop table if exists {table};")

# create user
root_cursor.execute(f"CREATE USER '{db_user}'@'{db_host}' IDENTIFIED BY '{db_user_pass}';")
# create customer
root_cursor.execute(f"CREATE USER '{db_customer}'@'{db_host}' IDENTIFIED BY '{db_customer_pass}';")
# create employee
root_cursor.execute(f"CREATE USER '{db_employee}'@'{db_host}' IDENTIFIED BY '{db_employee_pass}';")

# create tables
tables.create_tables(root_cursor)
root_db.commit()

# grant privileges to user
for table in users_tableList:
  root_cursor.execute(f"GRANT INSERT, UPDATE, DELETE, SELECT, REFERENCES ON {db_name}.{table} TO '{db_user}'@'{db_host}'")
# grant privileges to customer
for table in users_tableList:
  root_cursor.execute(f"GRANT INSERT, UPDATE, DELETE, SELECT, REFERENCES ON {db_name}.{table} TO '{db_customer}'@'{db_host}'")
# grant privileges to employee
for table in users_tableList:
  root_cursor.execute(f"GRANT INSERT, UPDATE, DELETE, SELECT, REFERENCES ON {db_name}.{table} TO '{db_employee}'@'{db_host}'")

# GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
# GRANT PRIVILEGE ON database.table TO 'username'@'host';
# root_cursor.execute(f"GRANT ALL PRIVILEGES ON agile_db.* TO '{db_user}'@'{db_host}';")
root_cursor.execute("FLUSH PRIVILEGES;")

root_db.commit()
root_cursor.close()
root_db.close()

# How to grant priveledges
# https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql