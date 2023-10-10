import json

import pytest
import requests


@pytest.fixture
def base_url():
    return "http://thetestingworldapi.com"


def test_get_all_students_details(base_url):
    response = requests.get(f"{base_url}/api/studentsDetails")
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=4))


def test_get_student_details_byID(base_url):
    response = requests.get(f"{base_url}/api/studentsDetails/8348121")
    assert response.status_code == 200
    data = response.json()
    # Validation
    assert data["data"]["id"] == 8348110
    assert data["data"]["first_name"] == "Hasan"
    # response print with prettify  mode
    print("\n", json.dumps(data, indent=4))
