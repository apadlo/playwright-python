from playwright.sync_api import Page


class ShopPage:
    """Page object for the shop page (https://rahulshettyacademy.com/angularpractice/shop)."""

    def __init__(self, page: Page):
        self.page = page

    def product_card(self, product_name: str):
        return self.page.locator(f'.card-body:has-text("{product_name}")').first

    def is_product_present(self, product_name: str) -> bool:
        try:
            return self.product_card(product_name).is_visible()
        except Exception:
            return False
