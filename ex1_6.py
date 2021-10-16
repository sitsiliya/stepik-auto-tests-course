import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(2)
button = browser.find_element_by_id("submit_button")

button.click()
time.sleep(5)
browser.quit()