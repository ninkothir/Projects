from HW_6.pages.login_page import LoginPage
from HW_6.pages.products_page import ProductsPage
from HW_6.pages.cart_page import CartPage
from HW_6.pages.checkout_page import CheckoutPage
from HW_6.pages.overview_page import OverviewPage


def test_checkout(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    # 1. открыть сайт
    login_page.open()

    # 2. логин
    login_page.login("standard_user", "secret_sauce")

    # 3. добавить товары
    products_page.add_products_to_cart()

    # 4. перейти в корзину
    products_page.go_to_cart()

    # 5. checkout
    cart_page.click_checkout()

    # 6. заполнить форму
    checkout_page.fill_form("Nina", "Test", "12345")
    checkout_page.click_continue()

    # 7. получить total
    total = overview_page.get_total_price()

    # 8. проверка
    assert total == "Total: $58.29"