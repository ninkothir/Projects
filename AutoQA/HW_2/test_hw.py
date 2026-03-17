import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_payment_section(driver):
    driver.get("https://itcareerhub.de/ru/")
    driver.maximize_window()
    time.sleep(3)

    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    time.sleep(3)

    driver.save_screenshot("payment_section.png")