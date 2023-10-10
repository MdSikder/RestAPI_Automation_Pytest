import json

import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_create_new_post(base_url):
    body = {
        "userId": 1,
        "id": 101,
        "title": "New Post Title",
        "body": "This is the body of the new post."
    }
    response = requests.post(f"{base_url}/posts", json=body)
    assert response.status_code == 201
    created_response = response.json()
    assert created_response["title"] == "New Post Title"
    # print("\n", created_response, "\n")
    print(json.dumps(created_response, indent=4))
