import pytest
import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.claim_page import ClaimPage
from utils.extract_json_data import get_random_event_type

@pytest.mark.depends(on=["valid_login"], scope="session")
@pytest.mark.regression
@pytest.mark.claim
def test_submit_claim(page,base_url,fullname,event_type,currency):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    claim_page = ClaimPage(page)
    
    home_page.click_claim()
    expect(page).to_have_url(f"{base_url}/web/index.php/claim/viewAssignClaim")
    claim_page.click_submit_claims()
    expect(page).to_have_url(f"{base_url}/web/index.php/claim/submitClaim")
    claim_page.submit_claim(fullname, event_type,currency)