from pyramid.response import FileResponse
from modules.settings import api_interface
from modules.system.api import API

def get_home(req):
    """
    Send main webpage

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """

    return FileResponse("index.html")

def get_venue_login(req):

    """
    Send login view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/login.html")

def get_login_verify(req):
    """
    Verify login information

    Returns:
    Returns a dictionary that stores states if information is verified or not
    :type: Dict()
    """

    response = {
        "verified":     True,
        "username":     True,
        "password":     True,
    }

    username_val = req['username']
    pass_val = req['password']
    new_account = False
    # create API object and make it accessible globally
    settings.settings(username_val,pass_val,new_account)
    
    return response

def get_create_account(req):
    """
    Send account view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/createAccount.html")

def get_account_verify(req):
    """
    Verify account information

    Returns:
    Returns a dictionary that stores states if information is verified or not
    :type: Dict()
    """

    response = {
        "verified":     True,
        "first_name":   True,
        "last_name":    True,
        "email":        True,
        "username":     True,
        "password":     True,
    }

    username_val = req['username']
    pass_val = req['password']
    new_account = True
    # create API object and make it accessible globally
    settings.settings(username_val,pass_val,new_account)
    
    return response