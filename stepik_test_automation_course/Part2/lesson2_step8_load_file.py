from selenium import webdriver
import os
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_class_name("form-control")
    for element in elements:
       element.send_keys("Мой ответ")

    load = browser.find_element_by_id("file")
    #load.click()
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')  # добавляем к этому пути имя файла
    load.send_keys(file_path)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


