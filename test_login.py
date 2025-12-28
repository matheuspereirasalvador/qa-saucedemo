from pages.login_page import LoginPage

def test_login_sucesso(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.fazer_login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_bloqueado(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.fazer_login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.obter_mensagem_erro()


def test_login_invalido(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.fazer_login("invalid_user", "secret_sauce")
    assert "do not match" in login_page.obter_mensagem_erro()