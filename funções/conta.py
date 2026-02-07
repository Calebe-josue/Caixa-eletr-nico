from funções.dados import*
from time import sleep


class Conta:
    def __init__(self,nome='Indefinido',saldo=0):
        self.nome = nome
        self.saldo = saldo

    
    def ver_saldo(self):
        arq=ler_arquivo("dados_dos_clientes.json")
        print(f'Seu saldo é de {arq["saldo"]} reais')
        

    def depositar(self):
        try:
            valor = float(input('Digite o valor que deseja depositar\n'))

        except (ValueError, KeyboardInterrupt):
            print('Erro, valor inválido!')
        
        else:
            arq = ler_arquivo('dados_dos_clientes.json')
            arq["saldo"]+=valor
            arq['historico'].append(f'deposito: {valor}')
            atualizar_arquivo("dados_dos_clientes.json",arq)
            print('Valor depositado com sucesso!')
            

    def sacar(self):
        try:
            valor = float(input('Digite o valor que deseja sacar\n'))
            arq = ler_arquivo('dados_dos_clientes.json')
            if valor > arq["saldo"]:
                print('Erro, valor sacado não pode ser maior que seu saldo!')
                return
            
        except (KeyboardInterrupt,ValueError):
            print('Erro, valor inváldio')

        else:
            try:
                confirmacao= str(input(f'Confirmar valor do saque de {valor}? S/N\n'))
                if confirmacao.lower()=='n':
                    print('Encerrando função...')
                elif confirmacao.lower()=='s':
                    arq["saldo"]-= valor
                    arq['historico'].append(f'saque: {valor}')
                    atualizar_arquivo("dados_dos_clientes.json",arq)
                else:
                    print('Erro, confirmação inválida')
            except:
                print('Erro no sistema')
            else:
                sleep(1)
                print("Saque efetuado com sucesso!")

    def historico(self):
        arq = ler_arquivo('dados_dos_clientes.json')
        lista= arq['historico']
        for i in range(0,len(lista)):
            print(f'- {lista[i]}')
            