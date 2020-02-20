import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
x_val = browser.find_element_by_css_selector("#input_value").text
res = calc(x_val)
ans = browser.find_element_by_css_selector("#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);",ans)
ans.send_keys(res)
cb = browser.find_element_by_css_selector("#robotCheckbox").click()
rb = browser.find_element_by_css_selector("#robotsRule").click()
submit_btn = browser.find_element_by_css_selector("body > div > form > button").click()
time.sleep(10)
browser.quit()
