from pyramid.response import FileResponse

def get_home(req):
    """
    Sends a file response for the main webpage html file

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    return FileResponse("index.html")

def get_temp(req):
    """
    Sends a file response for a temporary webpage

    Returns:
    Returns a FileResponse object that is associated with this route
    :type: FileResponse()
    """
    return FileResponse("pages/temp.html")