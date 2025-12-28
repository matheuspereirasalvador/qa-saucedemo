import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    servico = Service(ChromeDriverManager().install())
    meu_driver = webdriver.Chrome(service=servico)
    meu_driver.maximize_window()
    meu_driver.implicitly_wait(5)

    yield meu_driver
    meu_driver.quit()