from pages.home_page import HomePage
from utils.config_reader import Configreader


def test_homepage_loads_successfully(setup):
    home = HomePage()
    url =home.open_home_page(Configreader.get_base_url())
    print(url)