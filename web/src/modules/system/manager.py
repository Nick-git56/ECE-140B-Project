"""
"""

class Manager:
    """Abstract Class representing default Manager
    """
    def __init__(self,manager_type):
        print("Manager object created")
        self._manager_type = manager_type
    
    def _get_type(self):
        return self._manager_type


class EventManager(Manager):
    """Event Manager
    """
    def __init__(self):
        manager_type = "Event Manager"
        super().__init__(self,manager_type)


class SuiteManager(Manager):
    """Suite Manager
    """
    def __init__(self):
        manager_type = "Suite Manager"
        super().__init__(self,manager_type)


class ServiceManager(Manager):
    """Service Manager
    """
    def __init__(self):
        manager_type = "Service Manger"
        super().__init__(self,manager_type)


class CustomerManager(Manager):
    """Customer Manager
    """
    def __init__(self):
        manager_type = "Customer Manager"
        super().__init__(self,manager_type)