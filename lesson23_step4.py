from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

print(math.log(abs(12*math.sin(5))))
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    time.sleep(2)
    confirm.accept()
    x1 = browser.find_element_by_id("input_value")
    x=x1.text
    y1 = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(10)
	browser.quit()