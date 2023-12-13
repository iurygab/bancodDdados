import os


class Menus:
    @staticmethod
    def cadastrar_cliente():
        os.system("cls")
        codigo = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        return codigo, nome, telefone

    @staticmethod
    def cadastrar_produto():
        os.system("cls")
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))
        return codigo, nome, valor, quantidade_estoque

    @staticmethod
    def cadastrar_venda():
        os.system("cls")
        cliente_codigo = input("Digite o código do cliente: ")
        total = float(input("Digite o total da venda: "))
        forma_pagamento = input("Digite a forma de pagamento: ")

        itens_venda = []
        while True:
            produto_codigo = input(
                "Digite o código do produto (ou '0' para encerrar): "
            )
            if produto_codigo == "0":
                break
            quantidade = int(input("Digite a quantidade: "))
            subtotal = float(input("Digite o subtotal: "))
            itens_venda.append((produto_codigo, quantidade, subtotal))

        return cliente_codigo, total, forma_pagamento, itens_venda

    @staticmethod
    def atualizar_estoque():
        os.system("cls")
        produto_codigo = input("Digite o código do produto: ")
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
        return produto_codigo, quantidade_vendida

    @staticmethod
    def obter_informacoes_cliente():
        codigo = input("Digite o código do cliente: ")
        return codigo

    @staticmethod
    def exibir_menu_principal():
        print("------------ MENU ------------")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Cadastrar Venda")
        print("4. Atualizar Estoque")
        print("5. Informações do Cliente")
        print("6. Relatórios")
        print("\n0. Sair")
        print("-------------------------------")
        return input("\nEscolha uma opção: ")

    @staticmethod
    def exibir_menu_relatorios():
        os.system("cls")
        print("------------ RELATÓRIOS ------------")
        print("1. Todos os clientes cadastrados")
        print("2. Total de vendas do empreendimento")
        print("3. Total de vendas por cliente")
        print("\n0. Voltar")
        print("-------------------------------------")
        return input("\nEscolha uma opção: ")
