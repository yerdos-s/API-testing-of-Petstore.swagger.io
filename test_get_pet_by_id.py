import pytest
import requests
import json

json_file = 'create_pet.json'
with open(json_file, "r") as file:
    request_body = json.load(file)
    object_id = request_body['id']

class TestGetPetByID:

    def test_status_code_is_200(self):
        response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}', timeout=10)
        print(response.json())
        print(response.headers)
        assert response.status_code == 200, 'The status code is not 200'

    def test_content_type_in_response_headers(self):
        response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}', timeout=10)
        assert response.headers['Content-Type'] == response.headers['Content-Type'], \
            f"The content-type in response headers is not {response.headers['Content-Type']}"

    def test_id_in_response_body(self):
        response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}', timeout=10)
        response_body = response.json()
        assert response_body['id'] == object_id, 'The id in response body is wrong'

    def test_name_in_response_body(self):
        response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}', timeout=10)
        response_body = response.json()
        assert response_body['name'] == request_body['name'], 'The name in response body is wrong'

    def test_status_in_response_body(self):
        response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}', timeout=10)
        response_body = response.json()
        assert response_body['status'] == request_body['status'], \
            f"The status in response body is wrong, should be {request_body['status']}"
