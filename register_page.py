import random
from selenium.webdriver.common.by import By
from pythonProject1.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
    def register_new_user(self):
        email = f"testuser{random.randint(1000,9999)}@mail.com"
        password = "Test@1234"

        self.driver.find_element(By.ID, "firstname").send_keys("Test")
        self.driver.find_element(By.ID, "lastname").send_keys("User")
        self.driver.find_element(By.ID, "email_address").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password-confirmation").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.submit").click()

        return email, password

    def check_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "message-success"))
        )

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".customer-name").click()
        self.driver.find_element(By.LINK_TEXT, "Sign Out").click()
