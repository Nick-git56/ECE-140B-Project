"""Web-server 

Responsible for creating web-server Controller and the controller is
responsible for managing routes received from the client.
"""
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import mysql.connector as mysql
import os

from modules import routes,settings


db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']


def getController():
  """Creates controller that has Route Configurations

  Returns:
  Controller that will be used for controlling routes redirection for the server
  :type: Configurator()
  """
  config = Configurator()

  config.add_route('get_home', '/')
  config.add_view(routes.get_home, route_name='get_home')

  config.add_route('get_temp', '/temp')
  config.add_view(routes.get_temp, route_name='get_temp')

  config.add_route('create_event', '/createEvent')
  config.add_view(routes.create_event, route_name='create_event')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  return app


if __name__=="__main__":
  # setup controller for server
  app = getController()

  # create API object and make it accessible globally
  settings.settings()

  # start server
  server = make_server('0.0.0.0', 6000, app)

  try: 
    server.serve_forever()
  except KeyboardInterrupt:
    print("Shutting down server...")


# PEP8 guid for beautiful code layout
# https://realpython.com/python-pep8/