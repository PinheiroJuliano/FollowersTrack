# Comparador de Seguidores e Seguindo no Instagram

Este script em Python compara os usuários que você segue com aqueles que te seguem de volta no Instagram.

## Funcionalidade

1. Carrega dois arquivos JSON exportados do Instagram: um com a lista de **seguidores** e outro com a lista de **contas que você segue**.
2. Extrai os **nomes de usuário** (usernames) de cada arquivo.
3. Exibe o **total de pessoas que você segue** e o **total de seguidores**.
4. Compara os dois conjuntos e imprime os nomes dos usuários que você segue, mas que **não te seguem de volta**.

## Como Obter os Arquivos JSON

Para obter os arquivos JSON de seguidores e seguindo, siga os passos abaixo:

1. Acesse seu perfil do Instagram pelo navegador.
2. Clique em **Configurações** > **Privacidade e segurança** > **Download de dados**.
3. Solicite um download dos seus dados informando seu e-mail.
4. Você receberá um e-mail com um link para baixar um arquivo ZIP contendo todos os seus dados.
5. Extraia o arquivo ZIP e localize os arquivos JSON dentro da pasta `followers_and_following`.
6. Use o arquivo `followers_1.json` como `seguidores.json` e o arquivo `following.json` como `seguindo.json` (renomeie se necessário).

## Requisitos

- **Python**: Versão 3.6 ou superior
- **Arquivos**:
  - `followers_1.json`
  - `following.json`
  
### Estrutura Esperada dos Arquivos JSON

- **seguidores.json**: Lista de objetos com a chave `string_list_data`.
- **seguindo.json**: Objeto com a chave `relationships_following`, contendo uma lista com `string_list_data`.

## Como Rodar o Script

1. Coloque os arquivos `followers_1.json` e `following.json` na mesma pasta do script.
2. No terminal ou prompt de comando, navegue até o diretório do script.
3. Execute o script com o comando:

   ```bash
   python main.py
