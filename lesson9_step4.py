from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")
confirm_btn = driver.find_element_by_css_selector("body > form > div > div > button").click()
alrt = driver.switch_to.alert
alrt.accept()

driver.switch_to.default_content()
x = driver.find_element_by_css_selector("#input_value").text
answer = driver.find_element_by_css_selector("#answer").send_keys(calc(x))
submit_btn = driver.find_element_by_css_selector("body > form > div > div > button").click()
