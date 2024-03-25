import requests
import json
import allure
from test_data.data import Data
from test_data.helpers import UserHelpData
from config.endpoints import UserEndpoints
from config.urls import Urls


class TestUpdateUser:

    url = f'{Urls.BASE_URL}{UserEndpoints.UPDATE_USER_EP}'
    uhd = UserHelpData()

    @allure.title('Successful user update')
    def test_update_user_success(self, new_user):
        username = new_user.get('username')
        updated_data = self.uhd.generate_user_data_for_registration()
        with allure.step('Sending a request for user update'):
            response = requests.put(
                self.url.format(username=username), data=json.dumps(updated_data), headers=Data.headers_app_json)

        assert (response.status_code == 200 and response.json()['message'] == str(updated_data['id']))
