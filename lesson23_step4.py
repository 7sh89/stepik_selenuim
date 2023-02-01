import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

links = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(links)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

y_text = browser.find_element(By.CSS_SELECTOR, '#answer')
y_text.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.submit()

time.sleep(15)
browser.quit()