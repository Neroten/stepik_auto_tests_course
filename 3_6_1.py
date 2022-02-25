import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestUrl:
    def test_stepic_urls(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = links
        browser.get(link)
        browser.implicitly_wait(10)
        input = browser.find_element_by_tag_name("textarea")
        input.send_keys(answer)
        button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CLASS_NAME,"submit-submission")))
        button.click()
        mes = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.TAG_NAME,"pre")))
        assert "Correct!" in mes.text

        if __name__ == "__main__":
            pytest.main()
