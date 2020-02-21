from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')

input1 = driver.find_element_by_css_selector("input[name=firstname]")
input1.send_keys("Dan")
input2 = driver.find_element_by_css_selector("input[name=lastname]")
input2.send_keys("Kel")
input3 = driver.find_element_by_css_selector("input[name=email]")
input3.send_keys("test@test.tt")
txt_file = driver.find_element_by_css_selector("#file").send_keys(file_path)
submit_btn = driver.find_element_by_css_selector("body > div > form > button").click()

time.sleep(5)

driver.quit()