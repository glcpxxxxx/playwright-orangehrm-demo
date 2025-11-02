import re
import random
from playwright.sync_api import expect

class RecruitmentPage():
    def __init__(self,page):
        # pages under recruitment
        self.page = page
        self.candidates_tab = page.get_by_role("listitem").filter(has_text="Candidates")
        self.vacancies_tab = page.get_by_role("listitem").filter(has_text="Vacancies")
        
        # fields under add vacancy
        self.add_vancancy_button = page.get_by_role("button", name=" Add")
        self.vancancy_name = page.locator("div").filter(has_text=re.compile(r"^Vacancy NameJob Title-- Select --$")).get_by_role("textbox")
        self.job_title_dropdown = page.locator("div").filter(has_text=re.compile(r"^-- Select --$")).nth(2)
        self.description = page.get_by_role("textbox", name="Type description here")
        self.hiring_manager_field = page.get_by_role("textbox", name="Type for hints...")
        self.number_of_positions = page.get_by_role("textbox").nth(4)
        self.save_button = page.get_by_role("button", name="Save")
        self.success_modal = page.get_by_text("SuccessSuccessfully Saved×")
        
        #fields under recruitment/vacancies
        self.delete_selected_button = page.get_by_role("button", name=" Delete Selected")
        self.delete_confirmation_modal =  page.get_by_text("×Are you Sure?The selected")
        self.modal_yes_delete_button = page.get_by_role("button", name=" Yes, Delete")
        self.delete_success_modal = page.get_by_text("SuccessSuccessfully Deleted×")
        self.last_added_vacancy = None
        self.job_title_search_dropwdown = page.locator(".oxd-select-text").first
        self.vacancy_search_dropdown = page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text")
        self.search_button = page.get_by_role("button", name="Search")
        self.no_records_found_toast = page.locator("#oxd-toaster_1").get_by_text("No Records Found")
        
    # methods to navigate in recruitment page   
    def click_candidates(self):
        self.candidates_tab.click()
        
    def click_vacancies(self):
        self.vacancies_tab.click()
        
    # methods to add a vacancy
    def add_vacancy(self,job_title,hiring_manager):
        self.add_vancancy_button.click()
        self.vancancy_name.fill(job_title)
        self.job_title_dropdown.click()
        self.job_title = self.page.get_by_role("option", name=job_title)
        self.job_title.click()
        self.description.fill("Test Vacancy description.")
        self.hiring_manager_field.fill(hiring_manager)
        self.hiring_manager_dropdown_option = self.page.get_by_role("option", name=hiring_manager)
        self.hiring_manager_dropdown_option.click()
        self.number_of_positions.fill("1")
        self.save_button.click()
        self.last_added_vacancy = job_title
        return job_title
    
    def assert_created_vacancy(self,job_title=None):
        job_title = job_title or self.last_added_vacancy
        vacancy = job_title or self.last_added_vacancy
        self.job_title_search_dropwdown.click()
        self.page.get_by_text(job_title).click()
        self.vacancy_search_dropdown.click()
        self.page.get_by_text(vacancy).click()
        self.search_button.click()
        #first_row = self.page.get_by_role("row", name=f" {job_title}").first
        #expect(first_row).to_be_visible()
        
    def delete_vacancy(self,job_title=None):
        job_title = job_title or self.last_added_vacancy
        self.job_title_search_dropwdown.click()
        self.page.get_by_text(job_title).click()
        self.vacancy_search_dropdown.click()
        self.page.get_by_role("option", name=f"{job_title}")
        self.search_button.click()
        result = self.page.get_by_role("row", name=f" {job_title}").first
        expect(result).to_be_visible()
        checkbox = self.page.get_by_role("cell", name="").locator("i")
        checkbox.click()
        self.delete_selected_button.click()
        expect(self.delete_confirmation_modal)
        self.modal_yes_delete_button.click()
        expect(self.delete_success_modal)
        
    def assert_deleted_vacancy(self,job_title=None):
        job_title = job_title or self.last_added_vacancy
        self.job_title_search_dropwdown.click()
        self.page.get_by_text(job_title).click()
        self.vacancy_search_dropdown.click()
        self.page.get_by_role("option", name=f"{job_title}").first
        self.search_button.click()        
        expect(self.no_records_found_toast).to_be_visible()
        