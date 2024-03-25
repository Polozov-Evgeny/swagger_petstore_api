import requests
import json
import random
import allure
from faker import Faker
from test_data.data import Data
from config.urls import Urls
from config.endpoints import *


class UserHelpData:
    @allure.step('Generating data for user registration')
    def generate_user_data_for_registration(self):
        fake = Faker()
        user_data = {
            'id': random.randint(1, 1000000),
            'username': fake.user_name(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'phone': fake.phone_number(),
            'userStatus': random.randint(0, 3)
        }
        return user_data

    @allure.step('User registration and return of authorization data')
    def register_user_and_return_username_password(self):
        url = f'{Urls.BASE_URL}{UserEndpoints.CREATE_USER_EP}'
        registration_data = self.generate_user_data_for_registration()
        response = requests.post(url, data=json.dumps(registration_data), headers=Data.headers_app_json)
        if response.status_code == 200:
            login_data = {
                'username': registration_data['username'],
                'password': registration_data['password']
            }
            return login_data
        else:
            print('Problem: "User account" is not registered')

    @allure.step('Deleting test user account')
    def delete_user_account(self, username):
        url = f'{Urls.BASE_URL}{UserEndpoints.DELETE_USER_EP.format(username=username)}'
        response = requests.delete(url)
        if response.status_code != 200:
            print('Problem: "User account" was not deleted')


class PetHelpData:
    @allure.step('Generating pet data')
    def generate_pet_data(self):
        fake = Faker()
        pet_data = {
            'id': random.randint(1, 1000000),
            'category': {
                'id': random.randint(1, 10),
                'name': fake.word()
            },
            'name': fake.name(),
            'photoUrls': [fake.image_url()],
            'tags': [
                {
                    "id": random.randint(1, 10),
                    "name": fake.word()
                }
            ],
            'status': random.choice(["available", "pending", "sold"])
        }
        return pet_data

    @allure.step('Adding a pet for the test')
    def add_pet_data(self):
        url = f'{Urls.BASE_URL}{PetEndpoints.CREATE_PET_EP}'
        payload = self.generate_pet_data()
        response = requests.post(url, data=json.dumps(payload), headers=Data.headers_app_json)
        if response.status_code == 200:
            pet_data = response.json()
            return pet_data
        else:
            print('Problem: Pet for the test is not added')

    @allure.step('Deleting test pet data')
    def delete_pet_data(self, petId):
        url = f'{Urls.BASE_URL}{PetEndpoints.DELETE_PET_EP.format(petId=petId)}'
        response = requests.delete(url)
        if response.status_code != 200:
            print('Problem: Pet for the test was not deleted')


class OrderHelpData:
    @allure.step('Generating order data')
    def generate_order_data(self):
        fake = Faker()
        order_data = {
            'id': random.randint(1, 1000000),
            'petId': random.randint(1, 1000000),
            'quantity': random.randint(1, 5),
            'shipDate': fake.date_time_this_year().isoformat()+'Z',
            'status': random.choice(["placed", "approved", "delivered"]),
            'complete': fake.boolean()
        }
        return order_data

    @allure.step('Create a test order')
    def create_order(self):
        url = f'{Urls.BASE_URL}{OrderEndpoints.CREATE_ORDER_EP}'
        payload = self.generate_order_data()
        response = requests.post(url, data=json.dumps(payload), headers=Data.headers_app_json)
        if response.status_code == 200:
            order_data = response.json()
            return order_data
        else:
            print('Problem: Test order is not created')

    @allure.step('Deleting test order')
    def delete_order(self, orderId):
        url = f'{Urls.BASE_URL}{OrderEndpoints.DELETE_ORDER_EP.format(id=orderId)}'
        response = requests.delete(url)
        if response.status_code != 200:
            print('Problem: Test order was not deleted')
