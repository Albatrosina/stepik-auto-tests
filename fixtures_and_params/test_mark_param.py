import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'])
def test_specific_link_time(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    text_field = browser.find_element_by_css_selector("#ember67")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(str(answer))
    submit_btn = browser.find_element_by_css_selector(".submit-submission").click()
    wait = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"))
    result = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(result)
    assert result == "Correct!", "Wrong result.Try again!"