from pages.account_page import Account_Page
from pages.home_page import HomePage
from utils.config_reader import Configreader


def test_account_page_opens(setup):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    home.click_account()
    assert "signin" in home.get_url()

def test_incorrect_login(setup):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    home.click_account()
    accountpage = Account_Page(setup)
    accountpage.sign_in_flow()
    assert "Login failed. Please try again." in accountpage.login_error_message()

