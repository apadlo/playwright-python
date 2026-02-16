from .order_details import OrderDetails


class OrdersPage:
    def __init__(self, page):
        self.page = page

    def order_row(self, order_id):
        return self.page.locator("tr").filter(has_text=order_id)

    def select_order(self, order_id):
        self.order_row(order_id).get_by_role("button", name="View").click()
        return OrderDetails(self.page)
