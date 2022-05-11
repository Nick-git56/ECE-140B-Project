from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import mysql.connector as mysql
import os

from routes import routes


db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']


def getController():
  """
  Creates controller that has Route Configurations

  Returns:
  Controller that will be used for controlling routes redirection for the server
  :type: Configurator()
  """
  config = Configurator()

  config.add_route('get_home', '/')
  config.add_view(routes.get_home, route_name='get_home')

  config.add_route('get_temp', '/temp')
  config.add_view(routes.get_temp, route_name='get_temp')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  return app


if __name__=="__main__":
  # setup controller for server
  app = getController()

  # start server
  server = make_server('0.0.0.0', 6000, app)

  try: 
    server.serve_forever()
  except KeyboardInterrupt:
    print("Shutting down server...")