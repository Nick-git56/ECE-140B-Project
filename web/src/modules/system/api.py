"""
"""
from modules.system.controller import EventController,DataController

# class API_Storage:
#     """Storage for API objects. Each object is related to each ACTIVE USER. A user is active
#     when the user logs in and object is removed when user logs out.
#     """
#     def __init__(self):
#         """Instantiate class object
#         """
#         # KV pair => "username" : API()
#             # username is retrieved from cookies javascript
#             # value when used is copy by reference
#                 # temp = self.api_dict['user']      # temp is now referencing to the API() instantiated object
#         self.api_dict = {}

#     def get_api(self,username):
#         """Retrieves the API object for respective user if the
#         object exists

#         Arguments:
#         :param username: Users username
#         :type username: str

#         Returns:
#         Returns API object or None if it doesn't exist
#         """
#         result = None
#         # check if API() object exists
#         if self.api_dict.get(username) != None:
#             # found object so return it
#             result = self.api_dict[username]
#         return result

#     def add_api(self,username):
#         """User logged in so create API object if it doesn't exist

#         Arguments:
#         :param username: Users username
#         :type username: str

#         Returns:
#         Creates API object and returns boolean based on success
#         """
#         result = False
#         # check if API() object already exists
#         if self.api_dict.get(username) == None:
#             # No object exists so create
#             self.api_dict[username] = API()
#             result = True
#         return result

#     def remove_api(self,username):
#         """User logged out so delete API object if it does exist

#         Arguments:
#         :param username: Users username
#         :type username: str

#         Returns:
#         Deletes API object or None if it doesn't exist
#         """
#         result = False
#         # check if API() object exists
#         if self.api_dict.get(username) != None:
#             # object exists so remove
#             garbage = self.api_dict.pop(username)
#             # make sure object's destructor is called
#             del garbage
#             result = True
#         return result


class API:
    """API that is responsible for dealing with commands and interacting
    with the Data and Event Controller
    """
    def __init__(self):
        """Instantiate API object
        """
        print("API object created")
        self._event_controller = EventController()
        self._data_controller = DataController()

    def doSomething(self):
        print("The API object")

    def create_user(self,data):
        """
        """

        # state represents if data is verified
        message = None

        # check boolean if new user is organizer or VIPs
        if data['organizer_user']:
            # create organizer user
            message = self.create_organizer(data)
        else:
            # create vip user
            message = self.create_vip(data)

        if message is None:
            # data is verified so create user
            self._data_controller.create_user(data)
        
        # return Error message????
        return message

    def create_organizer(self,data):
        """create a new Customer
        """
        pass

    def create_vip(self,data):
        """Create a new User
        """
        pass
    
    def create_employee(self):
        """Create a new Employee
        """
        pass

    def create_event(self,data):
        """Create a new Event

        Arguments:
        :param data: dictionary that contains data collected from website
        :type data: str

        Returns:
        
        """
        pass

    def create_suite(self):
        """
        """
        pass

    def create_service(self):
        """Create a new service
        """
        pass

    # def create_transaction(self):
    #     """Create a new transaction
    #     """
    #     pass

    # def edit_event(self):
    #     """Edit an existing Event
    #     """
    # pass

