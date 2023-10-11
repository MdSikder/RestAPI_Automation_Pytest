####################################################################################
##  https://thetestingworldapi.com/Help/                                            ##
##  documents 'https://thetestingworldapi.com/Help/Api/POST-api-studentsDetails'    ##
##  api - 'http://thetestingworldapi.com/api/studentsDetails'                       ##
####################################################################################

# ************************************---run---*******************************************
import json

import requests
import pytest


@pytest.fixture
def base_url():
    return "https://thetestingworldapi.com"


def test_new_StudentDetails(base_url):
    body = {
        # "id": 1,
        "first_name": "Md",
        "middle_name": "Rased",
        "last_name": "Sikder",
        "date_of_birth": "11/12/1988"
    }

    headers = {
        "Content-Type": "application/json"  # Add the Content-Type header
    }

    response = requests.post(f"{base_url}/api/studentsDetails", json=body, headers=headers)
    assert response.status_code == 201
    created_response = response.json()
    # Validation with created response
    assert created_response["first_name"] == "Md"
    assert created_response["middle_name"] == "Rased"
    assert created_response["last_name"] == "Sikder"
    assert created_response["date_of_birth"] == "11/12/1988"
    print("\n", json.dumps(created_response, indent=4))
    created_response_id = created_response["id"]
    # to collect id for more use
    # print(created_response_id)
