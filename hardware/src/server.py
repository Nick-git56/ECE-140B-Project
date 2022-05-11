from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import mysql.connector as mysql
import os


db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']



if __name__=="__main__":
  print("start server...")