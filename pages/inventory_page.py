from selenium.webdriver.common.by import By
# IMPORTS NOVOS PARA O WAIT EXPLICITO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bike_light_add_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.page_title = (By.CLASS_NAME, "title")

    def adicionar_mochila(self):
        self.driver.find_element(*self.backpack_add_button).click()

    def adicionar_bike_light(self):
        self.driver.find_element(*self.bike_light_add_button).click()

    def obter_quantidade_carrinho(self):
        wait = WebDriverWait(self.driver, 10)

        elemento = wait.until(EC.visibility_of_element_located(self.cart_badge))

        return elemento.text

    def obter_titulo_pagina(self):
        return self.driver.find_element(*self.page_title).text