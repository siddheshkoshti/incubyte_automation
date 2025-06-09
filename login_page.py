from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pythonProject1.pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.ID, "send2").click()

    def is_logged_in(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "customer-name"))
        )
