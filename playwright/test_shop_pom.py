import pytest
from playwright.sync_api import Playwright
from page_objects.login_practice import LoginPracticePage


class TestShopPOM:
    """End-to-end test using Page Object Model to verify a product exists in the shop."""

    USERNAME = "rahulshettyacademy"
    PASSWORD = "Learning@830$3mK2"
    TARGET_PRODUCT = "iPhone X"

    def test_product_present_after_login(self, playwright: Playwright, browser_instance):
        """1. Navigate to login page
        2. Enter credentials and sign in
        3. Wait for navigation to the shop page
        4. Verify target product is present
        """
        page = browser_instance

        # Arrange: open login page
        login_page = LoginPracticePage(page)
        login_page.navigate()

        # Act: perform login
        shop_page = login_page.login(self.USERNAME, self.PASSWORD)

        # Assert: wait until URL is the shop URL then check product
        page.wait_for_url("https://rahulshettyacademy.com/angularpractice/shop", timeout=10000)

        assert shop_page.is_product_present(self.TARGET_PRODUCT), \
            f"Expected product '{self.TARGET_PRODUCT}' to be visible on the shop page"
