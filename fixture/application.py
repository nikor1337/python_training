from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://192.168.1.75/addressbook/")

    def destroy(self):
        driver = self.driver
        driver.quit()