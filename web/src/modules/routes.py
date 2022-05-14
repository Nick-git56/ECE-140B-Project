from pyramid.response import FileResponse
import settings

def get_home(req):
    """
    Sends a file response for the main webpage html file

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    # this is how to acccess api instantiation
    settings.api_interface.doSomething()
    return FileResponse("index.html")

def get_temp(req):
    """
    Sends a file response for a temporary webpage

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    return FileResponse("pages/temp.html")

def create_event(req):
    """
    Creates a new Event

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("index.html")

def create_account(req):
    """
    Creates a new account for customers
    collects customer credentials and send the sent direct customer to the 
    home/dashboard page

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("home.html")

def login_verify(req):
    """
    Verify customers credentials entered are correct  
    and send customer to home/dashboard page

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("home.html")

def venue_login_page(req):

    """
    login page 

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("home.html")