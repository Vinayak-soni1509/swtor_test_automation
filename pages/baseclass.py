from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import Configreader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,Configreader.get_timeout())

    def click(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self,locator,value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_title(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))