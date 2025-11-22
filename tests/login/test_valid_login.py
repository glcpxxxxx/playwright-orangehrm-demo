import re, pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.login_page import LoginPage
from pages.home_page import HomePage
#from utils.extract_json_data import get_valid_json_data

@pytest.mark.order(2)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.claim
@pytest.mark.vacancy
@pytest.mark.leave
def test_valid_login(page: Page, env) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
     
    page.goto(f"{env["base_url"]}/web/index.php/auth/login")
    expect(login_page.login_button).to_be_visible()
    login_page.login(env["username"],env["password"])
    
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/dashboard/index")        
    expect(home_page.upgrade_button).to_be_visible()
    home_page.click_performance()
    home_page.click_dashboard()
