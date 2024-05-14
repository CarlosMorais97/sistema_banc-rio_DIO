menu = '''
########## MENU ##########

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Qual operação deseja realizar? '''

saldo = 0
deposito = 0
limite = 500
extrato = ""
numero_deposito = 0
numero_saques = 0
limite_saques = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            numero_deposito += 1
            print("\n")
            print(f"O valor depositado foi de R$ {valor:.2f}")
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida! Tente novamente.")

    elif opcao == 2:
        valor = float(input("Qual valor deseja sacar? "))
        if valor > 0:
            if numero_saques < limite_saques:
                if valor <= saldo:
                    if valor <= limite:
                        saldo -= valor
                        numero_saques += 1
                        print("\n")
                        print(f"O valor sacado foi de R$ {valor:.2f}")
                        extrato += f"Valor sacado: R$ {valor:.2f}\n"
                        print("\n")
                    else:
                        print("\n")
                        print("O valor digitado excede o limite, tente novamente.")
                        print("\n")
                else:
                    print("\n")
                    print("Saldo insuficiente!")
                    print("\n")
            else:
                print("\n")
                print("Você excedeu o limite de saques diários")
                print("\n")
        else:
            print("Operação inválida! O valor informado está incorreto.")

    elif opcao == 3:
        print("\n---------------- EXTRATO ----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo é: R$ {saldo:.2f}")
        print("-------------------------------------------")

    elif opcao == 0:
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("Agradecemos por utilizar nossos serviços, até a próxima!")