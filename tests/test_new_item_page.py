from selenium.webdriver.common.by import By

def test_open_new_item_creation_page(browser):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    new_item_header = browser.find_element(By.CSS_SELECTOR, ".jenkins-app-bar h1")

    assert "/newJob" in browser.current_url
    assert new_item_header.text == "New Item"

def test_ok_button_disabled_when_name_is_blank(browser):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    assert not browser.find_element(By.ID, "ok-button").is_enabled()
