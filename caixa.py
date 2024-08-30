from datetime import datetime
saldo = 0
extrato = []


def main():
    tentativas = 6
    while (tentativas > 0):
        menu = "Menu de opções"
        print(menu.center(4, "#"))
        print("1 - Cadastrar Cliente")
        print("2 - Depósito")
        print("3 - Saque")
        print("4 - Extrato")
        print("5 - Verificar saldo")
        print("6 - Sair\n")
        opcao = int(input("Escolha uma opção do menu ou digite 6 para sair:"))
        if (opcao == 1):
            cadastrar_cliente()
                       
        elif (opcao == 2):
            depositar()
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 3):
            sacar()
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 4):
            relatorio()
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
            print(f"Você ainda tem {tentativas} tentativa(s).")
            print()
        elif (opcao == 5):
            verificar_saldo()
            
        elif (opcao == 6):
            print("Obrigado por usar nossos serviços.")
            print("Saindo do sistema...")
            print()
            break
        else:
            print("Opção inválida!")


class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    

class Conta:
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo


class Cliente(Pessoa, Conta):
    def __init__(self, nome, cpf, email, agencia, numero, saldo):
        Pessoa.__init__(self, nome, cpf, email)
        Conta.__init__(self, agencia, numero, saldo)


def cadastrar_cliente():
    print("Cadastro de cliente novo\n")
    return Cliente(
        nome=input("Nome: "),
        email=input("Email:"),
        cpf=input("Cpf: "),
        agencia=input("Agência: "),
        numero=input("Número Conta: "),
        saldo=depositar()

    )


def depositar():
    global saldo
    print(f"Saldo atual R$ {saldo:.2f}")
    valor = float(input("Entre com o valor para depósito R$: "))
    saldo += valor 
    data_hora = datetime.now()
    extrato.append(f"Depósito de R$ {valor:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
    print(f"Valor depositado R$ {valor:.2f}")
    print(f"Seu saldo atual é de R$ {saldo:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
    return main()


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


def verificar_saldo():
    global saldo
    data_hora = datetime.now()
    print(f"\nSaldo em {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}\n")
    print(f"Saldo atual: R$ {saldo:.2f} DATA: {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}\n")


if __name__ == "__main__":
    main()