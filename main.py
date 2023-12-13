from controleSQL import ControleSQL
from menus import Menus

# Configuração do banco de dados
DB_CONFIG = {
    "database": "trabalhoBD",
    "user": "postgres",
    "password": "0301",
    "host": "localhost",
    "port": "5432",
}

# Inicialização do controle SQL
controle_sql = ControleSQL(**DB_CONFIG)

while True:
    opcao_principal = Menus.exibir_menu_principal()

    if opcao_principal == "1":
        codigo, nome, telefone = Menus.cadastrar_cliente()
        controle_sql.cadastrar_cliente(codigo, nome, telefone)

    elif opcao_principal == "2":
        codigo, nome, valor, quantidade_estoque = Menus.cadastrar_produto()
        controle_sql.cadastrar_produto(codigo, nome, valor, quantidade_estoque)

    elif opcao_principal == "3":
        cliente_codigo, total, forma_pagamento, itens_venda = Menus.cadastrar_venda()
        controle_sql.cadastrar_venda(
            cliente_codigo, total, forma_pagamento, itens_venda
        )

    elif opcao_principal == "4":
        produto_codigo, quantidade_vendida = Menus.atualizar_estoque()
        controle_sql.atualizar_estoque(produto_codigo, quantidade_vendida)

    elif opcao_principal == "5":
        opcao_informacoes_cliente = Menus.obter_informacoes_cliente()
        nome, telefone = controle_sql.obter_informacoes_cliente(
            opcao_informacoes_cliente
        )
        print(f"Nome: {nome}, Telefone: {telefone}")

    elif opcao_principal == "6":
        while True:
            opcao_relatorios = Menus.exibir_menu_relatorios()

            if opcao_relatorios == "1":
                todos_clientes = controle_sql.obter_todos_clientes()
                for cliente in todos_clientes:
                    print(cliente)

            elif opcao_relatorios == "2":
                total_vendas_empreendimento = (
                    controle_sql.obter_total_vendas_empreendimento()
                )
                print(
                    f"Total de vendas do empreendimento: {total_vendas_empreendimento}"
                )

            elif opcao_relatorios == "3":
                codigo_cliente = Menus.obter_informacoes_cliente()
                total_vendas_cliente = controle_sql.obter_total_vendas_por_cliente(
                    codigo_cliente
                )
                print(
                    f"Total de vendas para o cliente {codigo_cliente}: {total_vendas_cliente}"
                )

            elif opcao_relatorios == "0":
                break

            else:
                print("Opção inválida. Tente novamente.")

    elif opcao_principal == "0":
        controle_sql.fechar_conexao()
        break

    else:
        print("Opção inválida. Tente novamente.")
