import requests


class EmployeeApi:
    BASE_URL = "http://5.101.50.27:8000"

    def create_employee(self, data: dict):
        return requests.post(f"{self.BASE_URL}/employee/create", json=data)

    def get_employee_info(self, employee_id: int):
        return requests.get(f"{self.BASE_URL}/employee/info", params={"id": employee_id})

    def change_employee(self, employee_id: int, data: dict):
        payload = {"id": employee_id, **data}
        return requests.patch(f"{self.BASE_URL}/employee/change", json=payload)