# Caixa Eletrônico

Simulador de Caixa Eletrônico desenvolvido em **Python**, executado via
terminal, que permite realizar operações bancárias como consulta de
saldo, depósito, saque e visualização de histórico, com persistência de
dados em arquivo **JSON**.

Projeto criado com foco em prática de lógica de programação, organização
de código em módulos e manipulação de arquivos.

------------------------------------------------------------------------

## Objetivo do Projeto

-   Praticar estrutura de menus interativos
-   Aplicar organização modular em Python
-   Trabalhar com persistência de dados usando JSON
-   Implementar regras básicas de negócio

------------------------------------------------------------------------

## Funcionalidades

-    Consultar saldo
-    Realizar depósito
-    Realizar saque
-    Visualizar histórico de transações
-    Armazenamento de dados em JSON
-    Interface interativa via terminal

------------------------------------------------------------------------

## Estrutura do Projeto

    Caixa-eletr-nico/
    ├── funções/
    │   ├── conta.py              # Regras da conta (saldo, saque, depósito, histórico)
    │   ├── dados.py              # Leitura e escrita no arquivo JSON
    │   └── menu.py               # Interface e exibição do menu
    ├── .gitignore
    ├── dados_dos_clientes.json   # Persistência dos dados
    ├── main.py                   # Arquivo principal (inicialização do sistema)
    └── README.md

------------------------------------------------------------------------

## Como Executar

``` bash
git clone https://github.com/Calebe-josue/Caixa-eletr-nico.git
cd Caixa-eletr-nico
python main.py
```

> É necessário ter Python 3 instalado.

------------------------------------------------------------------------

## Tecnologias Utilizadas

-   Python 3
-   JSON
-   Execução via terminal

------------------------------------------------------------------------

## Regras Implementadas

-   Não permite saque maior que o saldo disponível
-   Atualiza saldo automaticamente após operações
-   Mantém histórico das transações
-   Dados persistem mesmo após encerrar o programa

------------------------------------------------------------------------

## Autor

Desenvolvido por **Calebe Josué**
