import pytest
from modules.ui.pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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

@pytest.mark.homepage
def test_add_item_with_cart_redirection(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    item = home_page.get_element_by(By.XPATH, '//*[@title="Faded Short Sleeve T-shirts"][@class="product_img_link"]')
    actions = ActionChains(browser)
    actions.scroll_to_element(item)
    actions.move_to_element(item).perform()

    btn_add_to_cart = home_page.get_element_by(By.XPATH, '//*[@title="Add to cart"]')
    btn_add_to_cart.click()
    btn_to_order = home_page.get_element_by(By.CSS_SELECTOR, '.btn.btn-default.button.button-medium')
    btn_to_order.click()
    expected_text = 'Faded Short Sleeve T-shirts'

    assert home_page.get_element_by(By.XPATH, '//*[@id="product_1_1_0_0"]/td[2]/p/a').text == expected_text

def test_amount_of_items(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    list = browser.find_elements(By.CLASS_NAME, 'product-container')
    amount_of_items = len(list)
    expected_amount = 14
    assert amount_of_items == expected_amount
