from playwright.sync_api import expect

class OrderDetails:
    def __init__(self, page):
        self.page = page

    def verify_order_message(self):
        expect(self.page.locator("p.tagline")).to_contain_text("Thank you for Shopping With Us")