import pytest
from test_data.helpers import *


@pytest.fixture(scope='function')
def new_user():
    uhd = UserHelpData()
    new_user = uhd.register_user_and_return_username_password()
    yield new_user
    uhd.delete_user_account(new_user.get('username'))


@pytest.fixture(scope='function')
def new_pet():
    phd = PetHelpData()
    new_pet = phd.add_pet_data()
    yield new_pet
    phd.delete_pet_data(new_pet.get('id'))


@pytest.fixture(scope='function')
def new_order():
    ohd = OrderHelpData()
    new_order = ohd.create_order()
    yield new_order
    ohd.delete_order(new_order.get('id'))
