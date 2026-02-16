from unittest.mock import MagicMock

import pytest

from page_objects.login import LoginPage
from page_objects.login_practice import LoginPracticePage
from page_objects.shop import ShopPage


@pytest.mark.unit
class TestLoginAndShopPOMUnit:
    @pytest.mark.smoke
    @pytest.mark.parametrize("user_name", ["user@example.com", "qa@example.com"])
    def test_login_page_fills_email_and_submits(self, monkeypatch, user_name):
        page = MagicMock()
        email_input = MagicMock()
        password_input = MagicMock()
        login_button = MagicMock()

        page.get_by_placeholder.return_value = email_input
        page.locator.return_value = password_input
        page.get_by_role.return_value = login_button

        monkeypatch.setenv("USER_PASSWORD", "secret123")

        dashboard = LoginPage(page).login(user_name)

        email_input.fill.assert_called_once_with(user_name)
        password_input.fill.assert_called_once_with("secret123")
        login_button.click.assert_called_once()
        assert dashboard.page is page

    def test_login_page_navigate_uses_expected_url(self):
        page = MagicMock()
        login = LoginPage(page)

        login.navigate()

        page.goto.assert_called_once_with("https://rahulshettyacademy.com/client/", wait_until="domcontentloaded")

    @pytest.mark.parametrize(
        ("username", "password"),
        [
            ("rahulshettyacademy", "learning"),
            ("student", "pass123"),
        ],
    )
    def test_login_practice_fills_credentials_and_clicks_sign_in(self, username, password):
        page = MagicMock()
        username_input = MagicMock()
        password_input = MagicMock()
        sign_in_button = MagicMock()

        page.locator.side_effect = [username_input, password_input]
        page.get_by_role.return_value = sign_in_button

        shop_page = LoginPracticePage(page).login(username, password)

        username_input.fill.assert_called_once_with(username)
        password_input.fill.assert_called_once_with(password)
        sign_in_button.click.assert_called_once()
        assert isinstance(shop_page, ShopPage)

    def test_shop_page_returns_true_for_visible_product(self):
        page = MagicMock()
        card = MagicMock()
        card.is_visible.return_value = True
        page.locator.return_value.first = card

        assert ShopPage(page).is_product_present("iPhone X") is True
        page.locator.assert_called_once()

    def test_shop_page_returns_false_when_locator_raises(self):
        page = MagicMock()
        page.locator.side_effect = RuntimeError("temporary DOM failure")

        assert ShopPage(page).is_product_present("iPhone X") is False
