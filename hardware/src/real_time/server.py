"""Hardware-server 

Responsible for communicating with hardware components(bracelets) and 
uploading this data to the database system
"""
from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
import mysql.connector as mysql
import os
from dotenv import load_dotenv


load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

if __name__=="__main__":
  root_db = mysql.connect(user=db_user, password=db_pass, host=db_host)
  root_cursor = root_db.cursor()
  print("start server...")