from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import Configreader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,Configreader.get_timeout())

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator,value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def is_displayed(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_present(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator)).is_enabled()

    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))