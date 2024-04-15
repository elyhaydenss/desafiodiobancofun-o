# Sistema Bancário Simplificado

Este é um sistema bancário simplificado implementado em Python. Ele permite criar usuários, filtrar usuários por CPF, criar contas associadas a usuários e realizar operações bancárias básicas, como depositar, sacar e verificar extratos de conta.

## Funcionalidades

- **Criar Usuário:** Permite criar novos usuários informando nome e CPF.
- **Filtrar Usuário:** Permite encontrar um usuário existente por CPF.
- **Criar Conta:** Permite associar uma conta a um usuário existente.
- **Depositar:** Permite fazer um depósito em uma conta existente.
- **Sacar:** Permite sacar dinheiro de uma conta existente.
- **Extrato:** Permite visualizar o extrato de uma conta existente.
- **Sair:** Permite sair do sistema.

## Instruções de Uso

1. Execute o arquivo `sistema_bancario.py` em um ambiente Python.
2. Escolha uma das opções do menu e siga as instruções para realizar a operação desejada.
3. Repita o processo conforme necessário ou selecione "q" para sair do programa.

## Funções Adicionais

- **`criar_usuario()`:** Cria um novo usuário informando nome e CPF.
- **`filtrar_usuario(usuarios, cpf)`:** Filtra um usuário existente por CPF.
- **`criar_conta(usuario)`:** Cria uma conta associada a um usuário existente.
- **`depositar(conta)`:** Realiza um depósito em uma conta existente.
- **`sacar(conta)`:** Realiza um saque em uma conta existente.
- **`ver_extrato(conta)`:** Exibe o extrato de uma conta existente.
