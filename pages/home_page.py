from selenium.webdriver.common.by import By

from pages.baseclass import BasePage

class HomePage(BasePage):
    Main_menu = (By.ID, "swtor-main-menu")
    About = (By.LINK_TEXT,"About")
    privacy_button = (By.ID,"truste-show-consent")
    privacy_accept = (By.CSS_SELECTOR,".acceptAllButtonLower")
    shadowpopup = (By.CSS_SELECTOR,".trustarc_newcm_container")


    def open_home_page(self,url):
        self.driver.get(url)

    def homepage_title(self):
        return "Star Wars: The Old Republic" in self.get_title()

    def is_homepage_loaded(self):
        return "https://www.swtor.com" in self.driver.current_url

    def main_menu_nav(self):
        return self.is_displayed(self.Main_menu)

    def about_navigation(self):
        return self.click(self.About)

    def accept_cookies(self):
        self.click(self.privacy_button)
        #for shadow root we will use selenium 4 methods of shadow_root
        host = self.find_element(self.shadowpopup)

        shadow = self.wait.until( host.shadow_root)
        return shadow.find_element(self.privacy_accept).click()



