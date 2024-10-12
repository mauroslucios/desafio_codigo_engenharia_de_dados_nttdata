# Desafio_codigo_engenharia_de_dados_nttdata
### # Sistema Bancário em Python

Este projeto é um sistema bancário simples em Python que permite criar contas, realizar depósitos e saques, e gerenciar o histórico de transações. Ele suporta múltiplas contas por cliente e inclui funcionalidades como validação de depósitos e saques, limite de saques por dia, e exibição de informações detalhadas sobre as contas.

## Funcionalidades

- **Criar Conta Corrente ou Conta Poupança**: O cliente pode criar diferentes tipos de conta.
- **Realizar Depósitos e Saques**: Permite realizar operações financeiras, com validações de limite de saque e depósito.
- **Visualizar Histórico de Transações**: Exibe todas as transações realizadas na conta.
- **Listar Contas**: Lista todas as contas associadas a um cliente.
- **Exibir Informações da Conta**: Mostra detalhes da conta e do cliente, incluindo e-mail e telefone.

## Tecnologias Utilizadas

- Python 3
- Módulos: `abc`, `datetime`

## Como Usar

1. **Execute o programa**: Inicie o sistema bancário executando o arquivo `desafioV2.py`.
2. **Digite os dados do cliente**: Informe o nome, tipo de cliente (Pessoa Física ou Jurídica), CPF ou CNPJ, e-mail e telefone.
3. **Crie contas**: Escolha entre criar uma Conta Corrente ou Conta Poupança.
4. **Gerencie as contas**: Utilize o menu para realizar depósitos, saques, e visualizar o saldo e histórico de transações.

## Limitações e Validações

- **Limite de Saques**: Máximo de 3 saques por dia.
- **Limite de Valor de Saque**: R$ 10.000,00 por transação.
- **Limite de Depósito**: R$ 1.000.000,00 por transação.

## Executar o Sistema

Para executar o sistema, use o seguinte comando no terminal:

```bash
python desafio/main.py

