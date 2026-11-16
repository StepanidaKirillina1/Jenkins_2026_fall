from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_open_new_item_creation_page(browser):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    new_item_header = browser.find_element(By.CSS_SELECTOR, ".jenkins-app-bar h1")

    assert "/newJob" in browser.current_url
    assert new_item_header.text == "New Item"

def test_ok_button_disabled_when_name_is_blank(browser):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    assert not browser.find_element(By.ID, "ok-button").is_enabled()

@pytest.mark.parametrize("unsupported_characters", ["?", "*", "/", "!", "%", "$", "&", ";", ":"])
def test_verify_error_message(browser, unsupported_characters, wait5):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(unsupported_characters)

    error_message = wait5.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error"))).text
    assert error_message == f"‘{unsupported_characters}’ is an unsafe character"
