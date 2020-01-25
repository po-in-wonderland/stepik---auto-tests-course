import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    pole = browser.find_element_by_id("answer")
    pole.send_keys(y)

    button1 = browser.find_element_by_id("robotCheckbox")
    button1.click()

    button2 = browser.find_element_by_id("robotsRule")
    button2.click()

    button3 = browser.find_element_by_class_name("btn")
    button3.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()