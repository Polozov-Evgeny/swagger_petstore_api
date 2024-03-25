import requests
import json
import allure
from test_data.data import Data
from test_data.helpers import OrderHelpData
from config.endpoints import OrderEndpoints
from config.urls import Urls


class TestCreateOrder:

    url = f'{Urls.BASE_URL}{OrderEndpoints.CREATE_ORDER_EP}'
    ohd = OrderHelpData()

    @allure.title('Successful order creation')
    def test_create_order_success(self):
        payload = self.ohd.generate_order_data()
        with allure.step('Sending a request to create an order'):
            response = requests.post(self.url, data=json.dumps(payload), headers=Data.headers_app_json)

        assert (response.status_code == 200 and response.json()['id'] == payload['id'])