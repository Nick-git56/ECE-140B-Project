"""
"""
from modules.system.controller import EventController,DataController


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

    def create_event(self):
        """Create a new Event
        """
        pass


    def edit_event(self):
        """Edit an existing Event
        """
        pass

    def new_customer(self):
        """create a new Customer
        """
        pass

    def new_user(self):
        """Create a new User
        """
        pass
    
    def new_employee(self):
        """Create a new Employee
        """
        pass

    def create_transaction(self):
        """Create a new transaction
        """
        pass

    def create_service(self):
        """Create a new service
        """
        pass

    def create_suite(self):
        """
        """
        pass

