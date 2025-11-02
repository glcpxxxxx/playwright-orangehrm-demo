import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest
from utils.extract_json_data import get_valid_json_data


@pytest.mark.parametrize("username, password, expected", get_valid_json_data())
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.claim
@pytest.mark.vacancy
def test_valid_login(page: Page, username,password, expected, base_url) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
 
    
    page.goto(f"{base_url}/web/index.php/auth/login")
    expect(login_page.login_button).to_be_visible()
    login_page.login(username,password)
    if expected == "success":
        expect(page).to_have_url(f"{base_url}/web/index.php/dashboard/index")
        
        expect(home_page.upgrade_button).to_be_visible()
        home_page.click_performance()
        home_page.click_dashboard()
    
    elif expected == "invalid":
        pytest.skip("invalid user; skipping dependency check")
    