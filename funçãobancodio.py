# Função para criar um novo usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    return {"nome": nome, "cpf": cpf}

# Função para filtrar um usuário por CPF
def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar uma conta para um usuário existente
def criar_conta(usuario):
    saldo = float(input("Informe o saldo inicial da conta: "))
    limite = float(input("Informe o limite da conta: "))
    return {"usuario": usuario, "saldo": saldo, "limite": limite, "extrato": "", "numero_saques": 0}

# Função para depositar dinheiro na conta
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para sacar dinheiro da conta
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para ver o extrato da conta
def ver_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Menu de opções
menu = """

[u] Criar Usuário
[f] Filtrar Usuário
[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
conta = None
LIMITE_SAQUES = 3

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "u":
        usuarios.append(criar_usuario())
    elif opcao == "f":
        cpf = input("Digite o CPF do usuário que deseja filtrar: ")
        usuario = filtrar_usuario(usuarios, cpf)
        if usuario:
            print("Usuário encontrado:")
            print(usuario)
        else:
            print("Usuário não encontrado.")
    elif opcao == "c":
        cpf = input("Digite o CPF do usuário para criar a conta: ")
        usuario = filtrar_usuario(usuarios, cpf)
        if usuario:
            conta = criar_conta(usuario)
            print("Conta criada com sucesso!")
        else:
            print("Usuário não encontrado.")
    elif opcao == "d":
        if conta:
            depositar(conta)
        else:
            print("Crie uma conta antes de fazer um depósito.")
    elif opcao == "s":
        if conta:
            sacar(conta)
        else:
            print("Crie uma conta antes de fazer um saque.")
    elif opcao == "e":
        if conta:
            ver_extrato(conta)
        else:
            print("Crie uma conta antes de verificar o extrato.")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
