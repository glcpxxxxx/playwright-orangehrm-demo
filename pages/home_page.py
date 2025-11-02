class HomePage:
    def __init__(self,page):
        page.page = page
        # side nav
        self.admin_link = page.get_by_role("link", name="Admin")
        self.pim_link = page.get_by_role("link", name="PIM")
        self.leave_link = page.get_by_role("link", name="Leave", exact="True")
        self.time_link = page.get_by_role("link", name="Time")
        self.recruitment_link = page.get_by_role("link",name="Recruitment").filter(has_text="Recruitment").first
        self.my_info_link = page.get_by_role("link", name="My Info")
        self.performance_link = page.get_by_role("link",name="Performance")
        self.dashboard_link = page.get_by_role("link",name="Dashboard")
        self.claim_link = page.get_by_role("link",name="Claim")
        # navbar
        self.upgrade_button = page.get_by_role("link", name="Upgrade")
        self.profile_picture = page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.logout_button = page.get_by_role("menuitem", name="Logout")
    
    def click_recruitment(self):
        self.recruitment_link.click()
    
    def click_performance(self):
        self.performance_link.click()
        
    def click_dashboard(self):
        self.dashboard_link.click()
        
    def click_leave(self):
        self.leave_link.click()
        
    def click_claim(self):
        self.claim_link.click()
    
    def click_pim(self):
        self.pim_link.click()
        
    def click_time(self):
        self.time_link.click()
        
    def click_my_info(self):
        self.my_info_link.click()
    
    def click_logout(self):
        self.profile_picture.click()
        self.logout_button.click()