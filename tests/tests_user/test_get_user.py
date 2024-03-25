import requests
import allure
from test_data.helpers import UserHelpData
from test_data.messages import Messages
from config.endpoints import UserEndpoints
from config.urls import Urls


class TestGetUser:

    url = f'{Urls.BASE_URL}{UserEndpoints.GET_USER_EP}'
    uhd = UserHelpData()

    @allure.title('Successful receiving of user data by username')
    def test_get_user_by_username_success(self, new_user):
        username = new_user.get('username')
        with allure.step('Sending a request to receive user data'):
            response = requests.get(self.url.format(username=username))

        assert (response.status_code == 200 and response.json()['username'] == username)


    @allure.title('Unable to retrieve user data by non-existent username')
    def test_get_user_by_non_existent_username_failure(self):
        user_data = self.uhd.register_user_and_return_username_password()
        username = user_data.get('username')
        self.uhd.delete_user_account(username)
        with allure.step('Sending a request to receive user data'):
            response = requests.get(self.url.format(username=username))

        assert (response.status_code == 404
                and response.json()['message'] == Messages.MESSAGE_USER_NOT_FOUND)
