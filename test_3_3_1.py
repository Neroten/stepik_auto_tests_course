from selenium import webdriver
import time
import pytest

link1 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link1)


def test_reg1():
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

    assert "Congratulations! You have successfully registered!" == welcome_text


link2 = "http://suninjuly.github.io/registration1.html"
browser.get(link2)


def test_reg2():
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
    button.click( )
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == '__main__':
    pytest.main()

