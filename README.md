
# Comparador de Seguidores e Seguindo no Instagram

Este script em Python compara os usuários que você segue com aqueles que te seguem de volta no Instagram e registra o histórico das diferenças ao longo do tempo.

---

## Funcionalidades

1. Carrega dois arquivos JSON exportados do Instagram: um com a lista de **seguidores** e outro com a lista de **contas que você segue**.
2. Extrai os **nomes de usuário** (usernames) de cada arquivo.
3. Exibe:
   - Total de pessoas que você segue.
   - Total de seguidores.
   - Lista de usuários que **você segue, mas que não te seguem de volta**.
4. Salva essa lista em um arquivo `.json` dentro da pasta `Historico/`, com o nome baseado no timestamp atual.
5. Compara os **dois arquivos mais recentes** dentro da pasta `Historico/`.
6. Gera um novo arquivo chamado `lista_resultado.json` na pasta `Resultado/` contendo os **novos usuários que apareceram como "não te seguem de volta" em relação ao histórico anterior**.

---

## Como Obter os Arquivos JSON

1. Acesse seu perfil do Instagram pelo navegador.
2. Vá em **Configurações** > **Privacidade e segurança** > **Download de dados**.
3. Solicite o download informando seu e-mail.
4. Após receber o e-mail do Instagram, baixe e extraia o arquivo ZIP.
5. Localize os arquivos JSON na pasta `followers_and_following`.
6. Coloque esses arquivos na mesma pasta do script.

---

## Requisitos

- Python 3.6 ou superior
- Arquivos:
  - `followers_1.json` (lista de seguidores)
  - `following.json` (lista de contas que você segue)

---

## Como Rodar o Script

1. Coloque os arquivos `followers_1.json` e `following.json` na mesma pasta do script.
2. No terminal ou prompt de comando, navegue até o diretório do script.
3. Execute o comando:

```bash
python main.py
```

---

## Estrutura de Pastas Criadas

- `Historico/`: Armazena arquivos `.json` com as listas de quem você segue, mas que **não te segue de volta**, salvos com timestamp.
- `Resultado/`: Contém o arquivo `lista_resultado.json`, que mostra os **novos usuários que passaram a não te seguir de volta desde a última execução**.

