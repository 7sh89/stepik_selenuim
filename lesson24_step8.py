import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

button = browser.find_element(By.ID, 'book')
button.click()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)

solve = browser.find_element(By.ID, 'solve')
solve.submit()

time.sleep(25)
browser.quit()