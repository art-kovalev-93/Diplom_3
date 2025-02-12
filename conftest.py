import pytest
from selenium import webdriver
import urls
from api.order_api import OrderApi
from api.user_api import UserApi
from receip_generator import Generator
from test_data import USER_DATA


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    user = UserApi()
    response = user.registration(body=USER_DATA)
    order = OrderApi()
    order.create_order(access_token=response.json().get('accessToken'), ingredients=Generator.get_receipt())
    yield response
    user.delete(access_token=response.json().get('accessToken'))