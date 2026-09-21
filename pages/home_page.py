from selenium.webdriver.common.by import By

from pages.baseclass import BasePage

class HomePage(BasePage):
    Main_menu = (By.ID, "swtor-main-menu")


    def open_home_page(self,url):
        self.driver.get(url)

    def homepage_title(self):
        return "Star Wars: The Old Republic" in self.get_title()

    def is_homepage_loaded(self):
        return "https://www.swtor.com" in self.driver.current_url

    def main_menu_nav(self):
        return self.is_displayed(self.Main_menu)