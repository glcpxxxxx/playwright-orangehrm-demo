import pytest
import re
from playwright.sync_api import Page, expect # Import Playwright's expect for assertions
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.recruitment_page import RecruitmentPage
from utils.extract_json_data import get_random_hiring_manager, get_random_job_title

@pytest.mark.depends(on=["tests/login/test_valid_login.py::test_valid_login"], scope="session")
@pytest.mark.regression
@pytest.mark.recruitment
def test_add_vacancy(page,env,job_title,hiring_manager):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    recruitment_page = RecruitmentPage(page)
    
    page.goto(f"{env["base_url"]}/web/index.php/dashboard/index")
    home_page.click_recruitment()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/recruitment/viewCandidates")
    recruitment_page.click_vacancies()
    expect(page).to_have_url(f"{env["base_url"]}/web/index.php/recruitment/viewJobVacancy")
    recruitment_page.add_vacancy(job_title,hiring_manager)
    recruitment_page.click_vacancies()
    recruitment_page.assert_created_vacancy(job_title)