from abc import ABC, abstractmethod
from datetime import datetime, timezone

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
        """Adiciona uma ação ao histórico de transações."""
        data_hora_utc = datetime.now(timezone.utc)  # Corrigido para usar timezone-aware UTC
        self._historico.append(f"{acao} em {data_hora_utc.strftime('%Y-%m-%d %H:%M:%S')} UTC")

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
        print(f"Documento: {self._cliente.documento}")
        print(f"E-mail: {self._cliente.email}")
        print(f"Telefone: {self._cliente.telefone}\n")


# Classe Cliente que representa o cliente da conta (Pessoa Física ou Jurídica)
class Cliente:
    def __init__(self, nome, documento, email, telefone, tipo_cliente):
        """Inicializa um cliente com nome, documento (CPF ou CNPJ), email, telefone e tipo de cliente."""
        self.nome = nome
        self.documento = documento
        self.email = email
        self.telefone = telefone
        self.tipo_cliente = tipo_cliente
        self.contas = []  # Lista de contas associadas ao cliente

    def adicionar_conta(self, conta):
        """Adiciona uma conta à lista de contas do cliente."""
        self.contas.append(conta)

    def listar_contas(self):
        """Lista todas as contas do cliente."""
        print("Contas do cliente:")
        for conta in self.contas:
            print(f"Tipo: {conta.tipo_conta}, Agência: {conta._agencia}, Número: {conta._numero}")


# Classe ContaCorrente implementando a interface Conta
class ContaCorrente(Conta):
    LIMITE_SAQUE_DIA = 3
    LIMITE_VALOR_SAQUE = 10000
    LIMITE_DEPOSITO = 1000000  # Valor máximo para depósito

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

    def depositar(self, valor):
        """Método de depósito na Conta Corrente."""
        if valor <= 0:
            print("Depósito inválido. O valor deve ser maior que zero.")
        elif valor > ContaCorrente.LIMITE_DEPOSITO:
            print(f"Valor excede o limite de depósito de R$ {ContaCorrente.LIMITE_DEPOSITO:.2f}.")
        else:
            self._saldo += valor
            self.adicionar_historico(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")


# Classe ContaPoupanca implementando a interface Conta
class ContaPoupanca(Conta):
    LIMITE_DEPOSITO = 1000000  # Valor máximo para depósito

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
        if valor <= 0:
            print("Depósito inválido. O valor deve ser maior que zero.")
        elif valor > ContaPoupanca.LIMITE_DEPOSITO:
            print(f"Valor excede o limite de depósito de R$ {ContaPoupanca.LIMITE_DEPOSITO:.2f}.")
        else:
            self._saldo += valor
            self.adicionar_historico(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")


# Função principal que exibe o menu e controla o fluxo de ações
def main():
    print("Bem-vindo ao sistema bancário!")
    cliente = None
    conta = None

    # Escolha do tipo de cliente
    nome = input("Digite o nome do cliente: ")
    tipo_cliente = input("Digite o tipo de cliente (1 - para Pessoa Física, 2 - para Pessoa Jurídica): ").upper()
    if tipo_cliente == "1":
        documento = input("Digite o CPF do cliente: ")
    elif tipo_cliente == "2":
        documento = input("Digite o CNPJ do cliente: ")
    else:
        print("Tipo de cliente inválido.")
        return

    # Solicitando e-mail e telefone do cliente
    email = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    cliente = Cliente(nome, documento, email, telefone, tipo_cliente)

    # Menu para criar contas
    while True:
        print("\nMenu de criação de contas:")
        print("1 - Criar Conta Corrente")
        print("2 - Criar Conta Poupança")
        print("3 - Listar Contas")
        print("4 - Sair")
        opcao_conta = input("Escolha uma opção: ")

        if opcao_conta == "1":
            agencia = input("Digite a agência da conta: ")
            numero = input("Digite o número da conta: ")
            conta = ContaCorrente(agencia, numero, cliente)
            cliente.adicionar_conta(conta)
            print("Conta Corrente criada e associada ao cliente.")
        elif opcao_conta == "2":
            agencia = input("Digite a agência da conta: ")
            numero = input("Digite o número da conta: ")
            conta = ContaPoupanca(agencia, numero, cliente)
            cliente.adicionar_conta(conta)
            print("Conta Poupança criada e associada ao cliente.")
        elif opcao_conta == "3":
            cliente.listar_contas()
        elif opcao_conta == "4":
            break
        else:
            print("Opção inválida, tente novamente.")

    # Menu principal para transações
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
            if conta:
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(valor)
            else:
                print("Nenhuma conta selecionada.")
        elif opcao == "2":
            if conta:
                valor = float(input("Digite o valor do saque: R$ "))
                conta.sacar(valor)
            else:
                print("Nenhuma conta selecionada.")
        elif opcao == "3":
            if conta:
                conta.exibir_saldo()
            else:
                print("Nenhuma conta selecionada.")
        elif opcao == "4":
            if conta:
                conta.exibir_historico()
            else:
                print("Nenhuma conta selecionada.")
        elif opcao == "5":
            if conta:
                conta.info_conta()
            else:
                print("Nenhuma conta selecionada.")
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()

