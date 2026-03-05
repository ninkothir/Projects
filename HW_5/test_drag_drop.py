from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_and_drop():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    # 1) Закрываем cookie (если появится)
    try:
        btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Соглашаюсь')]"))
        )
        btn.click()
    except:
        pass

    # 2) Переходим в iframe
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
    driver.switch_to.frame(iframe)

    # 3) Ждём, пока появятся картинки и корзина
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
    trash = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    # иногда помогает прокрутка
    driver.execute_script("arguments[0].scrollIntoView(true);", trash)

    # 4) Drag & Drop (более стабильная цепочка)
    actions = ActionChains(driver)
    actions.click_and_hold(images[0]).pause(0.3).move_to_element(trash).pause(0.3).release().perform()

    # 5) Ждём результат: в корзине должна появиться 1 картинка
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)

    trash_images = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    gallery_images = driver.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(trash_images) == 1
    assert len(gallery_images) == 3

    driver.quit()