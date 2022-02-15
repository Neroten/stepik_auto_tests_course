from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    sum = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()