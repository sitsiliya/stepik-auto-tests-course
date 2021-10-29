import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_for_shop(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(10)
    assert button != None, "Button not found!"