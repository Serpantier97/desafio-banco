# 💰 Sistema Bancário em Python (Orientado a Objetos)

Este é um projeto de sistema bancário desenvolvido em Python com foco em **Programação Orientada a Objetos (POO)**. Ele permite operações básicas como **depósito, saque, criação de usuários e contas**, além de exibir extratos e listar contas.

## 🚀 Funcionalidades

- Criar um novo usuário (CPF, nome, data de nascimento, endereço)
- Criar uma nova conta bancária vinculada a um usuário
- Realizar depósitos
- Realizar saques com limite de valor e quantidade
- Exibir extrato de movimentações
- Listar contas cadastradas

## 📦 Tecnologias Utilizadas

- Python 3.10+
- Programação Orientada a Objetos (POO)
- Terminal/CLI para entrada de dados

## 📚 Modelo de Classes (UML)





+----------------+
| Usuario |
+----------------+
| nome |
| data_nascimento|
| cpf |
| endereco |
+----------------+



+----------------+
| Conta |
+----------------+
| agencia |
| numero |
| usuario |
| saldo |
| extrato |
| saques |
+----------------+
| depositar() |
| sacar() |
| mostrar_extrato()|
+----------------+





+----------------+
| Sistema |
+----------------+
| usuarios |
| contas |
+----------------+
| menu() |
| criar_usuario()|
| criar_conta() |
| listar_contas()|
| executar() |
+----------------+
