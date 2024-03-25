import requests
import allure
from test_data.helpers import PetHelpData
from config.endpoints import PetEndpoints
from config.urls import Urls
from test_data.messages import Messages


class TestGetPetById:

    url = f'{Urls.BASE_URL}{PetEndpoints.GET_PET_BY_ID_EP}'
    phd = PetHelpData()

    @allure.title('Successful receiving of pet data by petId')
    def test_get_pet_by_petId_success(self, new_pet):
        petId = new_pet.get('id')
        with allure.step('Sending a request to receive pet data'):
            response = requests.get(self.url.format(petId=petId))

        assert (response.status_code == 200 and response.json()['id'] == petId)


    @allure.title('Unable to retrieve pet data by non-existent petId')
    def test_get_pet_by_non_existent_petId_failure(self):
        pet_data = self.phd.add_pet_data()
        petId = pet_data.get('id')
        self.phd.delete_pet_data(petId)
        with allure.step('Sending a request to receive pet data'):
            response = requests.get(self.url.format(petId=petId))

        assert (response.status_code == 404
                and response.json()['message'] == Messages.MESSAGE_PET_NOT_FOUND)
