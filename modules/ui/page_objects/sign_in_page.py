from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'http://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # find the field where we will enter the wrong username or email
        login_elem = self.driver.find_element(By.ID, "login_field")

        # enter the wrong username or email 
        login_elem.send_keys(username)

        # find the field where we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        # enter the wrong password  
        pass_elem.send_keys(password)

        # find button sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # emulate left mouse button click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title