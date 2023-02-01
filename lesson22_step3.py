import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

a = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
b = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
c = str(a + b)

answer = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
answer.select_by_value(c)

browser.find_element(By.CSS_SELECTOR, 'button.btn').submit()

time.sleep(10)
browser.quit()