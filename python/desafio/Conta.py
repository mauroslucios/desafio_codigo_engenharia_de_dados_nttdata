from abc import ABC, abstractmethod
from datetime import datetime
import pytz


# Interface Conta com métodos abstratos
class Conta(ABC):
    
    def __init__(self, agencia, numero, cliente, saldo_inicial=0):
        """Inicializa a conta com agência, número, cliente e saldo inicial."""
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo_inicial
        self._historico = []
        self._saques_hoje = 0

    @abstractmethod
    def sacar(self, valor):
        """Método abstrato de saque que será implementado pelas subclasses."""
        pass

    @abstractmethod
    def depositar(self, valor):
        """Método abstrato de depósito que será implementado pelas subclasses."""
        pass

    def adicionar_historico(self, acao):
        data_hora_utc = datetime.now(pytz.timezone("America/Sao_Paulo"))
        """Adiciona uma ação ao histórico de transações."""
        self._historico.append(f"{acao} em {data_hora_utc.strftime('%d/%m/%Y - %H:%M:%S')} UTC")

    def exibir_historico(self):
        """Exibe o histórico de transações."""
        print("Histórico de ações:")
        for acao in self._historico:
            print(acao)

    def exibir_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual: R$ {self._saldo:.2f}")

    def info_conta(self):
        """Exibe informações da conta e do cliente."""
        print(f"\nAgência: {self._agencia}")
        print(f"Número da Conta: {self._numero}")
        print(f"Cliente: {self._cliente.nome} ({self._cliente.tipo_cliente})")
        print(f"Documento: {self._cliente.documento}\n")


# Classe Cliente que representa o cliente da conta (Pessoa Física ou Jurídica)
class Cliente:
    def __init__(self, nome, documento, email, telefone, tipo_cliente):
        """Inicializa um cliente com nome, documento (CPF ou CNPJ) e tipo de cliente."""
        self.nome = nome
        self.documento = documento
        self.email = email
        self.telefone = telefone
        self.tipo_cliente = tipo_cliente


# Classe ContaCorrente implementando a interface Conta
class ContaCorrente(Conta):
    LIMITE_SAQUE_DIA = 3
    LIMITE_VALOR_SAQUE = 100000

    def __init__(self, agencia, numero, cliente, saldo_inicial=0):
        """Inicializa uma Conta Corrente com agência, número, cliente e saldo inicial."""
        super().__init__(agencia, numero, cliente, saldo_inicial)
        self.tipo_conta = "Conta Corrente"

    def sacar(self, valor):
        """Método de saque que respeita o limite de saques e valor por dia."""
        if self._saques_hoje >= ContaCorrente.LIMITE_SAQUE_DIA:
            print("Limite diário de saques atingido.")
        elif valor > ContaCorrente.LIMITE_VALOR_SAQUE:
            print(f"Limite de saque de R$ {ContaCorrente.LIMITE_VALOR_SAQUE} excedido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            self._saques_hoje += 1
            self.adicionar_historico(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual R${self._saldo:.2f}")

    def depositar(self, valor):
        """Método de depósito na Conta Corrente."""
        data_hora_utc = datetime.now(pytz.timezone("America/Sao_Paulo"))
        self._saldo += valor
        self.adicionar_historico(f"Depósito de R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso em {data_hora_utc.strftime('%d/%m/%Y - %H:%M:%S')} UTC")
        data_hora_utc = datetime.now(pytz.timezone("America/Sao_Paulo"))  


# Classe ContaPoupanca implementando a interface Conta
class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, cliente, saldo_inicial=0):
        """Inicializa uma Conta Poupança com agência, número, cliente e saldo inicial."""
        super().__init__(agencia, numero, cliente, saldo_inicial)
        self.tipo_conta = "Conta Poupança"

    def sacar(self, valor):
        """Método de saque que checa apenas o saldo na Conta Poupança."""
        if valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            self.adicionar_historico(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        """Método de depósito na Conta Poupança."""
        self._saldo += valor
        self.adicionar_historico(f"Depósito de R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")


# Função principal que exibe o menu e controla o fluxo de ações
def main():
    print("Bem-vindo ao sistema bancário!")
    conta = None

    # Escolha do tipo de cliente
    nome = input("Digite o nome do cliente: ")
    tipo_cliente = int(input("Digite o tipo de cliente (1 - para Pessoa Física, 2 - para Pessoa Jurídica): "))
    if tipo_cliente == 1:
        documento = input("Digite o CPF do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
    elif tipo_cliente == 2:
        documento = input("Digite o CNPJ do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
    else:
        print("Tipo de cliente inválido.")
        return

    cliente = Cliente(nome, documento, email, telefone, tipo_cliente)

    # Escolha do tipo de conta
    while not conta:
        print("Selecione o tipo de conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        opcao_conta = int(input("Escolha uma opção (1 ou 2): "))

        agencia = int(input("Digite a agência da conta: "))
        numero = int(input("Digite o número da conta: "))

        if opcao_conta == 1:
            conta = ContaCorrente(agencia, numero, cliente)
            print("Conta Corrente criada.")
        elif opcao_conta == 2:
            conta = ContaPoupanca(agencia, numero, cliente)
            print("Conta Poupança criada.")
        else:
            print("Opção inválida, tente novamente.")

    # Menu principal
    while True:
        print("\nMenu de opções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Ver histórico")
        print("5 - Ver informações da conta")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_saldo()
        elif opcao == "4":
            conta.exibir_historico()
        elif opcao == "5":
            conta.info_conta()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
