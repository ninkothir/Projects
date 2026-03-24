import pytest
from HW_7.employee_api import EmployeeApi

@pytest.fixture
def api():
    return EmployeeApi()