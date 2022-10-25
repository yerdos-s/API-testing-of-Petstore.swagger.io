import json
import requests
import pytest

json_file = 'create_pet.json'
with open (json_file,'r') as file:
    data = json.load(file)
    object_id = data['id']

@pytest.fixture()
def api_response():
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{object_id}')
    return response

def test_object_is_deleted_successfully(api_response):
    response_body = api_response.json()
    assert api_response.status_code == 200, 'Status code is not 200'
    assert response_body['type'] == 'unknown', 'The response body type is not unknown'
    assert response_body['message'] == str(object_id), f"The message should be {object_id} ID"
