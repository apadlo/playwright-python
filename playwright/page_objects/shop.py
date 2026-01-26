from playwright.sync_api import Page


class ShopPage:
    """Page object for the shop page (https://rahulshettyacademy.com/angularpractice/shop)

    Exposes methods to query the product list and check for product presence.
    """

    def __init__(self, page: Page):
        self.page = page

    def is_product_present(self, product_name: str) -> bool:
        """Return True if a product with the given name is present on the page.

        This uses a product card selector that matches typical Rahul Shetty academy
        demo markup: product names are inside .card or .card-title elements. We search
        by visible text which is resilient to small DOM changes.
        """
        # Wait for product listings to load (timeout default) then search
        try:
            # Use :has-text() which is robust and checks visible text within the card body
            product_locator = self.page.locator(f".card-body:has-text(\"{product_name}\")")
            return product_locator.first.is_visible()
        except Exception:
            return False
