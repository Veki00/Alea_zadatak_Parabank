import json
import time
import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pageObjects.RegistrationPage import RegistrationPage
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
        hp = HomePage(self.driver)
        hp.click_register()
        time.sleep(2)
        self.wait.until(EC.title_is("ParaBank | Register for Free Online Account Access"))
        self.rp = RegistrationPage(self.driver)


    def test_registration(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.rp = RegistrationPage(self.driver)
        self.username_broj = randint(1,100)
        time.sleep(2)
        self.rp.enter_firstname(data["firstname"])
        self.rp.enter_lastname(data["lastname"])
        self.rp.enter_adress(data["adress"])
        self.rp.enter_city(data["city"])
        self.rp.enter_state(data["state"])
        self.rp.enter_zip_code(data["zip"])
        self.rp.enter_phone(data["phone"])
        self.rp.enter_snn(data["snn"])
        time.sleep(3)
        self.rp.enter_username(data["username"]+f"{self.username_broj}")
        self.rp.enter_password(data["password"])
        self.rp.enter_confirm_password(data["confirm_password"])
        self.rp.click_register_btn()
        time.sleep(2)
        self.rp.verify_successfull_reg()
        time.sleep(2)

    #Registracija – sva polja prazna
    def test_registration_all_fields_empty(self):
        self.rp.click_register_btn()
        time.sleep(2)
        self.rp.verify_error_mess_required()
        time.sleep(2)

    #Registracija – duplikat username
    def test_registration_duplicate_username(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.rp = RegistrationPage(self.driver)
        self.username_broj = randint(1,100)
        time.sleep(2)
        self.rp.enter_firstname(data["firstname"])
        self.rp.enter_lastname(data["lastname"])
        self.rp.enter_adress(data["adress"])
        self.rp.enter_city(data["city"])
        self.rp.enter_state(data["state"])
        self.rp.enter_zip_code(data["zip"])
        self.rp.enter_phone(data["phone"])
        self.rp.enter_snn(data["snn"])
        time.sleep(3)
        self.rp.enter_username("Pero30")
        self.rp.enter_password(data["password"])
        self.rp.enter_confirm_password(data["confirm_password"])
        self.rp.click_register_btn()
        time.sleep(2)
        self.rp.verify_errMessage_duplicate_username()

    #Registracija – pogresni podaci u svim poljima
    #Ovdje postoji bug gdje se korisnik moze registrovati sa ne validnim podacima,
    #zato ce se svaki put generisati screenshot kad verifikacija ne prodje
    def test_registration_all_data_not_valid(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.rp = RegistrationPage(self.driver)
        self.username_broj = randint(1,100)
        self.random_broj = randint(100, 1000)
        time.sleep(2)
        self.rp.enter_firstname(f"{self.random_broj}")
        self.rp.enter_lastname(f"{self.random_broj}")
        self.rp.enter_adress(f"{self.random_broj}")
        self.rp.enter_city(f"{self.random_broj}")
        self.rp.enter_state(f"{self.random_broj}")
        self.rp.enter_zip_code(data["firstname"])
        self.rp.enter_phone(data["lastname"])
        self.rp.enter_snn(data["username"])
        time.sleep(3)
        self.rp.enter_username(f"!@#{self.username_broj}")
        self.rp.enter_password("123")
        self.rp.enter_confirm_password("123")
        self.rp.click_register_btn()
        time.sleep(2)
        self.rp.verify_errMessage_invalid_data()

    #Registracija – lozinka se ne podudara
    def test_registration_password_no_match(self):
        with open("../TestData/data.json") as file:
            data = json.load(file)
        self.rp = RegistrationPage(self.driver)
        self.username_broj = randint(1, 100)
        self.rp.enter_firstname(data["firstname"])
        self.rp.enter_lastname(data["lastname"])
        self.rp.enter_adress(data["adress"])
        self.rp.enter_city(data["city"])
        self.rp.enter_state(data["state"])
        self.rp.enter_zip_code(data["zip"])
        self.rp.enter_phone(data["phone"])
        self.rp.enter_snn(data["snn"])
        self.rp.enter_username(data["username"] + f"{self.username_broj}")
        self.rp.enter_password(data["password"])
        self.rp.enter_confirm_password(data["noMatching_conf_password"])
        self.rp.click_register_btn()
        self.rp.verify_errMessage_no_matching_password()



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()