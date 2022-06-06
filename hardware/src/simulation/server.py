"""Hardware-server 

Responsible for communicating with hardware components(bracelets) and 
uploading this data to the database system
"""
from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
import mysql.connector as mysql
import os
from dotenv import load_dotenv

class Server:
  def __init__(self):
    load_dotenv('credentials.env')
    db_user = os.environ['MYSQL_USER']
    db_pass = os.environ['MYSQL_PASSWORD']
    db_name = os.environ['MYSQL_DATABASE']
    db_host = os.environ['MYSQL_HOST']
    self.root_db = mysql.connect(user=db_user, password=db_pass, host=db_host)
    self.root_cursor = self.root_db.cursor()
    self.root_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    self.root_cursor.execute(f"USE {db_name}")

  def show(self):
    self.root_cursor.execute("SHOW TABLES")
    my_result = self.root_cursor.fetchall()
    for x in my_result:
      print(x)

  def insert_record(self,query,values):
    """Insert single record
    """
    self.root_cursor.execute(query,values)
    self.root_db.commit()
    print('---INSERT---')
    print(self.root_cursor.rowcount, "record inserted")

  def insert_records(self,query,values):
    """Insert multiple records
    """
    self.root_cursor.executemany(query,values)
    self.root_db.commit()
    print('---INSERT---')
    print(self.root_cursor.rowcount, "record(s) inserted")

if __name__ == "__main__":
  server = Server()
  query = 'INSERT INTO LocationLogs (id, location_log, rfid_id, created_at) VALUES (%s, %s, %s, %s)'
  values = [('6', 'hello', '10',  '2022-02-11 12:36:09'),
            ('9', 'there', '8',  '2022-02-01 04:23:00'),
            ('420', 'howdy', '78', '2022-02-01 04:41:00')
          ]
  server.show()
  server.insert_record(query, values)