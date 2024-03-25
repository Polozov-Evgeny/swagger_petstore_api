import pytest
import requests
import allure
from test_data.data import Data
from test_data.helpers import PetHelpData
from config.endpoints import PetEndpoints
from config.urls import Urls


class TestUpdatePet:

    url = f'{Urls.BASE_URL}{PetEndpoints.UPDATE_PET_BY_ID_EP}'
    phd = PetHelpData()


    @allure.title('Successful pet update by petId')
    @pytest.mark.parametrize('key, value',
                             [
                                 ['name', 'testName'],
                                 ['status', 'testSold']
                             ])
    def test_update_pet_by_petId_success(self, new_pet, key, value):
        petId = new_pet.get('id')
        payload = {key: value}
        with allure.step('Sending a request for pet update'):
            response = requests.post(
                self.url.format(petId=petId), data=payload, headers=Data.headers_app_x_www_form)

        assert (response.status_code == 200 and response.json()['message'] == str(petId))

        # additional field verification
        with allure.step('Sending a request to receive pet data'):
            response = requests.get(self.url.format(petId=petId))

        assert (response.json()[key] == value)
