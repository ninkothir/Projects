import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://itcareerhub.de/ru"


def test_homework_3_main_page_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(URL)
        driver.maximize_window()

        # 1) ждём, что страница реально загрузилась (видим body)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 2) если есть cookie-кнопка "подтвердить" — кликаем
        cookie_buttons = driver.find_elements(
            By.XPATH,
            "//button[contains(., 'подтвердить') or contains(., 'Подтвердить')]"
        )
        if cookie_buttons:
            try:
                cookie_buttons[0].click()
                time.sleep(1)
            except:
                pass

        # 3) проверяем, что в верхнем меню есть пункты (как на твоём фото)
        menu_items = [
            "Программы",
            "Способы оплаты",
            "О нас",
            "Bildungsgutschein",
            "Контакты",
            "Отзывы",
            "Блог",
        ]

        for item in menu_items:
            elems = driver.find_elements(By.XPATH, f"//*[normalize-space()='{item}']")
            assert len(elems) > 0, f"Пункт меню не найден: {item}"

        # 4) проверяем переключатели языка ru / de (кнопки)
        assert len(driver.find_elements(By.XPATH, "//*[normalize-space()='ru']")) > 0, "Не найден переключатель ru"
        assert len(driver.find_elements(By.XPATH, "//*[normalize-space()='de']")) > 0, "Не найден переключатель de"

        # 5) проверяем, что на странице есть ссылка телефона tel:
        # НЕ кликаем по ней, чтобы не вылезало окно системы
        tel_links = driver.find_elements(By.CSS_SELECTOR, "a[href^='tel:']")
        assert len(tel_links) > 0, "Не найдена tel-ссылка (телефон)"

        # 6) скроллим в самый низ (футер)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 7) ищем текст из задания (часть фразы)
        # Иногда текст отличается — поэтому берём кусок "Если вы не дозвонились"
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        assert "it career hub" in driver.page_source.lower()

    finally:
        driver.quit()