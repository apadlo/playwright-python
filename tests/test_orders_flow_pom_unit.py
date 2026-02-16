from unittest.mock import MagicMock

import pytest

from page_objects.dashboard import DashboardPage
from page_objects.order_details import OrderDetails
from page_objects.orders import OrdersPage


@pytest.mark.unit
class TestOrdersFlowPOMUnit:
    @pytest.mark.smoke
    def test_dashboard_select_orders_clicks_orders_button(self):
        page = MagicMock()
        orders_button = MagicMock()
        page.get_by_role.return_value = orders_button

        orders_page = DashboardPage(page).select_orders()

        page.get_by_role.assert_called_once_with("button", name="ORDERS")
        orders_button.click.assert_called_once()
        assert isinstance(orders_page, OrdersPage)

    @pytest.mark.parametrize("order_id", ["ORD-001", "ORD-ABC-999", "123456"])
    def test_orders_page_select_order_filters_row_and_clicks_view(self, order_id):
        page = MagicMock()
        table_rows = MagicMock()
        row = MagicMock()
        view_button = MagicMock()

        page.locator.return_value = table_rows
        table_rows.filter.return_value = row
        row.get_by_role.return_value = view_button

        order_details = OrdersPage(page).select_order(order_id)

        page.locator.assert_called_once_with("tr")
        table_rows.filter.assert_called_once_with(has_text=order_id)
        row.get_by_role.assert_called_once_with("button", name="View")
        view_button.click.assert_called_once()
        assert isinstance(order_details, OrderDetails)

    def test_orders_page_order_row_returns_filtered_locator(self):
        page = MagicMock()
        table_rows = MagicMock()
        filtered = MagicMock()
        page.locator.return_value = table_rows
        table_rows.filter.return_value = filtered

        result = OrdersPage(page).order_row("ORD-777")

        assert result is filtered

    def test_order_details_verify_order_message_uses_expected_text(self, monkeypatch):
        page = MagicMock()
        order_details = OrderDetails(page)

        expect_mock = MagicMock()
        expectation = MagicMock()
        expect_mock.return_value = expectation

        import page_objects.order_details as module

        monkeypatch.setattr(module, "expect", expect_mock)
        order_details.verify_order_message()

        page.locator.assert_called_once_with("p.tagline")
        expectation.to_contain_text.assert_called_once_with("Thank you for Shopping With Us")
