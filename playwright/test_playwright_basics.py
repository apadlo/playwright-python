from playwright.sync_api import Page, Playwright, expect
import os
from dotenv import load_dotenv
import resources.generic as gen

# Load variables from .env file
load_dotenv()


class TestBasics:
    user_name = "andrzej@testowy.pl"

    @staticmethod
    def intercept_response(route):
        fake_response = {"data": [], "message": "No Orders"}
        route.fulfill(json=fake_response)

    @staticmethod
    def intercept_request(route):
        fake_url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69147e1f5008f6a9091a2b0f"
        route.continue_(url=fake_url)

    def test_basics(self, playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/")

    def test_shortcut(self, page: Page): # page is in default available in chromium headless with 1 context
        page.goto("https://rahulshettyacademy.com/")

    def test_locators_chrome(self, page: Page):
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("learning_wrongpw")
        page.get_by_role("combobox").select_option("teach")
        page.locator("#terms").check()
        page.get_by_role("button", name="Sign In").click()
        expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    def test_locators_firefox(self, playwright):
        browser = playwright.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("learning_wrongpw")
        page.get_by_role("combobox").select_option("teach")
        page.locator("#terms").check()
        page.get_by_role("button", name="Sign In").click()
        expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    def test_checkout(self, playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("Learning@830$3mK2")
        page.get_by_role("combobox").select_option("teach")
        page.locator("#terms").check()
        page.get_by_role("button", name="Sign In").click()
        checkout = page.locator(".nav-link.btn.btn-primary")
        expect(checkout).to_contain_text("0")
        iphone = page.locator("app-card").filter(has_text="iphone X")
        iphone.locator(".btn.btn-info").click()
        expect(checkout).to_contain_text("1")
        nokia = page.locator("app-card").filter(has_text="Nokia Edge")
        nokia.locator(".btn.btn-info").click()
        expect(checkout).to_contain_text("2")
        checkout.click()
        expect(page.locator(".media-body")).to_have_count(2)

    def test_multiple_pages(self, playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        with context.expect_page() as new_page_info:
            page.locator(".blinkingText").click()  # Opens a new tab
        new_page = new_page_info.value

        # Interact with the new page normally
        expect(new_page.locator(".red")).to_contain_text("mentor@rahulshettyacademy.com")
        text = new_page.locator(".red").text_content()
        print(text)

    def test_placeholder(self, page: Page):
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        placeholder = page.get_by_placeholder("Hide/Show Example")
        expect(placeholder).to_be_visible()
        page.locator("#hide-textbox").click()
        expect(placeholder).not_to_be_visible()
        page.locator("#show-textbox").click()
        expect(placeholder).to_be_visible()

    def test_alert(self, page: Page):
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        page.on("dialog", lambda dialog: dialog.accept())
        page.locator("#confirmbtn").click()

    def test_iframe(self, page: Page):
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        page_frame = page.frame_locator("#courses-iframe")
        page_frame.get_by_role("link", name="All Access plan").click()
        expect(page_frame.locator("body")).to_contain_text("Happy Subscibers!")

    def test_tables(self, page: Page):
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
        column_value = None
        for index in range(page.locator("th").count()):
             if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
                column_value = index
                print(f"Price column: {column_value}")
                break
        assert column_value is not None, "Price column not found"
        rice_row = page.locator("tr").filter(has_text="Rice")
        expect(rice_row.locator("td").nth(column_value)).to_contain_text("37")

    def test_mouse_hover(self, page: Page):
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        page.locator("#mousehover").hover()
        page.get_by_role("link", name="Top").click()

    def test_get_empty_orders(self, page: Page):
        page.goto("https://rahulshettyacademy.com/client/")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", self.intercept_response)
        page.get_by_placeholder("email@example.com").fill(self.user_name)
        page.locator("#userPassword").fill(os.getenv("USER_PASSWORD"))
        page.get_by_role("button", name="Login").click()

        # in UI check if order_id is present in order history
        page.get_by_role("button", name="ORDERS").click()
        expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time.")

    def test_get_orders_unauthorized(self, page: Page):
        page.goto("https://rahulshettyacademy.com/client/")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", self.intercept_request)

        page.get_by_placeholder("email@example.com").fill(self.user_name)
        page.locator("#userPassword").fill(os.getenv("USER_PASSWORD"))
        page.get_by_role("button", name="Login").click()

        # in UI check if order_id is present in order history
        page.get_by_role("button", name="ORDERS").click()
        page.get_by_role("button", name="View").first.click()
        expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")

    def test_skip_login_with_token(self, playwright: Playwright):
        get_token = gen.api_utils.get_token(playwright, self.user_name)

        # skip login with inject token
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.add_init_script(f"""localStorage.setItem('token', '{get_token}')""")
        page.goto("https://rahulshettyacademy.com/client/")
        page.get_by_role("button", name="ORDERS").click()
        expect(page.get_by_text("Your Orders")).to_be_visible()

        # ---------------------
        context.close()
        browser.close()

















