from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bikeLight_add_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.page_title = (By.CLASS_NAME, "title")

    def adicionar_mochila_ao_carrinho(self):
        self.driver.find_element(*self.backpack_add_button).click()


    def adicionar_bicicleta_ao_carrinho(self):
        self.driver.find_element(*self.bikeLight_add_button).click()

    def obter_quantidade_carrinho(self):
        return self.driver.find_element(*self.cart_badge).text

    def obter_titulo_pagina(self):
        return self.driver.find_element(*self.page_title).text