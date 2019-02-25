from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import Grouphelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = Grouphelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0:
            return
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
