# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
import datetime
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists TeamMembers;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE TeamMembers (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      major       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

# Insert Records
query = "insert into TeamMembers (first_name, last_name, email, major, created_at) values (%s, %s, %s, %s, %s)"
values = [
  ('Nicholas','Munoz','nmunoz@ucsd.edu', 'Electrical Engineering', datetime.datetime.now()),
  ('Raymond','Urbina','raurbina@ucsd.edu', 'Electrical Engineering', datetime.datetime.now()),
  ('Rusul','Albusultan','ralbussul@ucsd.edu', 'Electrical Engineering', datetime.datetime.now()),
  ('Marcin','Kierebinski','mrkiereb@ucsd.edu', 'Mechanical Engineering', datetime.datetime.now())
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from TeamMembers;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
