import pytest
from modules.ui.pages.authentication_page import AuthPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.authpage
def test_correct_email_registration(browser):
    auth_page = AuthPage(browser)
    auth_page.open_authpage()
    test_email = 'test@tezt.com'
    auth_page.create_account(test_email)
    email_field = auth_page.get_element_by(By.XPATH, '//*[@value="test@tezt.com"][@id="email"]')

    assert email_field is not None

@pytest.mark.authpage
def test_incorrect_email_registration(browser):
    auth_page = AuthPage(browser)
    auth_page.open_authpage()
    test_email = 'test'
    auth_page.create_account(test_email)
    error = auth_page.get_element_by(By.XPATH, '//*[@id="create_account_error"]/ol/li')

    actual_result = error.text
    expected_result = 'Invalid email address.'
    assert actual_result == expected_result

@pytest.mark.authpage
def test_login_with_correct_credentials(browser):
    auth_page = AuthPage(browser)
    auth_page.open_authpage()
    test_email = 'qatestanother46@gmx.com'
    test_password = 'Qapass22!'
    auth_page.login(test_email, test_password)

    expected_title = 'Мой аккаунт - http://prestashop.qatestlab.com.ua/'
    assert auth_page.check_title(expected_title)


@pytest.mark.authpage
def test_add_item_into_wishlist(browser):
    auth_page = AuthPage(browser)
    women_section = auth_page.get_element_by(By.CLASS_NAME, 'sf-with-ul')
    women_section.click()
    item = auth_page.get_element_by(By.XPATH, '//*[@title="Faded Short Sleeve T-shirts"][@class="product_img_link"]')
    item.click()
    add_to_wishes_btn = auth_page.get_element_by(By.ID, 'wishlist_button')
    add_to_wishes_btn.click()
    close_btn = auth_page.get_element_by(By.CSS_SELECTOR, '.fancybox-item.fancybox-close')
    close_btn.click()
    account_btn = auth_page.get_element_by(By.CLASS_NAME, 'header_user_info')
    account_btn.click()
    wishlist_btn = auth_page.get_element_by(By.CLASS_NAME, 'lnk_wishlist')
    wishlist_btn.click()
    amount = auth_page.get_element_by(By.CSS_SELECTOR, '.bold.align_center')
    my_wishlist_btn = auth_page.get_element_by(By.XPATH, '//*[@id="wishlist_9881"]/td[1]/a')
    my_wishlist_btn.click()

    actual_product_added = auth_page.get_element_by(By.ID, 's_title').text
    expected_product_name = ['Faded', 'Short', 'Sleeve', 'T-shirts']
    actual_product_amount = auth_page.get_element_by(By.ID, 'quantity_1_1').get_attribute('value')

    #Product name on the site is using some strange spaces, thats why we are looking word by word
    assert all(word in actual_product_added for word in expected_product_name) and actual_product_amount == '1'

@pytest.mark.authpage
def test_delete_item_from_wishlist(browser):
    auth_page = AuthPage(browser)
    delete_button = auth_page.get_element_by(By.CLASS_NAME, 'icon-remove-sign')
    delete_button.click()
    auth_page.refresh_page()
    actual_amount = auth_page.get_element_by(By.CSS_SELECTOR, '.bold.align_center').text

    assert actual_amount == '0'


