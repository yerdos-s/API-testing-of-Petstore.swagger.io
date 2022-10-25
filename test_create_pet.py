import requests
import json
import pytest

json_file = 'create_pet.json'
with open(json_file, "r") as file:
    request_body = json.load(file)


@pytest.mark.order(1)
class TestCreatePet:

    def test_status_code_is_200(self):
        response = requests.post('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        assert response.status_code == 200, 'The status code is not 200'

    def test_name_in_response_body(self):
        response = requests.post('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['name'] == request_body['name'], \
            f'The object name is wrong, should be {request_body["name"]}'

    def test_category_name_in_response_body(self):
        response = requests.post('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['category']['name'] == request_body['category']['name'], \
            f"The category name is wrong, should be {request_body['category']['name']}"

    def test_status_in_response_body(self):
        response = requests.post('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['status'] == request_body['status'], \
            f"The status is wrong, should be {request_body['status']}"
