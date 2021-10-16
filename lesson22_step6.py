import math
from selenium import webdriver
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

print(math.log(abs(12*math.sin(5))))
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_id("input_value")
    x=x1.text
    y1 = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y1)
    input1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    input1.click()
    ruler = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", ruler)
    ruler.click()
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(20)
	browser.quit()