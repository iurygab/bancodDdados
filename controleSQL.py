import psycopg2


class ControleSQL:
    def __init__(self, database, user, password, host, port):
        self.conn = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def cadastrar_cliente(self, codigo, nome, telefone):
        query = "INSERT INTO cliente (codigo, nome, telefone) VALUES (%s, %s, %s)"
        self.cur.execute(query, (codigo, nome, telefone))
        self.conn.commit()

    def cadastrar_produto(self, codigo, nome, valor, quantidade_estoque):
        query = "INSERT INTO produto (codigo, nome, valor, quantidade_estoque) VALUES (%s, %s, %s, %s)"
        self.cur.execute(query, (codigo, nome, valor, quantidade_estoque))
        self.conn.commit()

    def cadastrar_venda(self, cliente_codigo, total, forma_pagamento, itens_venda):
        query_venda = "INSERT INTO venda (cliente_codigo, total, forma_pagamento) VALUES (%s, %s, %s) RETURNING codigo"
        self.cur.execute(query_venda, (cliente_codigo, total, forma_pagamento))
        venda_codigo = self.cur.fetchone()[0]

        for produto_codigo, quantidade, subtotal in itens_venda:
            query_item_venda = "INSERT INTO item_venda (venda_codigo, produto_codigo, quantidade, subtotal) VALUES (%s, %s, %s, %s)"
            self.cur.execute(
                query_item_venda, (venda_codigo, produto_codigo, quantidade, subtotal)
            )

        self.conn.commit()

    def atualizar_estoque(self, produto_codigo, quantidade_vendida):
        query = "UPDATE produto SET quantidade_estoque = quantidade_estoque - %s WHERE codigo = %s"
        self.cur.execute(query, (quantidade_vendida, produto_codigo))
        self.conn.commit()

    def obter_informacoes_cliente(self, codigo):
        query = "SELECT nome, telefone FROM cliente WHERE codigo = %s"
        self.cur.execute(query, (codigo,))
        return self.cur.fetchone()

    def obter_todos_clientes(self):
        query = "SELECT * FROM cliente"
        self.cur.execute(query)
        return self.cur.fetchall()

    def obter_total_vendas_empreendimento(self):
        query = "SELECT SUM(total) FROM venda"
        self.cur.execute(query)
        return self.cur.fetchone()[0]

    def obter_total_vendas_por_cliente(self, cliente_codigo):
        query = "SELECT SUM(total) FROM venda WHERE cliente_codigo = %s"
        self.cur.execute(query, (cliente_codigo,))
        return self.cur.fetchone()[0]

    def fechar_conexao(self):
        self.cur.close()
        self.conn.close()
