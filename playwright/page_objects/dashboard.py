
from .orders import OrdersPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def select_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orders_page = OrdersPage(self.page)
        return orders_page