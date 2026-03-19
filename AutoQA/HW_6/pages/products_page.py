from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    # локаторы товаров
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    # корзина
    cart_button = (By.CLASS_NAME, "shopping_cart_link")

    # действия
    def add_products_to_cart(self):
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()