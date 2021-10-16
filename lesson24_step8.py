from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    #assert "$100" in price.text
    button = browser.find_element_by_id("book")
    button.click()
    x1 = browser.find_element_by_id("input_value")
    x=x1.text
    y1 = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y1)
    button = browser.find_element_by_id("solve")
    button.click()
	


finally:
	time.sleep(10)
	browser.quit()