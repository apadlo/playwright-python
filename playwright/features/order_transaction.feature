Feature: Order Transaction
  Tests related to Order Transactions

  Scenario Outline: Verify Order success message shown in details page
    Given place the item order with <user_name>
    And the user is on landing page
    When I login to portal with <user_name>
    And navigate to orders page
    And select the order_id
    Then order message is displayed
    Examples:
      | user_name            |
      | test@example.com     |
