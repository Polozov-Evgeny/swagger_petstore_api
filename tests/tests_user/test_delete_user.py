import requests
import allure
from test_data.helpers import UserHelpData
from config.endpoints import UserEndpoints
from config.urls import Urls


class TestDeleteUser:
    url = f'{Urls.BASE_URL}{UserEndpoints.DELETE_USER_EP}'
    uhd = UserHelpData()

    @allure.title('Successfully deleting a user account')
    def test_delete_user_success(self):
        user_data = self.uhd.register_user_and_return_username_password()
        username = user_data.get('username')
        with allure.step('Sending a request to delete user account'):
            response = requests.delete(self.url.format(username=username))

        assert (response.status_code == 200 and response.json()['message'] == username)


    @allure.title('Unable to delete user account by non-existent username')
    def test_delete_user_by_non_existent_username_failure(self):
        user_data = self.uhd.register_user_and_return_username_password()
        username = user_data.get('username')
        self.uhd.delete_user_account(username)
        with allure.step('Sending a request to delete user account'):
            response = requests.delete(self.url.format(username=username))

        assert response.status_code == 404
