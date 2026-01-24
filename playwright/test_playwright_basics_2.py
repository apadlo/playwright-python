# python
from playwright.sync_api import Playwright, expect
from dotenv import load_dotenv
import os
import resources.generic as gen
from page_objects.login import LoginPage

load_dotenv()


class TestBasicsPOM:
    user_name = "andrzej@testowy.pl"

    @staticmethod
    def intercept_response(route):
        fake_response = {"data": [], "message": "No Orders"}
        route.fulfill(json=fake_response)

    @staticmethod
    def intercept_request(route):
        fake_url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69147e1f5008f6a9091a2b0f"
        route.continue_(url=fake_url)

    def test_get_empty_orders(self, browser_instance):
        page = browser_instance
        # use POM to navigate & login
        login_page = LoginPage(page)
        login_page.navigate()
        dashboard = login_page.login(self.user_name)

        # force empty orders response and verify UI message
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", self.intercept_response)
        dashboard.select_orders()
        expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time.")

    def test_get_orders_unauthorized(self, browser_instance):
        page = browser_instance
        # use POM to navigate & login
        login_page = LoginPage(page)
        login_page.navigate()
        dashboard = login_page.login(self.user_name)

        # intercept details request to a specific unauthorized id and verify error shown in UI
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", self.intercept_request)
        orders_page = dashboard.select_orders()
        page.get_by_role("button", name="View").first.click()
        expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")

    def test_skip_login_with_token(self, playwright: Playwright):
        # obtain token via API utils and inject into localStorage, then verify orders page opens
        token = gen.api_utils.get_token(playwright, self.user_name)

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
        page.goto("https://rahulshettyacademy.com/client/")
        page.get_by_role("button", name="ORDERS").click()
        expect(page.get_by_text("Your Orders")).to_be_visible()

        context.close()
        browser.close()

    def test_create_order_and_verify_in_ui(self, playwright: Playwright, browser_instance):
        # create an order via API, then login via POM and verify order is visible in orders list
        payload = {"orders": [
            {
                "country": "India",
                "productOrderedId": "6960eac0c941646b7a8b3e68"
            }
        ]}
        response = gen.api_utils.create_order(playwright, self.user_name, payload)
        order_id = response.get("orders")[0]

        page = browser_instance
        login_page = LoginPage(page)
        login_page.navigate()
        dashboard = login_page.login(self.user_name)

        orders_page = dashboard.select_orders()
        order_details = orders_page.select_order(order_id)
        order_details.verify_order_message()
