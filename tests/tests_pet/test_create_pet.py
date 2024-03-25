import requests
import json
import allure
from test_data.data import Data
from test_data.helpers import PetHelpData
from config.endpoints import PetEndpoints
from config.urls import Urls


class TestCreatePet:

    url = f'{Urls.BASE_URL}{PetEndpoints.CREATE_PET_EP}'
    phd = PetHelpData()

    @allure.title('Successful pet addition')
    def test_add_pet_success(self):
        payload = self.phd.generate_pet_data()
        with allure.step('Sending a request to add a pet'):
            response = requests.post(self.url, data=json.dumps(payload), headers=Data.headers_app_json)

        assert (response.status_code == 200 and response.json()['id'] == payload['id'])


    @allure.title('Failure to add a pet without required request body')
    def test_add_pet_without_request_body_failure(self):
        with allure.step('Sending a request to add a pet'):
            response = requests.post(self.url, headers=Data.headers_app_json)

        assert response.status_code == 405
