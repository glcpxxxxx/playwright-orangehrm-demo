import os
import pytest
import random
from playwright.sync_api import sync_playwright
from datetime import date, timedelta
from dotenv import load_dotenv
from utils.extract_json_data import get_random_employee, get_random_leave_type,get_random_partial_days,get_random_leave_duration
from utils.extract_json_data import get_random_event_type, get_random_currency
from utils.extract_json_data import get_random_job_title, get_random_hiring_manager

# Load .env only once
load_dotenv()

@pytest.fixture
def env():
    """Returns environment variables from .env as a dict."""
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
        "base_url": os.getenv("BASE_URL"),
    }

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # or True for CI
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def fullname():
    """Fixture that provides one random employee full name."""
    random_employee = get_random_employee()
    return random_employee["employee"]

@pytest.fixture(scope="session")
def leave_type():
    """Fixture that provides one random leave type."""
    random_leave = get_random_leave_type()
    return random_leave["type"]

@pytest.fixture(scope="session")
def partial_days():
    random_partial_day = get_random_partial_days()
    return random_partial_day["days"]

@pytest.fixture(scope="session")
def to_date():
    current_date = date.today()
    future_date = current_date + timedelta(days=1)
    return future_date.strftime("%Y-%d-%m")

@pytest.fixture(scope="session")
def duration():
    random_duration = get_random_leave_duration()
    return random_duration["days"]

@pytest.fixture(scope="session")
def event_type():
    random_event = get_random_event_type()
    return random_event["type"]

@pytest.fixture(scope="session")
def currency():
    random_currency = get_random_currency()
    return random_currency["currency"]

@pytest.fixture(scope="session")
def job_title():
    random_job_title = get_random_job_title()
    return random_job_title["job"]
    
@pytest.fixture(scope="session")
def hiring_manager():
    random_hiring_manager = get_random_hiring_manager()
    return random_hiring_manager["manager"]