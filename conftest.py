import pytest
from faker import Faker
fake = Faker("pl_PL")

@pytest.fixture(scope="session")
def get_name():
    return fake.name()


@pytest.fixture
def polish_user_factory():

    def _factory():
        return {
            "full_name": fake.name(),
            "email": fake.email(),
            "pesel": fake.pesel(),
            "phone": fake.phone_number(),
            "city": fake.city(),
        }

    return _factory

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser to use, default: chrome")

@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    match browser_name:
        case "chrome":
            browser = playwright.chromium.launch(headless=False)
        case "firefox":
            browser = playwright.firefox.launch(headless=False)
        case _:
            raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()