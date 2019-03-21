from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import Grouphelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url, user, password):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = Grouphelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.user = user
        self.password = password

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
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
