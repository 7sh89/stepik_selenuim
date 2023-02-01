import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

y_text = browser.find_element(By.CSS_SELECTOR, '#answer')
y_text.send_keys(y)

im_not_robot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
im_not_robot.click()

robot_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
robot_rule.click()

y = calc(x)

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.submit()

time.sleep(10)
browser.quit()