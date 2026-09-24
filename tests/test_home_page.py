from pages.home_page import HomePage
from utils.config_reader import Configreader


def test_homepage_loads_successfully(setup):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    assert home.is_homepage_loaded()

def test_page_title(setup):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    assert home.homepage_title()

def test_main_menu_displayed(setup):
    home =HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    assert home.main_menu_nav()

def test_about_section_redirects_correctly(setup):
    home =HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    assert home.about_navigation()

