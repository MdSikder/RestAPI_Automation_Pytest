import json

import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_update_Student_details_byID(base_url):
    post_id_to_update = 1  # Specify the ID of the post to be updated
    student_id = 8348121
    body = {
        "id": 1,
        "first_name": "Md",
        "middle_name": "Porag",
        "last_name": "Sikder",
        "date_of_birth": "11/12/1988"
    }
    headers = {
        "Content-Type": "application/json"  # Add the Content-Type header

    }

    response = requests.put(f"{base_url}/api/studentsDetails/{student_id}", json=body, headers=headers)
    # assert response.status_code == 200
    updated_response = response.json()
    print(json.dumps(updated_response, indent=4))
