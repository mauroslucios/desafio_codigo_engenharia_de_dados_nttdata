# Inicialização do saldo e lista de transações
saldo = 0
transacoes = []


def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        transacoes.append(f"Saque de R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente para realizar o saque.")


def depositar(valor):
    global saldo
    saldo += valor
    transacoes.append(f"Depósito de R${valor:.2f}")
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")


def verificar_saldo():
    print(f"Seu saldo atual é: R${saldo:.2f}")


def relatorio():
    print("\nRelatório de Transações:")
    for transacao in transacoes:
        print(transacao)
    print(f"Saldo atual: R${saldo:.2f}\n")


def main():
    while True:
        print("\nBem-vindo ao Banco Python!")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Verificar Saldo")
        print("4. Relatório")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para sacar: R$"))
            sacar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para depositar: R$"))
            depositar(valor)
        elif opcao == "3":
            verificar_saldo()
        elif opcao == "4":
            relatorio()
        elif opcao == "5":
            print("Obrigado por usar o Banco Python. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
