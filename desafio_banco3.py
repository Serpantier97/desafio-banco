import textwrap

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

class Conta:
    def __init__(self, cliente, numero, agencia="0001", limite=500, limite_saques=3):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! Valor excede o limite. @@@")
        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Limite de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def criar_cliente(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.buscar_cliente(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print("=== Cliente criado com sucesso! ===")

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def criar_conta(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if cliente:
            numero_conta = len(self.contas) + 1
            conta = Conta(cliente, numero_conta)
            self.contas.append(conta)
            cliente.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Cliente não encontrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(textwrap.dedent(f"""
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
            """))

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "nu":
            banco.criar_cliente()

        elif opcao == "nc":
            banco.criar_conta()

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao in ["d", "s", "e"]:
            cpf = input("Informe o CPF do cliente: ")
            cliente = banco.buscar_cliente(cpf)

            if not cliente:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            if not cliente.contas:
                print("\n@@@ Cliente não possui contas! @@@")
                continue

            conta = cliente.contas[0]  # Usa a primeira conta do cliente

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)

            elif opcao == "e":
                conta.mostrar_extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione novamente.")


main()
