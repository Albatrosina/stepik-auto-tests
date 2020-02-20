from selenium import webdriver
import time
import unittest


class TestForm(unittest.TestCase):
    def test_first_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        self.fname = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Dan")
        self.lname = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Kel")
        self.email = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("test@test.tt")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",  welcome_text)

    def test_second_reqistration(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        self.fname = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Dan")
        self.lname = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Kel")
        self.email = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("test@test.tt")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()