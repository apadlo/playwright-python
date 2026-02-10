import pytest
from faker import Faker
import random
import re

fake = Faker("pl_PL")
# fake.seed_instance(1234)


POLISH_EMAIL_DOMAINS = [
    "gmail.com",
    "wp.pl",
    "onet.pl",
    "interia.pl",
    "o2.pl"
]


def normalize(text: str) -> str:
    """Remove Polish diacritics and non-letter chars"""
    replacements = {
        "ą": "a", "ć": "c", "ę": "e", "ł": "l",
        "ń": "n", "ó": "o", "ś": "s", "ż": "z", "ź": "z"
    }
    text = text.lower()
    for k, v in replacements.items():
        text = text.replace(k, v)
    return re.sub(r"[^a-z]", "", text)

@pytest.fixture()
def polish_user_factory():

    def _factory():
        gender = random.choice(["male", "female"])

        if gender == "male":
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            pesel = fake.pesel(sex="M")
        else:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            pesel = fake.pesel(sex="F")

        domain = random.choice(POLISH_EMAIL_DOMAINS)
        email = f"{normalize(first_name)}.{normalize(last_name)}@{domain}"

        return {
            "full_name": f"{first_name} {last_name}",
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "email": email,
            "pesel": pesel,
            "phone": fake.phone_number(),
            "city": fake.city(),
        }

    return _factory

@pytest.fixture(scope="session")
def get_name():
    return fake.name()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser to use, default: chrome")

@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    match browser_name:
        case "chrome":
            browser = playwright.chromium.launch()
        case "firefox":
            browser = playwright.firefox.launch(headless=False)
        case _:
            raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()