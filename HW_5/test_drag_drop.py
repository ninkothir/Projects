from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 15)

    # закрываем cookie, если появится
    try:
        agree_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Соглашаюсь') or contains(., 'Agree')]")
            )
        )
        agree_btn.click()
    except Exception:
        pass

    # переходим в iframe
    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame"))
    )
    driver.switch_to.frame(iframe)

    # ждём появления картинок и корзины
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li"))
    )
    trash = wait.until(
        EC.presence_of_element_located((By.ID, "trash"))
    )

    first_image = images[0]

    # прокрутка к корзине
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", trash)

    # более стабильный drag and drop через offset
    actions = ActionChains(driver)
    actions.click_and_hold(first_image).pause(0.5).move_to_element(trash).pause(0.5).release().perform()

    # ждём результата
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)

    trash_images = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    gallery_images = driver.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_images) == 1
    assert len(gallery_images) == 3