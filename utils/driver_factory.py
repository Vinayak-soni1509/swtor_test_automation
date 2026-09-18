from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
            driver.maximize_window()
            return driver
        elif browser.lower()=="firefox":
            driver = webdriver.firefox(service = Service(GeckoDriverManager().install()))
            driver.maximize_window()
            return driver
        raise Exception(
            f"Browser {browser} is not supported"
        )

