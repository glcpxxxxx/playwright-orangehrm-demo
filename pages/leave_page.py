import re
from datetime import date
from playwright.sync_api import expect

class LeavePage:
    def __init__(self,page):
        self.page = page
        self.apply_link = page.get_by_role("link", name="Apply")
        self.my_leave_link = page.get_by_role("link", name="My Leave")
        self.entitlements_dropdown = page.get_by_role("listitem").filter(has_text="Entitlements")
        self.add_entitlement = page.get_by_role("menuitem", name="Add Entitlements")
        self.assign_leave_link = page.get_by_role("link", name="Assign Leave")
        #fields under assign leave
        self.employee_name_field = page.get_by_role("textbox", name="Type for hints...")
        self.leave_type_dropdown =  page.locator("form i").first
        self.from_date = page.get_by_role("textbox", name="yyyy-dd-mm").first.first
        self.to_date = page.get_by_role("textbox", name="yyyy-dd-mm").nth(1)
        self.comment = page.locator("textarea")
        self.assign_button = page.get_by_role("button", name="Assign")
        self.partial = page.locator("form i").nth(4)
        self.duration = page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon")
        self.success_message = page.get_by_text("Successfully Saved")
        self.confirm_leave_modal = page.get_by_text("Confirm Leave Assignment", exact=True)
        self.confirm_ok_button = page.get_by_role("button", name="Ok")
        
    # methods to navigate to pages in Leaves page
    def click_assign_leave(self):
        self.assign_leave_link.click()

        
    # methods to the different functions in Leaves page       
    def assign_leave(self,fullname,leavetype,to_date,partial_days,duration):
        self.employee_name_field.fill(fullname)
        self.employee_name_field.press("Enter")
        employee_dropdown_option = self.page.get_by_role("option", name=fullname).first
        employee_dropdown_option.click()
        self.leave_type_dropdown.click()
        leavetype = self.page.get_by_role("option", name=leavetype)
        leavetype.click()
        today = date.today().strftime("%Y-%d-%m")
        self.from_date.fill(today)
        self.to_date.click()
        self.to_date.fill(to_date)
        self.from_date.click()
        self.comment.click()
        self.comment.fill("Test Comment")
        self.partial.click()
        self.page.get_by_role("option", name=partial_days).click()
        self.duration.click()
        self.page.get_by_role("option", name=duration).click()
        self.assign_button.click()
        expect(self.confirm_leave_modal).to_be_visible
        self.confirm_ok_button.click()
        expect(self.success_message).to_be_visible()
        
        
        
        
        
        
        
