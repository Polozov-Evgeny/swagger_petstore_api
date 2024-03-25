import requests
import allure
from test_data.helpers import OrderHelpData
from config.endpoints import OrderEndpoints
from config.urls import Urls
from test_data.messages import Messages


class TestGetOrder:

    url = f'{Urls.BASE_URL}{OrderEndpoints.GET_ORDER_ER}'
    ohd = OrderHelpData()

    @allure.title('Successful receipt of order data')
    def test_get_order_success(self, new_order):
        orderId = new_order.get('id')
        with allure.step('Sending a request for order data'):
            response = requests.get(self.url.format(id=orderId))

        assert (response.status_code == 200 and response.json()['id'] == orderId)


    @allure.title('Unable to retrieve order data by non-existent id')
    def test_get_order_by_non_existent_id_failure(self):
        order_data = self.ohd.create_order()
        orderId = order_data.get('id')
        self.ohd.delete_order(orderId)
        with allure.step('Sending a request to receive order data'):
            response = requests.get(self.url.format(id=orderId))

        assert (response.status_code == 404
                and response.json()['message'] == Messages.MESSAGE_ORDER_NOT_FOUND)
