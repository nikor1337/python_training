from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://192.168.1.75/addressbook/")

    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.ID, "content").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        driver = self.driver
        driver.quit()