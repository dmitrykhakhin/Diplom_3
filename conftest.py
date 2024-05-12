import pytest
from selenium import webdriver

from data import Url, Burger
from helper import Helper, User, Order


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Url.URL)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = Helper.generate_registration_data()
    registration_response = User.register_new_user_and_return_response(user)
    user["token"] = registration_response.json()['accessToken']
    yield user
    User.delete_user(user["token"], user["email"])


@pytest.fixture
def order(user):
    order = Order.create_order_with_auth_and_return_response(
        user["token"],
        Burger.SPACE_METEORITE_FLUORESCENT_BURGER["ingredients_list"]
    )
    yield order
