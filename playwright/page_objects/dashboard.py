from .orders import OrdersPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def orders_button(self):
        return self.page.get_by_role("button", name="ORDERS")

    def select_orders(self):
        self.orders_button().click()
        return OrdersPage(self.page)
