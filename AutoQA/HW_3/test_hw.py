import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://itcareerhub.de/ru/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_homework_3_main_page_elements(driver):
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    driver.maximize_window()

    # ждём загрузку страницы
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # закрываем cookie (если есть)
    cookie_buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in cookie_buttons:
        text = button.text.strip().lower()
        if "подтвердить" in text or "accept" in text or "agree" in text:
            try:
                button.click()
                time.sleep(1)
                break
            except Exception:
                print("Куки не закрылись")

    # проверка логотипа / текста сайта
    assert "it career hub" in driver.page_source.lower(), "Не найден текст сайта"

    # проверка меню
    assert len(driver.find_elements(By.LINK_TEXT, "Программы")) > 0, "Нет 'Программы'"
    assert len(driver.find_elements(By.LINK_TEXT, "Способы оплаты")) > 0, "Нет 'Способы оплаты'"
    assert len(driver.find_elements(By.LINK_TEXT, "О нас")) > 0, "Нет 'О нас'"
    assert len(driver.find_elements(By.LINK_TEXT, "Отзывы")) > 0, "Нет 'Отзывы'"

    # проверка "Новости" (частично)
    assert "новост" in driver.page_source.lower(), "Нет 'Новости'"

    # проверка языков
    assert "ru" in driver.page_source.lower(), "Нет переключателя ru"
    assert "de" in driver.page_source.lower(), "Нет переключателя de"

    # проверка ссылки телефона
    tel_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="tel:"]')
    assert len(tel_links) > 0, "Нет tel-ссылки"

