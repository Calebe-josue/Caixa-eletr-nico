from funções.conta import*
from funções.menu import*
from time import sleep
from funções.dados import*

arquivo = "dados_dos_clientes.json"
pessoa1= Conta('Calebe',1200)


if  not arquivo_existe(arquivo):
    criar_arquivo(arquivo,pessoa1.nome,pessoa1.saldo)


while True:
    sleep(2)
    clear_terminal()
    menu('CAIXA ELETRÔNICO')
    sleep(1)
    op('Ver Saldo','Depositar','Sacar','Ver histórico','Sair')
    esco= escolha('Digite sua opção')
    sleep(1)
    if esco==1:
        pessoa1.ver_saldo()
    elif esco==2:
        pessoa1.depositar()
    elif esco==3:
        pessoa1.sacar()
    elif esco==4:
        pessoa1.historico()
    elif esco==5:
        print('-----FIM DO PROGRAMA-----')
        break

