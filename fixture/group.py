from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
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

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        driver.find_element(By.NAME, "selected[]").click()
        # submit deletion
        driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()