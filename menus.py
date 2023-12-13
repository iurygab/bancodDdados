import os


class Menus:
    @staticmethod
    def cadastrar_cliente():
        os.system("cls")
        print("\n------------ CADASTRAR CLIENTE ------------")
        codigo = input("Código do cliente: ")
        nome = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        return codigo, nome, telefone

    @staticmethod
    def cadastrar_produto():
        os.system("cls")
        print("\n------------ CADASTRAR PRODUTO ------------")
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        valor = float(input("Valor do produto: "))
        quantidade_estoque = int(input("Quantidade em estoque: "))
        return codigo, nome, valor, quantidade_estoque

    @staticmethod
    def cadastrar_venda():
        os.system("cls")
        print("\n------------ CADASTRAR VENDA ------------")
        cliente_codigo = input("Código do cliente: ")
        total = float(input("Total da venda: "))
        forma_pagamento = input("Forma de pagamento: ")

        itens_venda = []
        while True:
            produto_codigo = input("Código do produto (ou '0' para encerrar): ")
            if produto_codigo == "0":
                break
            quantidade = int(input("Quantidade: "))
            subtotal = float(input("Subtotal: "))
            itens_venda.append((produto_codigo, quantidade, subtotal))

        return cliente_codigo, total, forma_pagamento, itens_venda

    @staticmethod
    def atualizar_estoque():
        os.system("cls")
        print("\n------------ ATUALIZAR ESTOQUE ------------")
        produto_codigo = input("Código do produto: ")
        quantidade_vendida = int(input("Quantidade vendida: "))
        return produto_codigo, quantidade_vendida

    @staticmethod
    def obter_informacoes_cliente():
        os.system("cls")
        print("\n------------ INFORMAÇÕES DO CLIENTE ------------")
        codigo = input("Código do cliente: ")
        return codigo

    @staticmethod
    def exibir_menu_principal():
        print("------------ MENU PRINCIPAL ------------")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Cadastrar Venda")
        print("4. Atualizar Estoque")
        print("5. Informações do Cliente")
        print("6. Relatórios")
        print("\n0. Sair")
        print("-----------------------------------------")
        return input("\nEscolha uma opção: ")

    @staticmethod
    def exibir_menu_relatorios():
        print("\n------------ MENU RELATÓRIOS ------------")
        print("1. Todos os clientes cadastrados")
        print("2. Total de vendas do empreendimento")
        print("3. Total de vendas por cliente")
        print("\n0. Voltar")
        print("------------------------------------------")
        return input("\nEscolha uma opção: ")
