from pyramid.response import FileResponse
# from modules.settings import api_interface
from modules import settings
# from modules.system.api import API

def get_home(req):
    """
    Send main webpage

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    settings.api_interface.doSomething()

    return FileResponse("index.html")

def get_organizer_login(req):

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

    # test data so delete when done testing
    username_val = req['username'] # test data
    pass_val = req['password'] # test data
    new_account = False # test data

    # api_interface.

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

    # Error message
    result = None

    response = {
        "verified":     True,
        "first_name":   True,
        "last_name":    True,
        "email":        True,
        "username":     True,
        "password":     True,
    }

    # test data ... delete after testing
    test={}
    test['username'] = req['username']
    test['password'] = req['password']
    test['organizer_user'] = False # boolean for what type of user : VIP or Venue Organizer
    # result = api_interface.create_user(test)

    # if result is None:
    #     # no error
    # else:
    #     # error message
    
    return response

def get_contact_us(req):
    """
    Send contact us view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/contactUs.html")

def get_organizer(req):
    """
    Send organizer view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/organizerPage.html")

def get_vip(req):
    """
    Send vip view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/vipPage.html")

def get_about_us(req):
    """
    Send about us view

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/aboutUs.html")

def get_test1(req):
    """
    

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/dashboard.html")

def get_test2(req):
    """
    

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("pages/event.html")