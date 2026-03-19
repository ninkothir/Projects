from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iframe_text(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    paragraphs = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "p"))
    )

    target_text = "semper posuere integer et senectus justo curabitur."

    assert any(target_text in p.text for p in paragraphs)