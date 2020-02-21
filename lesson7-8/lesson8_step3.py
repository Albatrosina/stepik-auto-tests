from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects2.html")
num1 = driver.find_element_by_css_selector("#num1").text
num2 = driver.find_element_by_css_selector("#num2").text
res = int(num1) + int(num2)
select = Select(driver.find_element_by_css_selector("#dropdown"))
select.select_by_visible_text(str(res))
submit_btn = driver.find_element_by_css_selector("body > div > form > button").click()
time.sleep(5)
driver.quit()