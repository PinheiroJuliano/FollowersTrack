import os
import json
from datetime import datetime

def extrair_usernames(caminho_arquivo, chave_lista=None):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    if chave_lista:
        dados = dados[chave_lista]

    usernames = []
    for item in dados:
        if 'string_list_data' in item and item['string_list_data']:
            usernames.append(item['string_list_data'][0]['value'])
    return usernames

def salvar_json(lista, pasta, nome_arquivo):
    os.makedirs(pasta, exist_ok=True)
    caminho_completo = os.path.join(pasta, nome_arquivo)
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

def obter_dois_arquivos_mais_recentes(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.json')]
    arquivos.sort(reverse=True)  # baseado na timestamp no nome do arquivo
    if len(arquivos) >= 2:
        return os.path.join(pasta, arquivos[1]), os.path.join(pasta, arquivos[0])  # antigo, novo
    return None, None

def detectar_novos_nao_seguem_de_volta(arquivo_antigo, arquivo_novo):
    with open(arquivo_antigo, 'r', encoding='utf-8') as f1, open(arquivo_novo, 'r', encoding='utf-8') as f2:
        lista_antiga = set(json.load(f1))
        lista_nova = set(json.load(f2))

    novos_nao_seguem = sorted(list(lista_nova - lista_antiga))
    return {'novos_nao_seguem_de_volta': novos_nao_seguem}

def main():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    caminho_following = os.path.join(pasta_atual, 'following.json')
    caminho_followers = os.path.join(pasta_atual, 'followers_1.json')

    seguindo = set(extrair_usernames(caminho_following, chave_lista='relationships_following'))
    seguidores = set(extrair_usernames(caminho_followers))

    print(f"Total seguindo: {len(seguindo)}")
    print(f"Total seguidores: {len(seguidores)}\n")

    nao_seguem_de_volta = sorted(seguindo - seguidores)

    print(f"Usuários que você segue, mas que não te seguem de volta ({len(nao_seguem_de_volta)}):")
    for nome in nao_seguem_de_volta:
        print(nome)

    # Salvar histórico
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nome_arquivo = f'{timestamp}.json'
    pasta_historico = os.path.join(pasta_atual, 'Historico')
    salvar_json(nao_seguem_de_volta, pasta_historico, nome_arquivo)

    # Comparar com o anterior
    antigo, novo = obter_dois_arquivos_mais_recentes(pasta_historico)
    if antigo and novo:
        resultado = detectar_novos_nao_seguem_de_volta(antigo, novo)
        pasta_resultado = os.path.join(pasta_atual, 'Resultado')
        salvar_json(resultado, pasta_resultado, 'lista_resultado.json')

if __name__ == '__main__':
    main()
