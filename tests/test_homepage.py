import pytest
from modules.ui.pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.homepage
def test_default_language(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()

    actual_result = home_page.get_page_language()
    expected_result = 'Русский'
    assert expected_result == actual_result

@pytest.mark.homepage
def test_default_currency(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()

    actual_result = home_page.get_currency()
    expected_result = 'UAH'
    assert actual_result == expected_result

@pytest.mark.homepage
def test_phone_number(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()

    actual_result = home_page.get_phone_number()
    expected_result = '0123-456-789'
    assert actual_result == expected_result

@pytest.mark.homepage
def test_search_functionality(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.search_for_item('Blouse')
    element = home_page.get_element_by(By.CLASS_NAME, 'lighter')

    actual_result = element.text
    expected_result = '"BLOUSE"'
    assert actual_result == expected_result
