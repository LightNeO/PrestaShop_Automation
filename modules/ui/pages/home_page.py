from modules.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    LANGUAGE_XPATH = '//*[@id="languages-block-top"]/div/span'
    CURRENCY_XPATH = '//*[@class="current"]/strong'
    PHONE_NUMBER_XPATH = '//*[@class="shop-phone"]/strong'
    SEARCH_FIELD_CLASS = 'search_query'
    SEARCH_BUTTON_NAME = 'submit_search'
    def __init__(self, driver):
        super().__init__(driver)

    def open_homepage(self):
        homepage_url = 'http://prestashop.qatestlab.com.ua/'
        self.open(homepage_url)
    def get_page_language(self):
        page_language = self.get_element_by(By.XPATH, self.LANGUAGE_XPATH).text
        return page_language

    def get_currency(self):
        currency = self.get_element_by(By.XPATH, self.CURRENCY_XPATH).text
        return currency

    def get_phone_number(self):
        phone_number = self.get_element_by(By.XPATH, self.PHONE_NUMBER_XPATH).text
        return phone_number

    def search_for_item(self, item_name):
        search_field = self.get_element_by(By.CLASS_NAME, self.SEARCH_FIELD_CLASS)
        search_field.send_keys(item_name)

        search_button = self.get_element_by(By.NAME, self.SEARCH_BUTTON_NAME)
        search_button.click()

