from pyramid.response import FileResponse
# import modules.settings

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
    
    return FileResponse("login.html")

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
    
    return response

def get_create_account(req):
    """
    Send account view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("createAccount.html")

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
    
    return response