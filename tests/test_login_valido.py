
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        # fazer login
        login_page.fazer_login("standard_user", "secret_sauce")

        # verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()



