import time

from selenium.webdriver.common.by import By

from pages import baseclass
from pages.baseclass import BasePage


class Account_Page(BasePage):
    Username = (By.ID,"username")
    Password = (By.ID,"password")
    SignIn = (By.CSS_SELECTOR,"button[type = 'submit']")
    SignInError = (By.CSS_SELECTOR,"div[class='FlashMessage error']")
    Verify_account = (By.CSS_SELECTOR,".DefaultBoxTitle")

    def sign_in_flow(self,username,password):
        self.send_keys(self.Username,username)
        self.send_keys(self.Password,password)
        self.click(self.SignIn)

    def login_error_message(self):
        return self.is_displayed(self.SignInError).text
    def verify_account_message(self):
        return self.find_element(self.Verify_account).text