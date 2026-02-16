from unittest.mock import MagicMock

import pytest

from page_objects.chat_page import ChatPage
from page_objects.portfolio import PortfolioPage
from page_objects.smart_scrapper_page import SmartScrapperPage


@pytest.mark.unit
class TestStreamlitPageObjectsUnit:
    @pytest.mark.parametrize(
        ("page_object_cls", "url"),
        [
            (PortfolioPage, "https://apadlo.streamlit.app/"),
            (ChatPage, "https://bielik.streamlit.app/"),
            (SmartScrapperPage, "https://smart-scrapper.streamlit.app/"),
        ],
    )
    def test_navigate_uses_expected_url(self, page_object_cls, url):
        page = MagicMock()

        page_object_cls(page).navigate()

        page.goto.assert_called_once_with(url, wait_until="domcontentloaded")

    def test_portfolio_download_button_locator_chain(self):
        page = MagicMock()
        frame = MagicMock()
        button = MagicMock()
        page.frame_locator.return_value = frame
        frame.get_by_test_id.return_value = button

        found = PortfolioPage(page).download_button()

        page.frame_locator.assert_called_once_with('iframe[title="streamlitApp"]')
        frame.get_by_test_id.assert_called_once_with("stDownloadButton")
        assert found is button

    def test_chat_heading_anchor_locator_chain(self):
        page = MagicMock()
        frame = MagicMock()
        heading_anchor = MagicMock()
        page.frame_locator.return_value = frame
        frame.get_by_role.return_value = heading_anchor

        found = ChatPage(page).heading_anchor()

        frame.get_by_role.assert_called_once_with("link", name="Link to heading")
        assert found is heading_anchor

    def test_smart_scrapper_heading_link_locator_chain(self):
        page = MagicMock()
        frame = MagicMock()
        heading = MagicMock()
        heading_link = MagicMock()
        page.frame_locator.return_value = frame
        frame.get_by_test_id.return_value = heading
        heading.get_by_role.return_value = heading_link

        found = SmartScrapperPage(page).heading_link()

        frame.get_by_test_id.assert_called_once_with("stHeading")
        heading.get_by_role.assert_called_once_with("link", name="Link to heading")
        assert found is heading_link

    @pytest.mark.parametrize(
        ("module_name", "page_object_cls", "method_name", "locator_method"),
        [
            ("page_objects.portfolio", PortfolioPage, "verify_download_button", "download_button"),
            ("page_objects.chat_page", ChatPage, "verify_message_visible", "heading_anchor"),
            (
                "page_objects.smart_scrapper_page",
                SmartScrapperPage,
                "verify_heading_link_visible",
                "heading_link",
            ),
        ],
    )
    def test_verify_methods_call_expect_visible(self, monkeypatch, module_name, page_object_cls, method_name, locator_method):
        page = MagicMock()
        po = page_object_cls(page)

        locator = MagicMock()
        setattr(po, locator_method, MagicMock(return_value=locator))

        expect_mock = MagicMock()
        expectation = MagicMock()
        expect_mock.return_value = expectation

        module = __import__(module_name, fromlist=["expect"])
        monkeypatch.setattr(module, "expect", expect_mock)

        getattr(po, method_name)()

        expect_mock.assert_called_once_with(locator)
        expectation.to_be_visible.assert_called_once_with(timeout=10000)
