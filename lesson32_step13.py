from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("a@a.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Регистрация не прошла, не заполнены обязательные поля")

        time.sleep(2)
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("a@a.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Регистрация не прошла, не заполнены обязательные поля")

        time.sleep(2)
        browser.quit()

if __name__ == '__main__':
    unittest.main()