from selenium import webdriver as wdr
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, userAgent, base_url):
        if userAgent == "Browser/Chrome":
            self.driverMode = wdr.Chrome()
        elif userAgent == "Browser/Firefox":
            self.driverMode = wdr.Firefox()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def destroy(self):
        driver = self.driver
        driver.quit()