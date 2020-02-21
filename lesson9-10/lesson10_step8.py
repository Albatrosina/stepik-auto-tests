from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
book_btn = driver.find_element_by_css_selector("#book").click()

x = driver.find_element_by_css_selector("#input_value").text
answer = driver.find_element_by_css_selector("#answer").send_keys(calc(x))
submit_btn = driver.find_element_by_css_selector("body > form > div > div > button").click()

time.sleep(5)
driver.quit()