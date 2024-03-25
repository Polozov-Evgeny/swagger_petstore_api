import requests
import allure
from test_data.messages import Messages
from test_data.helpers import OrderHelpData
from config.endpoints import OrderEndpoints
from config.urls import Urls



class TestDeleteOrder:
    url = f'{Urls.BASE_URL}{OrderEndpoints.DELETE_ORDER_EP}'
    ohd = OrderHelpData()

    @allure.title('Successful order deletion')
    def test_delete_order_success(self):
        order_data = self.ohd.create_order()
        orderId = order_data.get('id')
        with allure.step('Sending a request to delete an order'):
            response = requests.delete(self.url.format(id=orderId))

        assert (response.status_code == 200 and response.json()['message'] == str(orderId))


    @allure.title('Unable to delete an order by non-existent id')
    def test_delete_order_by_non_existent_id_failure(self):
        order_data = self.ohd.create_order()
        orderId = order_data.get('id')
        self.ohd.delete_order(orderId)
        with allure.step('Sending a request to delete an order'):
            response = requests.delete(self.url.format(id=orderId))

        assert (response.status_code == 404
                and response.json()['message'] == Messages.MESSAGE_ORDER_NOT_FOUND.title())
