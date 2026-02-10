from playwright.sync_api import Page, expect

class SmartScrapperPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://smart-scrapper.streamlit.app/")

    def verify_heading_link_visible(self):
        page_title = self.page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_test_id("stHeading").get_by_role("link", name="Link to heading")
        expect(page_title).to_be_visible(timeout=10000)