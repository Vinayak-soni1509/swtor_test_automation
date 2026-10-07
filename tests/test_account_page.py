import json

import pytest

from pages.account_page import Account_Page
from pages.home_page import HomePage
from test_data import logindetails
from test_data.logindetails import Login
from utils.config_reader import Configreader


def test_account_page_opens(setup):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    home.click_account()
    assert "signin" in home.get_url()

#parametrized using pytest methods
@pytest.mark.parametrize("username,password",
    [("sadawwra@gmail.com","pasdwad213"),("vtest@gmail.com","Password123")])

def test_incorrect_login(setup,username,password):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    home.click_account()
    accountpage = Account_Page(setup)
    accountpage.sign_in_flow(username,password)
    assert "Login failed. Please try again." in accountpage.login_error_message()


#creating same testcases with different parameterize methods

#using testdata pyfile
@pytest.mark.skip
@pytest.mark.parametrize("username,password",Login)
def test_incorrectestpy_login(setup,username,password):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.accept_cookies()
    home.click_account()
    accountpage = Account_Page(setup)
    accountpage.sign_in_flow(username,password)
    print(accountpage.verify_account_message())


#test using json
with open ("test_data/logindetails.json","r") as file:
    loginfile = json.load(file)
@pytest.mark.skip
@pytest.mark.parametrize("username,password",loginfile)
def test_incorrecttestson_login(setup,username,password):
    home = HomePage(setup)
    home.open_home_page(Configreader.get_base_url())
    home.dismiss_cookies()
    home.click_account()
    accountpage = Account_Page(setup)
    accountpage.sign_in_flow(username,password)
    assert (accountpage.verify_account_message())