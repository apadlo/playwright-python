import os
from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, user_name):
        self.page.get_by_placeholder("email@example.com").fill(user_name)
        password = os.getenv("USER_PASSWORD", "Password@1")
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page