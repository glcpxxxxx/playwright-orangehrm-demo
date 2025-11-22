import pytest
import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.home_page import HomePage
from pages.leave_page import LeavePage
from utils.extract_json_data import get_random_employee

@pytest.mark.depends(on=["tests/login/test_valid_login.py::test_valid_login"], scope="session")
@pytest.mark.regression
@pytest.mark.leave
def test_apply_leave(page,env,fullname):
    home_page = HomePage(page)
    leave_page = LeavePage(page)
    
    page.goto(f"{env["base_url"]}/web/index.php/dashboard/index")
    home_page.click_leave()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/leave/viewLeaveList")
    leave_page.click_apply_leave()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/leave/applyLeave")
    if leave_page.assert_no_leave_balance() == False:  
        leave_page.apply_leave(leave_page.assign_leave)
    else: 
        pytest.skip("Employee doesn't have enough leave credits")