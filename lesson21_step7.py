import math
from selenium import webdriver
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

print(calc(5))
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id("treasure")
    x=x1.get_attribute("valuex")
    y = calc(x)
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(y)
    input4 = browser.find_element_by_id("robotCheckbox")
    input4.click()
    input5 = browser.find_element_by_id("robotsRule")
    input5.click()
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(30)
	browser.quit()
