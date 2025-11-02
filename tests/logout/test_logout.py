import pytest
import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.depends(on=["valid_login"], scope="session")
@pytest.mark.smoke
@pytest.mark.last
def test_logout(page, base_url):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    home_page.click_logout()
    expect(login_page.login_heading).to_be_visible()
    expect(page).to_have_url(f"{base_url}/web/index.php/auth/login")
