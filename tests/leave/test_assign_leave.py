import pytest
import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
#from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.leave_page import LeavePage
from utils.extract_json_data import get_random_employee, get_random_leave_type,get_random_partial_days,get_random_leave_duration


@pytest.mark.depends(on=["tests/login/test_valid_login.py::test_valid_login"], scope="session")
@pytest.mark.regression
@pytest.mark.leave
def test_assign_leave(page,env,fullname,leave_type,to_date,partial_days,duration):
    #login_page = LoginPage(page)
    home_page = HomePage(page)
    leave_page = LeavePage(page)
    
    page.goto(f"{env["base_url"]}/web/index.php/dashboard/index")
    home_page.click_leave()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/leave/viewLeaveList")
    leave_page.click_assign_leave()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/leave/assignLeave")
    leave_page.assign_leave(fullname,leave_type,to_date,partial_days,duration)
    