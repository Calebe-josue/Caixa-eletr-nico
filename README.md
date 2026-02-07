SIMULADOR DE CAIXA ELETRONICO EM PYTHON COM PERSISTENCIA DE DADOS EM JSON


MENU:
    1. Ver saldo
    2. Depositar dinheiro
    3. Sacar dinheiro
    4. Sair

FUNÇÃO:

    VER SALDO:
        Mostra o saldo na tela

    DEPOSITAR DINHEIRO:
        Pede valor
        Trata Erro
        Soma com saldo atual

    SACAR DINHEIRO:
        Pede valor
        Trata erro
        subtrai com saldo atual
        *NÃO PERMITE SACAR MAIS QUE O SALDO ATUAL

    SAIR:
        encerra algoritmo

DADOS:

    Persistencia em json

    FUNÇÕES:
        CRIAR_ARQUIVO:
            Cria um arquivo json

        LER_ARQUIVO:
            LE O ARQUIVO E RETORNA EM UM DICIONÁRIO
        
        ATUALIZAR_ARQUIVO:
            ATUALIZA O ARQUIVO COM BASE EM UM DICIONÁRIO
    
        ARQUIVO_EXISTE:
            Verifica se o arquivo existe, retornando valor booleano

ARQUIVO:
    A ideia do json é armazenar os dados do cliente e seu histórico de transações no banco.