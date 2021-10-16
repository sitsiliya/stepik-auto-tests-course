from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements_by_css_selector(".first_block .form-control")
    e=browser.find_element_by_css_selector(".first_block .form-control.first")
    e.send_keys("Мой ответ")
    e=browser.find_element_by_css_selector(".first_block .form-control.second")
    e.send_keys("Мой ответ")
    e=browser.find_element_by_css_selector(".first_block .form-control.third")
    e.send_keys("Мой ответ")
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта Congratulations! You have successfully registered!
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    