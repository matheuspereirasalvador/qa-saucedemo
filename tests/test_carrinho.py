from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_adicionar_item_ao_carrinho(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.fazer_login("standard_user", "secret_sauce")

    inventory_page.adicionar_mochila()
    assert "1" == inventory_page.obter_quantidade_carrinho()

    inventory_page.adicionar_luz_bicicleta()
    assert "2" == inventory_page.obter_quantidade_carrinho()