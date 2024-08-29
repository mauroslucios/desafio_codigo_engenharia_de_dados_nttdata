from datetime import datetime
saldo = 0
extrato = []


def main():
    tentativas = 6
    data_hora = datetime.now()
    while (tentativas > 0):
        menu = "Menu de opções"
        print(menu.center(4, "#"))
        print("1 - verificar saldo")
        print("2 - depósito")
        print("3 - saque")
        print("4 - extrato")
        print("5 - sair")
        opcao = int(input("Escolha uma opção do menu:\n"))    
        if (opcao == 1):
            tentativas -= 1
            print(f"Seu saldo atual é de R$ {saldo:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 2):
            tentativas -= 1
            depositar()
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 3):
            tentativas -= 1
            sacar()
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 4):
            tentativas -= 1
            relatorio()
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 5):
            relatorio()
            print("Obrigado por usar nossos serviços.")
            print("Saindo do sistema...")
            break
        elif (tentativas == 0):
            print("Limite de tentativas atingido nesta sessão.")
            print(f"Você tem {tentativas} tentativa(s).")
            print("Saindo do sistema...")
            print()
            break
        else:
            tentativas -= 1
            print("Opção inválida!")


def depositar():
    global saldo
    print(f"Saldo atual R$ {saldo:.2f}")
    valor = float(input("Entre com o valor para depósito R$: "))
    saldo += valor 
    data_hora = datetime.now()
    extrato.append(f"Depósito de R$ {valor:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
    print(f"Valor depositado R$ {valor:.2f}")
    print(f"Seu saldo atual é de R$ {saldo:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")


def sacar():
    global saldo
    saque = float(input("Entre com o valor de saque R$ "))
    if (saque > saldo or saldo <= 0):
        print(f"Seu saldo atual é de R$ {saldo:.2f}. Saque não realizado!")
        print("Saldo insuficiente!")
    else:
        print(f"Saque realizado de R$ {saque:.2f} com sucesso")
        saldo = saldo - saque
        data_hora = datetime.now()
        print(f"Seu saldo atualizado é de R$ {saldo:.2f}.")
        extrato.append(f"Saque de R$ {saque:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")


def relatorio():
    global saldo
    data_hora = datetime.now()
    print("\nExtrato de transações:")
    for tot_extrato in extrato:
        print(tot_extrato)
    print(f"Saldo atual: R$ {saldo:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}\n")


if __name__ == "__main__":
    main()