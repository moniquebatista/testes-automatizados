from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.btn_add_carrinho = (By.XPATH, "//*[text() = 'Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class = 'shopping_cart_link']")
    def verificar_login_com_sucesso(self):
        self.verificar_elemento_existentente(self.titulo_pagina)

    def add_ao_carrinho (self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.btn_add_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)
