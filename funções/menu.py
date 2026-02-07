import os
from time import sleep
def clear_terminal():
    if os.name=='nt':
        sleep(1)
        os.system('cls')
    else:
        sleep(1)
        os.system('clear')
    

def menu(nome):
    print('-='*20)
    print(f'{nome}\n')



def op(*lista):
    for k,v in enumerate(lista):
        print(f'{k+1} - {v}')
    

def escolha(frase):
    try:
        valor = int(input(f'\n{frase}\n'))
    except (ValueError, KeyboardInterrupt):
        print('Valor inválido')
    else:
        return valor