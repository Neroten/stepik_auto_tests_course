from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    input1 = browser.find_element_by_xpath(".//label[text()='First name* ']/following-sibling::input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath(".//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath(".//label[text()='Email * ']/following-sibling::input")
    input3.send_keys("ip@pi.ru")
    input4 = browser.find_element_by_xpath('//*[@id="file"]')
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()