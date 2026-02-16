import os

from .dashboard import DashboardPage


class LoginPage:
    URL = "https://rahulshettyacademy.com/client/"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def login(self, user_name):
        self.page.get_by_placeholder("email@example.com").fill(user_name)
        self.page.locator("#userPassword").fill(os.getenv("USER_PASSWORD"))
        self.page.get_by_role("button", name="Login").click()
        return DashboardPage(self.page)
