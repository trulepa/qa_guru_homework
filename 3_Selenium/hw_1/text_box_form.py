import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_no_email():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(0)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Иванов Иван Иванович")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("qe@mail.ru")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(0)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")
        assert result_box.text, "Блок пуст, форма не отправилась?"

        # Получаем нужную строку из блока
        buffer = result_box.text.split("\n")
        email_line = None
        for line in buffer:
            if line.startswith("Email:"):
                email_line = line
                break
        print(email_line + "\n")

        assert email_line is not None, "В блоке нет строки с Email"

        # Проверяем, что в блоке результата появился введенный текст
        email_value = email_line.split(":",1)[1].strip()
        print(email_value)

        assert email_value == "", f"Ожидался пустой email, но получено: '{email_value}'"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()

def test_current_address():
    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(0)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле currentAddress по его ID и вводим текст
        current_field = driver.find_element(By.ID, "currentAddress")
        current_field.send_keys("Москва ул.Фадеева д.13 кв.5")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(0)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")
        if len(result_box.text) == 0:
            assert False, "Итоговый блок не получен, отработала валидация"

        # Обработаем данные в блоке
        print(result_box.text + ("\n"))
        massive = result_box.text.split("\n")

        # Проверяем, что в блоке результата появился введенный текст
        if len(massive[2]) == 17:
            assert False, "Поле currentAddress не заполнено"
        elif len(massive[2]) > 17:
            print("В поле currentAddress что-то ввели")
        else:
            assert False, "Тест сломан, всё пропало!"

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()
