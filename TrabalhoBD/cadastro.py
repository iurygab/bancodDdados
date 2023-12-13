import banco


class Cliente:
    def __init__(self, nome, telefone, codigo):
        self.nome = nome
        self.telefone = telefone
        self.codigo = codigo
        self.compras = []


class Produto:
    def __init__(self, nome, codigo, valor, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.valor = valor
        self.quantidade_estoque = quantidade


class Venda:
    def __init__(self, cliente, itens, total, forma_pagamento):
        self.cliente = cliente
        self.itens = itens
        self.total = total
        self.forma_pagamento = forma_pagamento


clientes = []
produtos = []
vendas = []


def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    codigo = input("Código: ")

    # Realizar validações dos dados de entrada, se necessário

    cliente = Cliente(nome, telefone, codigo)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def cadastrar_produto():
    nome = input("Nome do produto: ")
    codigo = input("Código: ")
    valor = float(input("Valor de venda: "))
    quantidade = int(input("Quantidade em estoque: "))

    # Realizar validações dos dados de entrada, se necessário

    produto = Produto(nome, codigo, valor, quantidade)
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def cadastrar_venda():
    cliente_codigo = input("Código do cliente: ")
    cliente = next((c for c in clientes if c.codigo == cliente_codigo), None)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    itens = []
    total = 0

    while True:
        codigo_produto = input("Código do produto (0 para finalizar): ")
        if codigo_produto == "0":
            break

        produto = next((p for p in produtos if p.codigo == codigo_produto), None)

        if produto is None or produto.quantidade_estoque == 0:
            print("Produto não encontrado ou sem estoque.")
            continue

        quantidade = int(input(f"Quantidade de {produto.nome}: "))
        if quantidade > produto.quantidade_estoque:
            print("Quantidade insuficiente em estoque.")
            continue

        subtotal = quantidade * produto.valor
        total += subtotal
        itens.append((produto, quantidade, subtotal))
        produto.quantidade_estoque -= quantidade

    forma_pagamento = input("Forma de pagamento (Débito ou Crédito): ")

    venda = Venda(cliente, itens, total, forma_pagamento)
    cliente.compras.append(venda)
    vendas.append(venda)
    print("Venda cadastrada com sucesso!")


def atualizar_estoque():
    for produto in produtos:
        print(f"{produto.nome} - Quantidade em estoque: {produto.quantidade_estoque}")


def informacoes_cliente():
    codigo_cliente = input("Código do cliente: ")
    cliente = next((c for c in clientes if c.codigo == codigo_cliente), None)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print(f"Nome: {cliente.nome}")
    print(f"Código: {cliente.codigo}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Total de compras realizadas: {len(cliente.compras)}")


def relatorio_clientes():
    print("Lista de todos os clientes:\n")
    for cliente in clientes:
        print(
            f"{cliente.nome} - Código: {cliente.codigo} - Telefone: {cliente.telefone}"
        )


def relatorio_total_vendas():
    total_vendas = sum(venda.total for venda in vendas)
    print(f"Total de vendas do empreendimento: R${total_vendas:.2f}")


def relatorio_vendas_cliente():
    codigo_cliente = input("Código do cliente: ")
    cliente = next((c for c in clientes if c.codigo == codigo_cliente), None)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    total_vendas_cliente = sum(venda.total for venda in cliente.compras)
    print(f"Total de vendas para {cliente.nome}: R${total_vendas_cliente:.2f}")


while True:
    print("\n=================== MENU ===================")
    print("1. Cadastrar cliente")
    print("2. Cadastrar produto")
    print("3. Cadastrar venda")
    print("4. Atualizar estoque")
    print("-------------------------------------------")
    print("5. Informações do cliente")
    print("6. Relatório de todos os clientes")
    print("7. Relatório de total de vendas")
    print("8. Relatório de vendas por cliente")
    print("-------------------------------------------")
    print("9. Sair do sistema")
    print("===========================================")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        cadastrar_produto()
    elif opcao == "3":
        cadastrar_venda()
    elif opcao == "4":
        atualizar_estoque()
    elif opcao == "5":
        informacoes_cliente()
    elif opcao == "6":
        relatorio_clientes()
    elif opcao == "7":
        relatorio_total_vendas()
    elif opcao == "8":
        relatorio_vendas_cliente()
    elif opcao == "9":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
