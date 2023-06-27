import pytest
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        #add mochila ao carrinho
        home_page.add_ao_carrinho("Sauce Labs Backpack")

        #vericando se o item foi adc
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_no_carrinho("Sauce Labs Backpack")

        #voltar para tela de produtos
        carrinho_page.clicar_continuar_comprando()

        #add mais um produto ao carrinho
        home_page.add_ao_carrinho("Sauce Labs Bike Light")

        #verificando os 2 produtos no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_no_carrinho("Sauce Labs Backpack")
        carrinho_page.verificar_produto_no_carrinho("Sauce Labs Bike Light")

