import pytest
from modules.ui.pages.authentication_page import AuthPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def test_correct_email_registration(browser):
    auth_page = AuthPage(browser)
    auth_page.open_authpage()
    test_email = 'test@tezt.com'
    auth_page.create_account(test_email)
    email_field = auth_page.get_element_by(By.XPATH, '//*[@value="test@tezt.com"][@id="email"]')

    assert email_field is not None

def test_incorrect_email_registration(browser):
    auth_page = AuthPage(browser)
    auth_page.open_authpage()
    test_email = 'test'
    auth_page.create_account(test_email)
    error = auth_page.get_element_by(By.XPATH, '//*[@id="create_account_error"]/ol/li')

    actual_result = error.text
    expected_result = 'Invalid email address.'
    assert actual_result == expected_result
