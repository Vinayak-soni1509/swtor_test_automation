from pages.baseclass import BasePage

class HomePage(BasePage):

    def open_home_page(self,url):
        self.driver.get(url)
