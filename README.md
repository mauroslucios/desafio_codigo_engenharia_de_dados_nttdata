# Desafio_codigo_engenharia_de_dados_nttdata
### Sistema Bancário em Python

## Descrição

Este é um sistema bancário simples que permite aos usuários realizar operações como depósitos, saques, consulta de saldo, histórico de transações, e visualizar informações de conta. Ele implementa conceitos de Programação Orientada a Objetos (POO), como interfaces, polimorfismo e encapsulamento, utilizando a biblioteca `ABC`. Além disso, o sistema possui limites para saque diário e máximo por transação, registra transações com data e hora em UTC e permite a criação de clientes Pessoa Física (CPF) ou Jurídica (CNPJ).

## Funcionalidades

- Criar conta de Pessoa Física ou Jurídica.
- Criar Conta Corrente ou Conta Poupança.
- Realizar depósitos.
- Realizar saques (com limite de 3 saques por dia e de até R$ 10.000,00 por saque para Conta Corrente).
- Consultar o saldo da conta.
- Consultar o histórico de transações com registro de data/hora em UTC.
- Verificar informações detalhadas da conta e cliente.

## Tecnologias Usadas

- **Python 3.7+**
- **ABC** (Abstract Base Classes) para interfaces abstratas.
- **datetime** para registrar data e hora das transações em UTC.

## Como Usar

1. Clone o repositório ou copie os arquivos para o seu ambiente de desenvolvimento.
2. Execute o arquivo `main.py` no terminal:
   ```bash
   python main.py


### Explicação do Código

1. **Classe `Conta`**: Classe base abstrata que define os atributos comuns a todas as contas (agência, número, cliente, saldo e histórico) e os métodos abstratos `sacar` e `depositar`. Contém também métodos para adicionar ao histórico e exibir saldo.
2. **Classe `Cliente`**: Representa um cliente, que pode ser uma pessoa física ou jurídica, com nome e documento (CPF/CNPJ).
3. **Classe `ContaCorrente`**: Implementa os métodos de saque e depósito específicos para Conta Corrente, respeitando os limites diários e de valor por saque.
4. **Classe `ContaPoupanca`**: Implementa os métodos de saque e depósito para Conta Poupança, que não possui limites de saque diários.
5. **Função `main`**: Controla o fluxo principal do programa, exibe menus, cria clientes e contas e gerencia transações.

### Conclusão

Este sistema bancário utiliza boas práticas de POO e pode ser facilmente expandido para incluir mais funcionalidades. Ele é modular e permite operações de maneira simples e direta.

