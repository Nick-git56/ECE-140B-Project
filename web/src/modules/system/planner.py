"""
"""
from modules.system.manager import EventManager,SuiteManager,ServiceManager,CustomerManager

class Planner:
    """Abstract Class representing default Planner
    """
    def __init__(self,planner_type):
        print("Planner object created")
        self._planner_type = planner_type
    
    def _get_type(self):
        return self._planner_type


class EventPlanner(Planner):
    """Event Planner
    """
    def __init__(self):
        planner_type = "Event Planner"
        super().__init__(planner_type)
        self._eventManger = EventManager()


class SuitePlanner(Planner):
    """Suite Planner
    """
    def __init__(self):
        planner_type = "Suite Planner"
        super().__init__(planner_type)
        self._suiteManager = SuiteManager()


class ServicePlanner(Planner):
    """Service Planner
    """
    def __init__(self):
        planner_type = "Service Planner"
        super().__init__(planner_type)
        self._serviceManager = ServiceManager()


class CustomerPlanner(Planner):
    """Customer Planner
    """
    def __init__(self):
        planner_type = "Customer Planner"
        super().__init__(planner_type)
        self._customerManager = CustomerManager()