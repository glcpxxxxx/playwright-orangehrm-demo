import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.extract_json_data import get_invalid_json_data

@pytest.mark.order(1)
@pytest.mark.parametrize("username, password, expected", get_invalid_json_data())
def test_invalid_login(page: Page, username, password, expected, env) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto(f"{env["base_url"]}/web/index.php/auth/login")
    expect(login_page.login_button).to_be_visible()
    login_page.login(username, password)

    if expected == "invalid":
        expect(login_page.invalid_credential).to_be_visible(timeout=5000)
        expect(page).to_have_url(f"{env["base_url"]}/web/index.php/auth/login")
