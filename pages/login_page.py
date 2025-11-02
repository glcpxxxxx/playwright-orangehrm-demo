from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="username")
        self.password_input = page.get_by_role("textbox", name="password")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_heading = page.get_by_role("heading", name="Login")
        self.invalid_credential = page.get_by_text("Invalid credentials")
        
    def enter_username(self, username:str):
        self.username_input.fill(username)
        
    def enter_password(self, password:str):
        self.password_input.fill(password)
        
    def click_loginButton(self):
        self.login_button.click()
        
    #method that includes all the individual methods for login
    def login(self,username:str,password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_loginButton()