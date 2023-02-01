import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

links = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(links)

firstname = browser.find_element(By.CSS_SELECTOR, '[name=firstname]')
firstname.send_keys('FirsnName')

lastname = browser.find_element(By.CSS_SELECTOR, '[name=lastname]')
firstname.send_keys('Lastname')

email = browser.find_element(By.CSS_SELECTOR, '[name=email]')
email.send_keys('a@a.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '1.txt')

print(file_path)

file = browser.find_element(By.CSS_SELECTOR, '[name=file]')
file.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.submit()

time.sleep(15)
browser.quit()