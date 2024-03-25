import requests
import json
import allure
from test_data.data import Data
from test_data.helpers import UserHelpData
from config.endpoints import UserEndpoints
from config.urls import Urls


class TestCreateUser:

    url = f'{Urls.BASE_URL}{UserEndpoints.CREATE_USER_EP}'
    uhd = UserHelpData()

    @allure.title('Successful user registration')
    def test_create_user_success(self):
        payload = self.uhd.generate_user_data_for_registration()
        with allure.step('Sending a request for user registration'):
            response = requests.post(self.url, data=json.dumps(payload), headers=Data.headers_app_json)

        assert (response.status_code == 200 and response.json()['message'] == str(payload['id']))


    @allure.title('Failure to create a user without required header "content-type"')
    def test_create_user_without_header_content_type_failure(self):
        payload = self.uhd.generate_user_data_for_registration()
        headers = {'accept': 'application/json'}
        with allure.step('Sending a request for user registration'):
            response = requests.post(self.url, data=json.dumps(payload), headers=headers)

        assert response.status_code == 415
