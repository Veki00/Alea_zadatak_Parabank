
class HomePageLocators():
    register_button_xpath = '//*[@id="loginPanel"]/p[2]/a'
    about_page_xpath = '//*[@id="headerPanel"]/ul[1]/li[2]/a'

class CustomerLoginLocators():
    username_input_name = 'username'
    password_input_name = 'password'
    login_button = '.button'

class RegistrationPageLocators():
    firstname_input_ID = "customer.firstName"
    lastname_input_ID = "customer.lastName"
    adress_input_ID = "customer.address.street"
    city_input_ID = "customer.address.city"
    state_input_ID = "customer.address.state"
    zip_code_input_ID = "customer.address.zipCode"
    phone_input_NAME = "customer.phoneNumber"
    snn_input_NAME = "customer.ssn"
    username_input_ID = "customer.username"
    password_input_ID = "customer.password"
    confirm_password_input_ID = "repeatedPassword"
    register_button_CSS = '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input'
    successfull_reg_mess = '//*[@id="rightPanel"]/p'
    field_required_mess = 'error'

class AdminPageLocators():
    admin_username_input_xpath = '//*[@id="loginPanel"]/form/div[1]/input'
    admin_password_input_xpath = '//*[@id="loginPanel"]/form/div[2]/input'
    admin_login_button = '//*[@id="loginPanel"]/form/div[3]/input'
