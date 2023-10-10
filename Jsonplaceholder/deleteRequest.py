import json

import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_delete_post(base_url):
    post_id_to_delete = 1  # Specify the ID of the post to be deleted
    response = requests.delete(f"{base_url}/posts/{post_id_to_delete}")
    updated_response = response.json()
    print(json.dumps(updated_response, indent=4))
    assert response.status_code == 200
