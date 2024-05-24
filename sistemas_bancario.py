import textwrap

def menu():
    menu = '''\n
    ############### MENU ###############
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuario
    [5]\tNova Conta
    [6]\tListar Contas
    [0]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        print("\n=== Depósito efetuado com sucesso! ===\n")
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print("@@@ Operação inválida! Tente novamente.@@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if numero_saques < limite_saques:
            if valor <= saldo:
                if valor <= limite:
                    saldo-= valor
                    numero_saques += 1
                    print("\n=== Saque efetuado com sucesso! ===\n")
                    extrato += f"Saque:\t\tR${valor:.2f}\n"
                else:
                    print("\n@@@ O valor digitado excede o limite! @@@")
            else:
                print("\n@@@ Saldo insucifiente! @@@\n")    
        else:
            print("\n@@@ Usuário excedeu o limite de saques diários! @@@")
    else: 
        print("\n@@@ Operação inválida! O valor informado é inválido. @@@")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo:\t\tR$ {saldo:.2f}")
    print("============================")

def criar_usuarios(usuarios):
    cpf = input("Informe o CPF (somente os números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ CPF já cadastrado! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n === Contra criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, criação de conta encerrada! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Qual valor deseja depositar? "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Qual valor você deseja sacar? "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "4":
            criar_usuarios(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
           print("Operação inválida, por favor selecione novamente a operação desejada.")

main()