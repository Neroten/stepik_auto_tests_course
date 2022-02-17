from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link1)


class Testreg(unittest.TestCase):
    def test_reg1(self):
        first = browser.find_element_by_xpath(".//label[text()='First name*']/following-sibling::input")
        first.send_keys("Ivan")
        last = browser.find_element_by_xpath(".//label[text()='Last name*']/following-sibling::input")
        last.send_keys("Petrov")
        email = browser.find_element_by_xpath(".//label[text()='Email*']/following-sibling::input")
        email.send_keys("ip@pi.ru")
        phone = browser.find_element_by_xpath(".//label[text()='Phone:']/following-sibling::input")
        phone.send_keys("+73049503045")
        adr = browser.find_element_by_xpath(".//label[text()='Address:']/following-sibling::input")
        adr.send_keys("+73049503045")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    link2 = "http://suninjuly.github.io/registration1.html"
    browser.get(link2)

    def test_reg2(self):
        input1 = browser.find_element_by_xpath(".//label[text()='First name*']/following-sibling::input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath(".//label[text()='Last name*']/following-sibling::input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath(".//label[text()='Email*']/following-sibling::input")
        input3.send_keys("ip@pi.ru")
        input4 = browser.find_element_by_xpath(".//label[text()='Phone:']/following-sibling::input")
        input4.send_keys("+73049503045")
        input5 = browser.find_element_by_xpath(".//label[text()='Address:']/following-sibling::input")
        input5.send_keys("+73049503045")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == '__main__':
    unittest.main()

