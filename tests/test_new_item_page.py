from selenium.webdriver.common.by import By

def test_open_new_item_creation_page(browser):

    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/newJob']").click()
    new_item_header = browser.find_element(By.CSS_SELECTOR, ".jenkins-app-bar h1")

    assert "/newJob" in browser.current_url
    assert new_item_header.text == "New Item"
