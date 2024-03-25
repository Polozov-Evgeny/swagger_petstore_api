import requests
import allure
from test_data.helpers import PetHelpData
from config.endpoints import PetEndpoints
from config.urls import Urls


class TestDeletePet:
    url = f'{Urls.BASE_URL}{PetEndpoints.DELETE_PET_EP}'
    phd = PetHelpData()

    @allure.title('Successful pet deleting')
    def test_delete_pet_success(self):
        pet_data = self.phd.add_pet_data()
        petId = pet_data.get('id')
        with allure.step('Sending a request to delete a pet'):
            response = requests.delete(self.url.format(petId=petId))

        assert (response.status_code == 200 and response.json()['message'] == str(petId))


    @allure.title('Unable to delete a pet by non-existent petId')
    def test_delete_pet_by_non_existent_petId_failure(self):
        pet_data = self.phd.add_pet_data()
        petId = pet_data.get('id')
        self.phd.delete_pet_data(petId)
        with allure.step('Sending a request to delete a pet'):
            response = requests.delete(self.url.format(petId=petId))

        assert response.status_code == 404
