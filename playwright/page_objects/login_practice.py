from playwright.sync_api import Page
from .shop import ShopPage


class LoginPracticePage:
    """Page object for https://rahulshettyacademy.com/loginpagePractise/

    Provides navigation and login actions. Uses reliable locators (input[name=...], role)
    so the selectors are resilient to small DOM changes.
    """

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        """Open the login page."""
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username: str, password: str) -> ShopPage:
        """Fill credentials and click Sign In; returns a ShopPage instance.

        Note: the caller can wait for navigation or URL changes if desired. We keep
        this method focused on the action and returning the next page object.
        """
        # use name attributes for stable element selection
        self.page.locator('input[name="username"]').fill(username)
        self.page.locator('input[name="password"]').fill(password)
        # click button by role+name which is more accessible and resilient
        self.page.get_by_role("button", name="Sign In").click()
        return ShopPage(self.page)
