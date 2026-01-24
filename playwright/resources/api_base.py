from playwright.sync_api import Playwright
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class APIUtils:


    BASE_URL = "https://rahulshettyacademy.com"

    def get_token(self, playwright: Playwright, user_name):
        endpoint = "api/ecom/auth/login"
        api_request_context = playwright.request.new_context(base_url=self.BASE_URL)
        payload = {"userEmail": user_name,"userPassword": os.getenv("USER_PASSWORD")}
        response = api_request_context.post(endpoint, data=payload)
        assert response.ok
        token = response.json().get("token")
        return token


    def create_order(self, playwright: Playwright, user_name, payload):
        endpoint = "/api/ecom/order/create-order"
        token = self.get_token(playwright, user_name)
        headers = {"Content-Type": "application/json", "Authorization": token}
        api_request_context = playwright.request.new_context(base_url=self.BASE_URL)
        response = api_request_context.post(endpoint, data=payload, headers=headers)
        print(response.json())
        return response.json()


    def get_order_details(self, playwright: Playwright):
        pass