import requests
import json
import pytest

json_file = 'update_pet.json'
with open(json_file, 'r') as file:
    request_body = json.load(file)


@pytest.mark.order(3)
class TestUpdatePet:

    def test_status_code_is_200(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        assert response.status_code == 200, 'The status code is not 200'

    def test_content_type_in_response_headers(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        assert response.headers['Content-Type'] == response.headers['Content-Type'], \
            f"The content-type in response headers is not {response.headers['Content-Type']}"

    def test_id_in_response_body(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['id'] == request_body['id'], 'The response id is wrong'

    def test_name_in_response_body(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['category']['name'] == request_body['category']['name'], \
            "The name in response body is wrong"

    def test_photo_url_in_response_body(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body["photoUrls"] == request_body["photoUrls"], \
            'The photo url is wrong in response body'

    def test_status_in_response_body(self):
        response = requests.put('https://petstore.swagger.io/v2/pet', json=request_body, timeout=10)
        response_body = response.json()
        assert response_body['status'] == request_body['status'], \
            'The status in response body is wrong'
