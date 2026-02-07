# 🏧 Caixa Eletrônico

Simulador de Caixa Eletrônico desenvolvido em **Python**, executado via
terminal, que permite realizar operações bancárias como consulta de
saldo, depósito, saque e visualização de histórico, com persistência de
dados em arquivo **JSON**.

Este projeto foi criado com foco em prática de lógica de programação,
manipulação de dados e organização de código.

------------------------------------------------------------------------

## 🎯 Objetivo do Projeto

O objetivo deste projeto é praticar:

-   Estrutura de menus interativos no terminal
-   Manipulação de arquivos JSON
-   Controle de fluxo (condições e loops)
-   Organização de código em módulos
-   Simulação de regras básicas de negócio

------------------------------------------------------------------------

## ⚙️ Funcionalidades

-   💰 Consultar saldo
-   ➕ Realizar depósito
-   ➖ Realizar saque
-   📜 Visualizar histórico de transações
-   📄 Armazenamento de dados em JSON
-   🖥️ Interface interativa via terminal
-   🔄 Atualização automática do saldo após operações

------------------------------------------------------------------------

## 🧠 Estrutura do Projeto

    Caixa-eletronico/
     ├─ main.py
     ├─ controller.py
     ├─ repository.py
     ├─ model.py
     ├─ dados.json
     ├─ .gitignore
     └─ README.md

------------------------------------------------------------------------

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

``` bash
git clone https://github.com/Calebe-josue/Caixa-eletr-nico.git
```

### 2️⃣ Entre na pasta do projeto

``` bash
cd Caixa-eletr-nico
```

### 3️⃣ Execute o programa

``` bash
python main.py
```

> ⚠️ É necessário ter o **Python 3** instalado.

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   🐍 Python 3
-   📄 JSON para armazenamento de dados
-   💻 Execução via terminal

------------------------------------------------------------------------

## 📌 Regras de Negócio Implementadas

-   Não é possível sacar valor maior que o saldo disponível
-   O saldo é atualizado após cada operação
-   O histórico registra as movimentações realizadas
-   Os dados permanecem salvos mesmo após encerrar o programa

------------------------------------------------------------------------


## 👨‍💻 Autor

Desenvolvido por **Calebe Josué**
