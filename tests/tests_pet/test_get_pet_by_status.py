import pytest
import requests
import allure
from test_data.data import Data
from config.endpoints import PetEndpoints
from config.urls import Urls


class TestGetPetByStatus:

    url = f'{Urls.BASE_URL}{PetEndpoints.GET_PET_BY_STATUS_EP}'

    @allure.title('Successful receiving of pet data by status')
    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    def test_get_pet_by_status_success(self, status):
        query = {'status': status}
        with allure.step('Sending a request to receive pet data'):
            response = requests.get(self.url, params=query, headers=Data.headers_app_json)

        assert (response.status_code == 200
                and all(item['status'] == status for item in response.json()))
