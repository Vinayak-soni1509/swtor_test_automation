import os

import pytest
from pytest_html import extras

from utils.config_reader import Configreader
from utils.driver_factory import DriverFactory

@pytest.fixture()
def setup():
    browser = Configreader.get_browser()
    driver = DriverFactory.get_driver(browser)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report
            extras_list = getattr(report, "extras", [])

            extras_list.append(
                extras.image(screenshot_path)
            )

            report.extras = extras_list