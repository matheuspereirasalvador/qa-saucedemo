import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Rodar em modo headless")

@pytest.fixture()
def driver(request):
    servico = Service(ChromeDriverManager().install())
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    meu_driver = webdriver.Chrome(service=servico, options=options)
    meu_driver.maximize_window()
    meu_driver.implicitly_wait(5)

    yield meu_driver
    meu_driver.quit()