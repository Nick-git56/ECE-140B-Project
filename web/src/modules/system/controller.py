"""
"""
from modules.system.planner import EventPlanner
from modules.system.uploader import UserDataUploader,CustomerDataUploader,EmployeeDataUploader


class Controller:
    """Abstract Class representing default Controller
    """
    def __init__(self,controller_type):
        print("Controller object created")
        self._controller_type = controller_type

    def _get_type(self):
        return self._controller_type


class EventController(Controller):
    """Event Controller
    """
    def __init__(self):
        controller_type = "Event Controller"
        super().__init__(controller_type)
        self._event_planner = EventPlanner()


class DataController(Controller):
    """Data Controller
    """
    def __init__(self):
        controller_type = "Data Controller"
        super().__init__(controller_type)
        self._user_uploader = UserDataUploader()
        self._customer_uploader = CustomerDataUploader()
        self._employee_uploader = EmployeeDataUploader()