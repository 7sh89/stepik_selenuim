import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

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
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
robot_rule.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
browser.quit()