from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_payment_section():
    driver = webdriver.Firefox()

    try:
        driver.get("https://itcareerhub.de/ru")
        driver.maximize_window()
        time.sleep(3)

        # Переходим в раздел "Способы оплаты"
        payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
        payment_link.click()
        time.sleep(3)

        # Делаем скриншот
        driver.save_screenshot("payment_section.png")

    finally:
        driver.quit()