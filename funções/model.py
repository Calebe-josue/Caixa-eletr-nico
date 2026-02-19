import json
from funções.controller import*


def arquivo_existe(nome):
    try:
        with open(nome,'r') as f:
            return True
    except (FileNotFoundError, FileExistsError):
        return False
    


def criar_arquivo(nome,nome_cliente,valor):
    with open(nome,'w', encoding='utf-8') as arquivo:
        dados = {"nome":nome_cliente,
                 "saldo":valor,
                 "historico":[]
        }
        json.dump(dados,arquivo,indent=4)

def ler_arquivo(nome):
    with open(nome,'r', encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def atualizar_arquivo(nome,arq):
    with open(nome,'w',encoding='utf-8') as arquivo:
        json.dump(arq,arquivo,indent=4)
    


