import re
from playwright.sync_api import expect

class ClaimPage:
    def __init__(self, page):
        # page links
        self.page = page
        self.configuration_dropdown = page.get_by_role("listitem").filter(has_text="Configuration")
        self.submit_claims = page.get_by_role("listitem").filter(has_text="Submit Claim")
        self.my_claims = page.get_by_role("listitem").filter(has_text="My Claims")
        self.employee_claims = page.get_by_role("listitem").filter(has_text="Employee Claims")
        self.assign_claim = page.get_by_role("listitem").filter(has_text="Assign Claim")
        # global fields
        self.employee_name = page.get_by_role("textbox", name="Type for hints...")
        # submit claim fields
        self.event = page.locator(".oxd-select-text").first
        self.currency = page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text")
        self.remarks = page.locator("textarea")
        self.create_button =  page.get_by_role("button", name="Create")
        self.success_modal = page.get_by_text("SuccessSuccessfully Saved×")
    
    # methods to navigate to pages in Claims page  
    def click_configuration_dropdown(self):
        self.configuration_dropdown.click()
        
    def click_submit_claims(self):
        self.submit_claims.click()
        
    def click_my_claims(self):
        self.my_claims.click()
        
    def click_employee_claims(self):
        self.employee_claims.click()
        
    def click_assign_claim(self):
        self.assign_claim.click()
        
    # methods to the different functions in Claims page
    def submit_claim(self,fullname,event_type,currency):
        self.event.click()
        self.page.get_by_role("option", name=event_type).click()
        self.currency.click()
        self.page.get_by_role("option", name=currency).click()
        self.remarks.fill("Submit Claim Remarks")
        self.create_button.click()
        expect(self.success_modal).to_be_visible()
        