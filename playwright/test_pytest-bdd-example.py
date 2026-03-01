import pytest
from pytest_bdd import given, when, then, parsers, scenarios
import resources.generic as gen
from page_objects.login import LoginPage


scenarios('features/order_transaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {user_name}'))
def place_item_order(playwright, user_name, shared_data):
    payload = {"orders": [
        {
            "country": "India",
            "productOrderedId": "6960eac0c941646b7a8b3e68"
        }
    ]
    }
    response = gen.api_utils.create_order(playwright, user_name, payload)
    order_id = response.get('orders')[0]
    shared_data['order_id'] = order_id

@given('the user is on landing page')
def user_on_landing_page(browser_instance, shared_data):
    page = browser_instance
    login_page = LoginPage(page)
    login_page.navigate()
    shared_data['login_page'] = login_page

@when(parsers.parse('I login to portal with {user_name}'))
def user_logged_in(user_name, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(user_name)
    shared_data['dashboard_page'] = dashboard_page

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    orders_page = dashboard_page.select_orders()
    shared_data['orders_page'] = orders_page

@when('select the order_id')
def select_order_id(shared_data):
    orders_page = shared_data['orders_page']
    order_id = shared_data['order_id']
    order_details = orders_page.select_order(order_id)
    shared_data['order_details'] = order_details

@then('order message is displayed')
def order_is_displayed(shared_data):
    order_details = shared_data['order_details']
    order_details.verify_order_message()

