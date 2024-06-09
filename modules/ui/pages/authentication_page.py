from modules.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_authpage(self):
        authpage_url = 'http://prestashop.qatestlab.com.ua/ru/authentication'
        self.open(authpage_url)

    def create_account(self, email):
        email_field = self.driver.find_element(By.ID, 'email_create')
        email_field.send_keys(email)

        create_an_account_button = self.driver.find_element(By.ID, 'SubmitCreate')
        create_an_account_button.click()

    def login(self, email, password):
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.ID, 'passwd')
        password_field.send_keys(password)

        signin_button = self.driver.find_element(By.ID, 'SubmitLogin')
        signin_button.click()
