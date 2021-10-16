import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def calc(x,y):
  return str(int(x)+int(y))

print(calc(5,22))
link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id("num1")
    x=x1.text
    y1 = browser.find_element_by_id("num2")
    y=y1.text
    y1 = calc(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y1)
    #time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(20)
	browser.quit()