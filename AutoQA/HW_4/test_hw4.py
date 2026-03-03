import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_text_change():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://uitestingplayground.com/textinput")

        # находим input
        input_field = wait.until(
            EC.presence_of_element_located((By.ID, "newButtonName"))
        )

        input_field.clear()
        input_field.send_keys("ITCH")

        # находим кнопку
        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        # проверяем, что текст кнопки изменился
        assert button.text == "ITCH"

    finally:
        driver.quit()


def test_loading_images():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # берём только "содержательные" картинки (у которых есть alt)
        def get_images_with_alt(d):
            imgs = d.find_elements(By.TAG_NAME, "img")
            return [img for img in imgs if (img.get_attribute("alt") or "").strip()]

        # ждём, пока таких картинок станет минимум 3
        wait.until(lambda d: len(get_images_with_alt(d)) >= 3)

        # ждём, пока alt у третьей станет именно "award"
        wait.until(lambda d: get_images_with_alt(d)[2].get_attribute("alt") == "award")

        images = get_images_with_alt(driver)
        alt_value = images[2].get_attribute("alt")

        assert alt_value == "award"

    finally:
        driver.quit()