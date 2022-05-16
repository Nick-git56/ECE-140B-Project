"""
"""
import os

class DataUploader:
    """Abstract Class representing default Data Uploader
    """
    def __init__(self,uploader_type):
        print("Data Uploader object created")
        self._uploader_type = uploader_type
        self._db_host = os.environ['MYSQL_HOST']
        self._db_name = os.environ['MYSQL_DATABASE']

    def _get_type(self):
        return self._uploader_type


class UserDataUploader(DataUploader):
    """User Data Uploader
    """
    def __init__(self):
        uploader_type = "User Data Uploader"
        super().__init__(uploader_type)
        self._db_user = os.environ['MYSQL_VIP']
        self._db_pass = os.environ['MYSQL_VIP_PASSWORD']


class CustomerDataUploader(DataUploader):
    """Customer Data Uploader
    """
    def __init__(self):
        uploader_type = "Customer Data Uploader"
        super().__init__(uploader_type)
        self._db_user = os.environ['MYSQL_CUSTOMER']
        self._db_pass = os.environ['MYSQL_CUSTOMER_PASSWORD']


class EmployeeDataUploader(DataUploader):
    """Employee Data Uploader
    """
    def __init__(self):
        uploader_type = "Employee Data Uploader"
        super().__init__(uploader_type)
        self._db_user = os.environ['MYSQL_EMPLOYEE']
        self._db_pass = os.environ['MYSQL_EMPLOYEE_PASSWORD']