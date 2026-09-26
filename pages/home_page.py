from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.baseclass import BasePage

class HomePage(BasePage):
    Main_menu = (By.ID, "swtor-main-menu")
    Account_btn = (By.CSS_SELECTOR,".login")
    About = (By.LINK_TEXT,"About")
    About_section = (By.CLASS_NAME,"kotfe-legacyofthesith-lander")
    privacy_button = (By.ID,"truste-show-consent")
    privacy_accept = (By.CSS_SELECTOR,"button[class = 'acceptAllButtonLower']")
    shadowpopup = (By.CSS_SELECTOR,"div.trustarc_newcm_container.truste_popframe")
    privacy_close = (By.ID,"gwt-debug-close_id")


    def open_home_page(self,url):
        self.driver.get(url)

    def homepage_title(self):
        return "Star Wars: The Old Republic" in self.get_title()

    def is_homepage_loaded(self):
        return "https://www.swtor.com" in self.driver.current_url

    def main_menu_nav(self):
        return self.is_displayed(self.Main_menu)

    def about_navigation(self):
        self.click(self.About)
        return self.is_present(self.About_section)

    def click_account(self):
        self.click(self.Account_btn)

    def accept_cookies(self):
        self.click(self.privacy_button)
        #for shadow root we will use selenium 4 methods of shadow_root
        host = self.wait.until(EC.presence_of_element_located(self.shadowpopup))
        shadow = host.shadow_root
        accept_button = self.wait.until(lambda driver: shadow.find_element(*self.privacy_accept))
        accept_button.click()
        close_btn = self.wait.until(lambda driver: shadow.find_element(*self.privacy_close))
        close_btn.click()





