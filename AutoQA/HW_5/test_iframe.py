from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iframe_text():

    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    wait = WebDriverWait(driver, 10)

    iframe = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )

    driver.switch_to.frame(iframe)

    text_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[2]"))
    )

    assert "semper posuere integer et senectus justo curabitur." in text_element.text

    driver.quit()