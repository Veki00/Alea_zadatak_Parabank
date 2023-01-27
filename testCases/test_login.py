import json
import time
import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Login import CustomerLogin
from pageObjects.HomePage import HomePage



class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.delete_all_cookies()

        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.expected_title = "ParaBank | Welcome | Online Banking"
        self.wait.until(EC.title_is(self.expected_title))
        assert self.expected_title in self.driver.title
        assert self.driver.find_element(By.ID, "leftPanel").is_displayed()


    def test_login_valid_login(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.lp = CustomerLogin(self.driver)
        self.lp.enter_username(data["login_username"])
        self.lp.enter_password(data["login_password"])
        self.lp.click_login()
        #Verify success
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        element = self.driver.find_element(By.TAG_NAME, "h1")
        assert element.is_displayed(), "Element didn't found"
        assert element.text == "Accounts Overview", "Text not match"

    #Login – pogresna sifra
    def test_login_invalid_password(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
           # userLogin = data["Login"]
        self.lp = CustomerLogin(self.driver)
        self.lp.enter_username(data["login_username"])
        self.lp.enter_password("123")
        self.lp.click_login()
        # Verify
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rightPanel"]/p')))
        message = self.driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p')
        assert message.is_displayed() and message.text == "An internal error has occurred and has been logged."

    #Login – prazna polja
    def test_login_empty_fields(self):
        self.lp = CustomerLogin(self.driver)
        self.lp.click_login()
        # Verify
        message = self.driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rightPanel"]/p')))
        assert message.is_displayed() and message.text == "Please enter a username and password."

    #Login - nepostojeci korisnik
    def test_login_nonexistent_user(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.lp = CustomerLogin(self.driver)
        self.lp.enter_username("Marko999")
        self.lp.enter_password(data["login_password"])
        self.lp.click_login()
        # Verify
        message = self.driver.find_element(By.XPATH, '//*[@id="rightPanel"]/p')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rightPanel"]/p')))
        assert message.is_displayed() and message.text == "An internal error has occurred and has been logged."

    #Login sa stranice About us
    def test_login_login_from_admin_page(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.hp = HomePage(self.driver)
        self.lp = CustomerLogin(self.driver)
        self.hp.click_About_Page()
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="rightPanel"]/h1'), "ParaSoft Demo Website"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input').send_keys(data["login_username"])
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input').send_keys(data["login_password"])
        self.driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()
        #Verify success
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        element = self.driver.find_element(By.TAG_NAME, "h1")
        assert element.is_displayed(), "Element didn't found"
        assert element.text == "Accounts Overview", "Text not match"


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()