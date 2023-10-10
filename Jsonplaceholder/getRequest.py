import json

import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_user_data(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Leanne Graham"
    # print("\n", data)
    # response print with prettify  mode
    print(json.dumps(data, indent=4))


def test_get_post_data(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["userId"] == 1
    # print("\n", data)
    # response print with prettify  mode
    print(json.dumps(data, indent=4))
