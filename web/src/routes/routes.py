from pyramid.response import FileResponse
import modules.settings

def get_home(req):
    """
    Sends a file response for the main webpage html file

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    # this is how to acccess api instantiation
    # settings.api_interface.doSomething()
    return FileResponse("index.html")

def get_create_account(req):
    """
    Sends a file response for the create account webpage html file

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    # this is how to acccess api instantiation
    # settings.api_interface.doSomething()
    return FileResponse("/pages/createProfile.html")

def get_log_in_account(req):
    """
    Sends a file response for the log in webpage html file

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    # this is how to acccess api instantiation
    # settings.api_interface.doSomething()
    return FileResponse("/pages/login.html")

# def create_event(req):
#     """
#     Creates a new Event

#     Returns:
#     Returns a FileResponse object that is associated with this route
#     :type: FileResponse()
#     """
    
#     return FileResponse("index.html")

def create_account(req):
    """
    Creates a new account for customers
    collects customer credentials and send the sent direct customer to the 
    home/dashboard page

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("index.html")

def login_verify(req):
    """
    Verify customers credentials entered are correct  
    and send customer to home/dashboard page

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("index.html")

def venue_login_page(req):

    """
    login page 

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    
    return FileResponse("index.html")