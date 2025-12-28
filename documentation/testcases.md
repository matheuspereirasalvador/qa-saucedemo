# Suite de Testes: Login SauceDemo

## CT01 - Login com Usuário Padrão (Caminho Feliz)
**Objetivo:** Verificar se um usuário ativo consegue acessar a loja.

**Técnica:** Particionamento de Equivalência (Classe Válida).

**Passos:**
1. Inserir usuário: `standard_user`
2. Inserir senha: `secret_sauce`
3. Clicar no botão Login.

**Resultado Esperado:** Redirecionamento para a página de produtos (/inventory.html).

## CT02 - Tentativa de Login com Usuário Bloqueado
**Objetivo:** Verificar se o sistema impede acesso de contas travadas.

**Técnica:** Particionamento de Equivalência (Classe Inválida Específica).

**Passos:**
1. Inserir usuário: `locked_out_user`
2. Inserir senha: `secret_sauce`
3. Clicar no botão Login.
   
**Resultado Esperado:** Exibir mensagem de erro: "Epic sadface: Sorry, this user has been locked out."

## CT03 - Tentativa de Login com Credenciais Inválidas
**Objetivo:** Garantir segurança contra dados incorretos.

**Técnica:** Particionamento de Equivalência (Classe Inválida Genérica).

**Passos:**
1. Inserir usuário: `standard_user`
2. Inserir senha: `senha_errada_123`
3. Clicar no botão Login.

**Resultado Esperado:** Exibir mensagem de erro: "Epic sadface: Username and password do not match any user in this service"

