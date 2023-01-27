from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Locators.locators import RegistrationPageLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.firstname = driver.find_element(By.ID, RegistrationPageLocators.firstname_input_ID)
        self.lastname =driver.find_element(By.ID, RegistrationPageLocators.lastname_input_ID)
        self.adress = driver.find_element(By.ID, RegistrationPageLocators.adress_input_ID)
        self.city = driver.find_element(By.ID, RegistrationPageLocators.city_input_ID)
        self.state = driver.find_element(By.ID, RegistrationPageLocators.state_input_ID)
        self.zip_code = driver.find_element(By.ID, RegistrationPageLocators.zip_code_input_ID)
        self.phone = driver.find_element(By.NAME, RegistrationPageLocators.phone_input_NAME)
        self.snn = driver.find_element(By.NAME, RegistrationPageLocators.snn_input_NAME)
        self.username = driver.find_element(By.ID, RegistrationPageLocators.username_input_ID)
        self.password =driver.find_element(By.ID, RegistrationPageLocators.password_input_ID)
        self.confirm_password = driver.find_element(By.ID, RegistrationPageLocators.confirm_password_input_ID)
        self.register_button = driver.find_element(By.XPATH, RegistrationPageLocators.register_button_CSS)
        self.successfull_reg_message = driver.find_element(By.XPATH, RegistrationPageLocators.successfull_reg_mess)
        self.field_required_message = driver.find_elements(By.CLASS_NAME, RegistrationPageLocators.field_required_mess)

    def enter_firstname(self, firstname):
        self.firstname.clear()
        self.firstname.send_keys(firstname)

    def enter_lastname(self, lastname):
        self.lastname.clear()
        self.lastname.send_keys(lastname)

    def enter_adress(self, adress):
        self.adress.clear()
        self.adress.send_keys(adress)

    def enter_city(self, city):
        self.city.clear()
        self.city.send_keys(city)

    def enter_state(self, state):
        self.state.clear()
        self.state.send_keys(state)

    def enter_zip_code(self, zip_code):
        self.zip_code.clear()
        self.zip_code.send_keys(zip_code)

    def enter_phone(self, phone):
        self.phone.clear()
        self.phone.send_keys(phone)

    def enter_snn(self, snn):
        self.snn.clear()
        self.snn.send_keys(snn)

    def enter_username(self, username):
        self.username.clear()
        self.username.send_keys(username)

    def enter_password(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.confirm_password.clear()
        self.confirm_password.send_keys(confirm_password)

    def click_register_btn(self):
        self.register_button.click()

    def verify_successfull_reg(self):
        self.expected_text = "Your account was created successfully. You are now logged in."
        try:
            if self.successfull_reg_message.text == self.expected_text:
                print("User is registered successfully")
            else:
                print("I could not find element")
        except:
            self.driver.get_screenshot_as_file("../ScreenShots/registration_failed.png")
            print("Message: {Your account was created successfully. You are now logged in.} is not located")
            return False

    def verify_error_mess_required(self):
        err_elements = self.field_required_message
        try:
            for elem in err_elements:
                if not elem.is_displayed():
                    return False
            print("Error messages displayed")
            return True
        except:
            self.driver.get_screenshot_as_file("../ScreenShots/empty_fields_err.png")
            print("Elements not found!")

    def verify_errMessage_duplicate_username(self):
        try:
            error_message = self.driver.find_element(By.ID, "customer.username.errors")
            assert  error_message.is_displayed() == True, "Error message is not displayed"

            expected_error_message = "This username already exists."
            assert error_message.text == expected_error_message, f"Expected error message: {expected_error_message}, but got: {error_message.text}"
        except:
            self.driver.get_screenshot_as_file("../ScreenShots/duplicate_username_err.png")
            print("SeleniumTimeout: Error message not found!")


    def verify_errMessage_no_matching_password(self):
        self.no_matching_password = self.wait.until(EC.visibility_of_element_located((By.ID, "repeatedPassword.errors")))
        if self.no_matching_password.is_displayed():
            print("Error message displayed")
        else:
            print("Could not find err message!")

    def verify_errMessage_invalid_data(self):
        err_elements = self.field_required_message
        try:
            for elem in err_elements:
                if not elem.is_displayed():
                    return False
            print("Error messages displayed")
            assert err_elements.text == "Error: Invalid data", \
                f"Error message text does not match."
            return True
        except:
            self.driver.get_screenshot_as_file("../ScreenShots/invalid_data_err.png")
            print("SeleniumTimeout: Error message not found!")






