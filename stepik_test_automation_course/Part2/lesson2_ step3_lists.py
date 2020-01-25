from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(int(num1) + int(num2)))

    button3 = browser.find_element_by_class_name("btn")
    button3.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()