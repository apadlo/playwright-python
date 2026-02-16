from playwright.sync_api import Page, expect


class SmartScrapperPage:
    URL = "https://smart-scrapper.streamlit.app/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def app_frame(self):
        return self.page.frame_locator('iframe[title="streamlitApp"]')

    def heading_link(self):
        heading = self.app_frame().get_by_test_id("stHeading")
        return heading.get_by_role("link", name="Link to heading")

    def verify_heading_link_visible(self) -> None:
        expect(self.heading_link()).to_be_visible(timeout=10000)
