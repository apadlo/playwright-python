import pytest

from page_objects.chat_page import ChatPage
from page_objects.portfolio import PortfolioPage
from page_objects.smart_scrapper_page import SmartScrapperPage


@pytest.mark.e2e
@pytest.mark.streamlit
class TestStreamlitPageObjectsE2E:
    @pytest.mark.smoke
    def test_portfolio_download_button_visible(self, browser_instance):
        portfolio_page = PortfolioPage(browser_instance)
        portfolio_page.navigate()
        portfolio_page.verify_download_button()

    def test_chat_heading_anchor_visible(self, browser_instance):
        chat_page = ChatPage(browser_instance)
        chat_page.navigate()
        chat_page.verify_message_visible()

    def test_smart_scrapper_heading_visible(self, browser_instance):
        smart_scrapper_page = SmartScrapperPage(browser_instance)
        smart_scrapper_page.navigate()
        smart_scrapper_page.verify_heading_link_visible()
