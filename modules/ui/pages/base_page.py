from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_element_by(self, ByDotType, value):
        return WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable((ByDotType, value)))

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def refresh_page(self):
        self.driver.refresh()



