# 🧪 QA Automation - SauceDemo Project

![Build Status](https://github.com/matheuspereirasalvador/qa-saucedemo/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)

Projeto de automação de testes End-to-End (E2E) para o e-commerce [SauceDemo](https://www.saucedemo.com/), focado em demonstrar conhecimentos avançados em arquitetura de testes e CI/CD.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework de Teste:** Pytest
* **Motor de Browser:** Selenium WebDriver
* **Padrão de Projeto:** Page Object Model (POM)
* **CI/CD:** GitHub Actions (Pipeline automatizado)
* **Relatórios:** Pytest-HTML

## 📂 Estrutura do Projeto

O projeto segue o padrão **Page Object Model** para garantir manutenibilidade e escalabilidade:

* `pages/`: Classes que mapeiam os elementos e ações de cada página (Login, Inventário).
* `tests/`: Arquivos de teste focados na regra de negócio e validações.
* `conftest.py`: Configurações globais (Fixtures) e setup do WebDriver.
* `.github/workflows/`: Configuração do Pipeline de CI/CD.

## ⚙️ Cenários Cobertos

1.  **Login:**
    * ✅ Login com sucesso (Caminho Feliz).
    * 🔒 Tentativa de login com usuário bloqueado.
    * ❌ Tentativa de login com credenciais inválidas.
2.  **Carrinho de Compras:**
    * 🛒 Adicionar múltiplos itens ao carrinho e validar contagem.

## 🛠️ Como Rodar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/matheuspereirasalvador/qa-saucedemo.git](https://github.com/matheuspereirasalvador/qa-saucedemo.git)
    cd qa-saucedemo
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute os testes:**
    ```bash
    # Rodar todos os testes
    pytest

    # Rodar gerando relatório HTML
    pytest --html=relatorio.html
    ```

---
Desenvolvido por **Matheus Pereira Salvador** para portfólio de QA.
