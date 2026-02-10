from playwright.sync_api import Playwright
import resources.generic as gen
from page_objects.login import LoginPage
from page_objects.portfolio import PortfolioPage
from page_objects.chat_page import ChatPage
from page_objects.smart_scrapper_page import SmartScrapperPage
import os
from dotenv import load_dotenv

load_dotenv()

class TestPOM:
    user_name = os.getenv("TEST_EMAIL", "test@example.com")

    def test_create_order(self, playwright: Playwright, browser_instance):
        payload = {"orders": [
            {
                "country": "India",
                "productOrderedId": "6960eac0c941646b7a8b3e68"
            }
        ]
        }
        # create order using api call > get order_id
        response = gen.api_utils.create_order(playwright, self.user_name, payload)
        order_id = response.get('orders')[0]

        # login
        page = browser_instance
        login_page = LoginPage(page)
        login_page.navigate()
        dashboard_page = login_page.login(self.user_name)

        # in UI check if order_id is present in order history
        orders_page = dashboard_page.select_orders()
        order_details = orders_page.select_order(order_id)
        order_details.verify_order_message()


    def test_verify_streamlit_pages_online(self, browser_instance):
        page = browser_instance
        portfolio_page = PortfolioPage(page)
        chat_page = ChatPage(page)
        smart_scrapper_page = SmartScrapperPage(page)

        portfolio_page.navigate()
        portfolio_page.verify_download_button()

        chat_page.navigate()
        chat_page.verify_message_visible()

        smart_scrapper_page.navigate()
        smart_scrapper_page.verify_heading_link_visible()
