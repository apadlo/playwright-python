from playwright.sync_api import Page, expect

class ChatPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://bielik.streamlit.app/")

    def verify_message_visible(self):
        message_locator = self.page.locator("iframe[title=\"streamlitApp\"]").content_frame.get_by_role("link", name="Link to heading")
        expect(message_locator).to_be_visible(timeout=10000)