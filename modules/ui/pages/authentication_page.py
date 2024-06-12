from modules.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AuthPage(BasePage):

    CREATE_BUTTON_ID = 'SubmitCreate'
    EMAIL_FIELD_TO_CREATE_ID = 'email_create'
    EMAIL_FIELD_FOR_LOGIN_ID = 'email'
    PASSWORD_FIELD_FOR_LOGIN_ID = 'passwd'
    SIGN_IN_BUTTON_ID = 'SubmitLogin'
    def __init__(self, driver):
        super().__init__(driver)

    def open_authpage(self):
        authpage_url = 'http://prestashop.qatestlab.com.ua/ru/authentication'
        self.open(authpage_url)

    def create_account(self, email):
        email_field = self.driver.find_element(By.ID, self.EMAIL_FIELD_TO_CREATE_ID)
        email_field.send_keys(email)

        create_an_account_button = self.driver.find_element(By.ID, self.CREATE_BUTTON_ID)
        create_an_account_button.click()

    def login(self, email, password):
        email_field = self.driver.find_element(By.ID, self.EMAIL_FIELD_FOR_LOGIN_ID)
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.ID, self.PASSWORD_FIELD_FOR_LOGIN_ID)
        password_field.send_keys(password)

        signin_button = self.driver.find_element(By.ID, self.SIGN_IN_BUTTON_ID)
        signin_button.click()
