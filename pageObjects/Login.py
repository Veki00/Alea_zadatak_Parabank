from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Locators.locators import CustomerLoginLocators
from Locators.locators import AdminPageLocators

class CustomerLogin():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = driver.find_element(By.NAME, CustomerLoginLocators.username_input_name)
        self.password = driver.find_element(By.NAME, CustomerLoginLocators.password_input_name)
        self.login_button = driver.find_element(By.CSS_SELECTOR, CustomerLoginLocators.login_button)

    def enter_username(self, username):
        self.username.clear()
        self.username.send_keys(username)

    def enter_password(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def click_login(self):
        self.login_button.click()
