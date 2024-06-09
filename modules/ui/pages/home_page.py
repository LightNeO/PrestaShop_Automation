from modules.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_homepage(self):
        homepage_url = 'http://prestashop.qatestlab.com.ua/'
        self.open(homepage_url)
    def get_page_language(self):
        page_language = self.get_element_by(By.XPATH, '//*[@id="languages-block-top"]/div/span').text
        return page_language

    def get_currency(self):
        currency = self.get_element_by(By.XPATH, '//*[@class="current"]/strong').text
        return currency

    def get_phone_number(self):
        phone_number = self.get_element_by(By.XPATH, '//*[@class="shop-phone"]/strong').text
        return phone_number

    def search_for_item(self, item_name):
        search_field = self.get_element_by(By.CLASS_NAME, 'search_query')
        search_field.send_keys(item_name)

        search_button = self.get_element_by(By.NAME, 'submit_search')
        search_button.click()

