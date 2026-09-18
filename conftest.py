import pytest

from utils.config_reader import Configreader
from utils.driver_factory import DriverFactory

@pytest.fixture()
def setup():
    browser = Configreader.get_browser()
    driver = DriverFactory.get_driver(browser)
    yield driver

    driver.quit()