from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Petrov")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Petrov")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test2.txt')
    #with open(file_path, "w") as file:
    #    content = file.write("automationbypython")  # create test.txt file
    input = browser.find_element_by_id("file")
    input.send_keys(file_path)
    #time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
	time.sleep(20)
	browser.quit()