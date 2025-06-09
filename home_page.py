from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def load(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

    def go_to_register(self):
        self.driver.find_element(By.LINK_TEXT, "Create an Account").click()
