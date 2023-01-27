from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Locators.locators import HomePageLocators

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.register_link = driver.find_element(By.XPATH, HomePageLocators.register_button_xpath)
        self.about = driver.find_element(By.XPATH, HomePageLocators.about_page_xpath)

    def click_register(self):
        self.register_link.click()

    def click_About_Page(self):
        self.about.click()