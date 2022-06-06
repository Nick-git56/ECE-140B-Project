"""Web-server 

Responsible for creating web-server Controller and the controller is
responsible for managing routes received from the client.
"""
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import mysql.connector as mysql
from dotenv import load_dotenv
import os

from modules import settings
from routes import routes

# NOTE: CLEAR CACHE WHEN LOADING WEBPAGE!!!!!!!(ctr+F5)

# load_dotenv('credentials.env')
# db_user = os.environ['MYSQL_ROOT']
# db_pass = os.environ['MYSQL_ROOT_PASSWORD']
# db_name = os.environ['MYSQL_DATABASE']
# db_host = os.environ['MYSQL_HOST']


def getController():
  """Creates controller that has Route Configurations

  Returns:
  Controller that will be used for controlling routes redirection for the server
  :type: Configurator()
  """
  config = Configurator()

  config.add_route('get_home', '/')
  config.add_view(routes.get_home, route_name='get_home')

  # login view
  config.add_route('get_organizer_login', '/venue_login')
  config.add_view(routes.get_organizer_login, route_name='get_organizer_login')

  # login form completed
  config.add_route('get_login_verify', '/login_verify')
  config.add_view(routes.get_login_verify, route_name='get_login_verify', renderer='json')

  # create account view
  config.add_route('get_create_account', '/create_account')
  config.add_view(routes.get_create_account, route_name='get_create_account')

  # create account form completed
  config.add_route('get_account_verify', '/account_verify')
  config.add_view(routes.get_account_verify, route_name='get_account_verify', renderer='json')

  # contact us view
  config.add_route('get_contact_us', '/contactUs')
  config.add_view(routes.get_contact_us, route_name='get_contact_us')
  
  # contact us view
  config.add_route('get_organizer', '/organizer')
  config.add_view(routes.get_organizer, route_name='get_organizer')

  # contact us view
  config.add_route('get_vip', '/vip')
  config.add_view(routes.get_vip, route_name='get_vip')

  # contact us view
  config.add_route('get_about_us', '/aboutUs')
  config.add_view(routes.get_about_us, route_name='get_about_us')

  # # contact us view
  # config.add_route('get_contact_us', '/contactUs')
  # config.add_view(routes.get_contact_us, route_name='get_contact_us')

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