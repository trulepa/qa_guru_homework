import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://qa-guru.github.io/one-page-form/text-box.html"
driver =  webdriver.Chrome()
# locator = {
#     "full_name_locator": "userName",
#     "email_locator": "userEmail",
#     "submit_button_locator": "submit",
#     "result_box_locator": "output"
#     }
result_line_name = {
    "full_name": "Name:",
    "Email": "Email:",
    "current_address": "Current Address :",
    "permananet_address": "Permananet Address :"
}

class TestSuite:

    full_name_locator = (By.ID, "userName")
    email_locator = (By.ID, "userEmail")
    submit_button_locator = (By.ID, "submit")
    result_box_locator = (By.ID, "output")

    def __init__(self, url, driver, result_line_name):
        self.url = url # "https://qa-guru.github.io/one-page-form/text-box.html"
        self.driver = driver # driver = webdriver.Chrome()
        self.result_line_name = result_line_name

    # Запуск браузера и открытие страницы
    def set_up(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()
        time.sleep(1)  # Пауза, чтобы визуально заметить открытие

    # Находим поле по его ID и вводим текст
    def search_fill_fields(self, send_keys):
        field = self.driver.find_element(*self.full_name_locator)
        field.send_keys(send_keys)

    # Находим кнопку по ее ID и кликаем
    def click_submit(self):
        submit_button = driver.find_element(*self.submit_button_locator)
        submit_button.click()
        time.sleep(2)  # Пауза, чтобы визуально заметить открытие

    # Находим блок с отправленными данными
    def search_result_box(self):
        result_box = driver.find_element(*self.result_box_locator)
        assert result_box.text, "Блок пуст, форма не отправилась?"
        return result_box

    # Получаем нужную строку из блока
    def get_sring(self, result_box, line_name):
        buffer = result_box.text.split("\n")

        current_line = None # для проверки
        for line in buffer:
            if line.startswith(line_name):
                current_line = line
                break
        print(current_line + "\n")

        assert current_line is not None, f"В блоке нет строки с {line_name}"
        return current_line

    # Проверяем, что в блоке результата появился введенный текст
    def empty_input(self, current_line):
        current_value = current_line.split(":", 1)[1].strip()
        print(current_value)

        assert current_value == "", f"Ожидалась пустая строка, но получено: '{current_value}'"
        print("Тест успешно пройден!")
        return current_line

    # Закрытие браузера в любом случае
    def teardown(self):
        self.driver.quit()

    # Проверка ввода пустой строки в поле
    def empty_full_name(self):
        try:
            empty_test.set_up()
            empty_test.search_fill_fields("")
            empty_test.click_submit()
            result_box = empty_test.search_result_box()
            current_line = empty_test.get_sring(result_box, self.result_line_name["full_name"])
            empty_test.empty_input(current_line)

        except AssertionError as error:
            print(f"Тест не пройден!: {error}")
            raise

        finally:
            # 5. Закрытие браузера в любом случае
            empty_test.teardown()


empty_test = TestSuite(url, driver, result_line_name)
empty_test.empty_full_name()
