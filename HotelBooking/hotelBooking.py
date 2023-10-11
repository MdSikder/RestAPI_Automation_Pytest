import json
from json import JSONDecodeError

import pytest
import requests


@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com"


# @pytest.fixture
def test_Post_Token(base_url):
    body = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(f"{base_url}/auth", json=body)
    assert response.status_code == 200
    token_response = response.json()
    print("\n", json.dumps(token_response, indent=4))
    return token_response
    # created_response_id = created_response["id"]
    # to collect id for more use
    # print(created_response_id)


def test_get_all_booked_list(base_url):
    response = requests.get(f"{base_url}/booking/")
    assert response.status_code == 200
    data = response.json()
    # assert data["name"] == "Leanne Graham"
    # print("\n", data)
    # response print with prettify  mode
    print(json.dumps(data, indent=4))


def test_get_booked_list_byID(base_url):
    booking_id = 4403
    response = requests.get(f"{base_url}/booking/{booking_id}")
    assert response.status_code == 200
    data = response.json()
    # assert data["name"] == "Leanne Graham"
    # print("\n", data)
    # response print with prettify  mode
    print(json.dumps(data, indent=4))


def test_Post_booking(base_url):
    body = {

        "firstname": "limon",
        "lastname": "hasan",
        "totalprice": 4000,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2023-11-01",
            "checkout": "2023-11-03"
        },
        "additionalneeds": "Breakfast"

    }

    response = requests.post(f"{base_url}/booking/", json=body)
    assert response.status_code == 200
    created_response = response.json()
    # Validation with created response
    # assert created_response["first_name"] == "Md"
    # assert created_response["middle_name"] == "Rased"
    # assert created_response["last_name"] == "Sikder"
    # assert created_response["date_of_birth"] == "11/12/1988"
    print("\n", json.dumps(created_response, indent=4))
    # created_response_id = created_response["id"]
    # to collect id for more use
    # print(created_response_id)


def test_update_Student_details_byID(base_url):
    post_id_to_update = 1  # Specify the ID of the post to be updated
    student_id = 4403
    body = {

        "firstname": "Imran",
        "lastname": "Kabir",
        "totalprice": 15000,
        "depositpaid": "false",
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    headers = {
        "Content-Type": "application/json",  # Add the Content-Type header
        "Accept": "application/json",
        "Cookie": "token = 27696bd54466848"
    }

    response = requests.put(f"{base_url}/api/studentsDetails/{student_id}", json=body, headers=headers)
    if response.status_code == 200:
        # Request was successful
        print("PUT request was successful")
    else:
        # Handle errors
        print(f" \n PUT request failed with status code {response.status_code}")
        print(response.text)


def test_update_bookg(base_url):
    booking_id_to_update = 1077  # Specify the ID of the booking to be updated

    body = {
        "firstname": "Imran",
        "lastname": "Kabir",
        "totalprice": 15000,
        "depositpaid": "false",
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",  # Add the Content-Type header
        "Accept": "application/json",
        "Cookie": "token=27696bd54466848"
    }

    response = requests.put(f"{base_url}/api/studentsDetails/{booking_id_to_update}", json=body, headers=headers)

    try:
        updated_booking = response.json()
        print(json.dumps(updated_booking, indent=4))
    except JSONDecodeError:
        print("JSONDecodeError: Unable to decode response content as JSON.")
