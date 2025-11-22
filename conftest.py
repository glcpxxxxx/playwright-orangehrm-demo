import os
import pytest
from datetime import date, timedelta
from dotenv import load_dotenv

# import your custom helper functions
from utils.extract_json_data import (
    get_random_employee,
    get_random_leave_type,
    get_random_partial_days,
    get_random_leave_duration,
    get_random_event_type,
    get_random_currency,
    get_random_job_title,
    get_random_hiring_manager
)

# load .env once
load_dotenv()

# -----------------------------
# ENV FIXTURE
# -----------------------------
@pytest.fixture
def env():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
        "base_url": os.getenv("BASE_URL"),
    }


# -----------------------------
# OVERRIDE CONTEXT (Reuse Browser, Keep Videos/Screenshots)
# -----------------------------
@pytest.fixture(scope="session")
def context(browser):
    """Reuse same browser for all tests while keeping auto screenshots/videos."""
    ctx = browser.new_context()
    yield ctx
    ctx.close()


# -----------------------------
# USE BUILT-IN PAGE FIXTURE
# (Do NOT override it — this enables screenshots on failure)
# -----------------------------
# Playwright creates a NEW page per test -> best practice
# Nothing to do here


# -----------------------------
# CUSTOM DATA FIXTURES (KEPT)
# -----------------------------
@pytest.fixture(scope="session")
def fullname():
    return get_random_employee()["employee"]

@pytest.fixture(scope="session")
def leave_type():
    return get_random_leave_type()["type"]

@pytest.fixture(scope="session")
def partial_days():
    return get_random_partial_days()["days"]

@pytest.fixture(scope="session")
def to_date():
    current_date = date.today()
    future_date = current_date + timedelta(days=1)
    return future_date.strftime("%Y-%d-%m")

@pytest.fixture(scope="session")
def duration():
    return get_random_leave_duration()["days"]

@pytest.fixture(scope="session")
def event_type():
    return get_random_event_type()["type"]

@pytest.fixture(scope="session")
def currency():
    return get_random_currency()["currency"]

@pytest.fixture(scope="session")
def job_title():
    return get_random_job_title()["job"]

@pytest.fixture(scope="session")
def hiring_manager():
    return get_random_hiring_manager()["manager"]
