import json

import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_update_post_title(base_url):
    post_id_to_update = 1  # Specify the ID of the post to be updated
    body = {
        "title": "Updated Post Title Check"

    }
    response = requests.put(f"{base_url}/posts/{post_id_to_update}", json=body)
    assert response.status_code == 200
    updated_response = response.json()
    assert updated_response["title"] == "Updated Post Title Check"
    print(json.dumps(updated_response, indent=4))
