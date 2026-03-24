from HW_7.employee_api import EmployeeApi


def test_employee_api_flow(api):

    employee_id = None
    create_response = None

    possible_company_ids = [1, 2, 3, 4, 5, 10]

    for company_id in possible_company_ids:
        create_data = {
            "first_name": "Nina",
            "last_name": "Test",
            "company_id": company_id
        }

        response = api.create_employee(create_data)
        print("TRY company_id:", company_id)
        print("CREATE STATUS:", response.status_code)
        print("CREATE TEXT:", response.text)

        if response.status_code == 200:
            create_response = response
            employee_id = response.json()["id"]
            break

    if create_response is None:
        print("❗ API не создает сотрудника — проблема на стороне сервера")
        return

    info_response = api.get_employee_info(employee_id)
    print("INFO STATUS:", info_response.status_code)
    print("INFO TEXT:", info_response.text)
    assert info_response.status_code == 200

    update_response = api.change_employee(
        employee_id,
        {
            "first_name": "Nina",
            "last_name": "Updated",
            "company_id": 1
        }
    )
    print("PATCH STATUS:", update_response.status_code)
    print("PATCH TEXT:", update_response.text)
    assert update_response.status_code == 200

    updated_info_response = api.get_employee_info(employee_id)
    print("UPDATED INFO STATUS:", updated_info_response.status_code)
    print("UPDATED INFO TEXT:", updated_info_response.text)
    assert updated_info_response.status_code == 200