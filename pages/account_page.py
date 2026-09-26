from selenium.webdriver.common.by import By

from pages import baseclass
from pages.baseclass import BasePage


class Account_Page(BasePage):
    Username = (By.ID,"username")
    Password = (By.ID,"password")
    SignIn = (By.CSS_SELECTOR,"button[type = 'submit']")
    SignInError = (By.CSS_SELECTOR,"div[class='FlashMessage error']")

    def sign_in_flow(self):
        self.send_keys(self.Username,"testadsfdsbd")
        self.send_keys(self.Password,"passddsgsdgw")
        self.click(self.SignIn)

    def login_error_message(self):
        return self.is_displayed(self.SignInError).text