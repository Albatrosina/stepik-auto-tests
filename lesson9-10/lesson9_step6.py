from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")
confirm_btn = driver.find_element_by_css_selector("body > form > div > div > button").click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

driver.switch_to.default_content()
x = driver.find_element_by_css_selector("#input_value").text
answer = driver.find_element_by_css_selector("#answer").send_keys(calc(x))
submit_btn = driver.find_element_by_css_selector("body > form > div > div > button").click()

time.sleep(5)
driver.quit()