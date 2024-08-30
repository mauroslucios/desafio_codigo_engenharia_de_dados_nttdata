from datetime import datetime

# Inicialização das listas de clientes e suas contas
clientes = []


class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    

class Conta:
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor, cliente):
        self.saldo += valor
        data_hora = datetime.now()
        self.extrato.append(f"Depósito de R$ {valor:.2f} em {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        self.mostrar_identificacao_cliente(cliente)

    def sacar(self, valor, cliente):
        if valor > self.saldo:
            print(f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            data_hora = datetime.now()
            self.extrato.append(f"Saque de R$ {valor:.2f} em {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        self.mostrar_identificacao_cliente(cliente)

    def mostrar_extrato(self, cliente):
        print("\nExtrato de transações:")
        self.mostrar_identificacao_cliente(cliente)
        for transacao in self.extrato:
            print(transacao)
        data_hora = datetime.now()
        print(f"Saldo atual: R$ {self.saldo:.2f} em {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}\n")
    
    def verificar_saldo(self, cliente):
        data_hora = datetime.now()
        print(f"\nSaldo em {data_hora.strftime('%d/%m/%Y - %H:%M:%S')}: R$ {self.saldo:.2f}")
        self.mostrar_identificacao_cliente(cliente)

    def mostrar_identificacao_cliente(self, cliente):
        print(f"Nome: {cliente.nome}")
        print(f"CPF: {cliente.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero}\n")


class Cliente(Pessoa):
    def __init__(self, nome, cpf, email, agencia, numero):
        super().__init__(nome, cpf, email)
        self.conta = Conta(agencia, numero)


def cadastrar_cliente():
    print("Cadastro de cliente novo\n")
    cliente = Cliente(
        nome=input("Nome: "),
        email=input("Email: "),
        cpf=input("Cpf: "),
        agencia=input("Agência: "),
        numero=input("Número da Conta: ")
    )
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")


def buscar_cliente_por_numero_conta(numero_conta):
    for cliente in clientes:
        if cliente.conta.numero == numero_conta:
            return cliente
    print("Conta não encontrada!")
    return None


def main():
    while True:
        print("######## Menu de opções ########")
        print("1 - Cadastrar Cliente")
        print("2 - Depósito")
        print("3 - Saque")
        print("4 - Extrato")
        print("5 - Verificar saldo")
        print("6 - Sair\n")
        
        opcao = int(input("Escolha uma opção do menu ou digite 6 para sair: "))
        
        if opcao == 1:
            cadastrar_cliente()
                       
        elif opcao == 2:
            numero_conta = input("Digite o número da conta: ")
            cliente = buscar_cliente_por_numero_conta(numero_conta)
            if cliente:
                valor = float(input("Digite o valor do depósito: R$ "))
                cliente.conta.depositar(valor, cliente)
            print()
        
        elif opcao == 3:
            numero_conta = input("Digite o número da conta: ")
            cliente = buscar_cliente_por_numero_conta(numero_conta)
            if cliente:
                valor = float(input("Digite o valor do saque: R$ "))
                cliente.conta.sacar(valor, cliente)
            print()
        
        elif opcao == 4:
            numero_conta = input("Digite o número da conta: ")
            cliente = buscar_cliente_por_numero_conta(numero_conta)
            if cliente:
                cliente.conta.mostrar_extrato(cliente)
            print()
        
        elif opcao == 5:
            numero_conta = input("Digite o número da conta: ")
            cliente = buscar_cliente_por_numero_conta(numero_conta)
            if cliente:
                cliente.conta.verificar_saldo(cliente)
            print()
        
        elif opcao == 6:
            print("Obrigado por usar nossos serviços.")
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    main()
