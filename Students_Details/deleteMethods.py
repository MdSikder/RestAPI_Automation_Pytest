import json

import pytest
import requests


@pytest.fixture
def base_url():
    return "http://thetestingworldapi.com"


def test_delete_student_details_byID(base_url):
    student_id = 8348118

    response = requests.delete(f"{base_url}/api/studentsDetails/{student_id}")
    # assert response.status_code == 200
    data = response.json()
    # Validation
    assert data["status"] == "true"
    assert data["msg"] == "Delete  data success"
    # assert data["status"] == "false"
    # assert data["msg"] == "record not found"
    # response print with prettify  mode
    print("\n", json.dumps(data, indent=4))
