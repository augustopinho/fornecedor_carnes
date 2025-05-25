# Import Modulos
from driver.psycopg2_connect import PostgresConnect as driver

# Import Libs
import pandas as pd

class Manage_database(driver):
    '''
    Classe responsável por gerenciar as operações no banco de dados, 
    se baseia na PostgresConnect (classe pai, driver do sgbd)
    para fazer a conexão com o banco. 
    '''

    def __init__(self):
        super().__init__() # Chama o __init__ da classe pai (PostgresConnect)
    
        # Cria o banco de dados se não existir
        self.create_table_tb_fornecedor()
        self.create_table_tb_produto()
        self.create_table_tb_entrada()
        self.create_table_tb_produto_entrada()
        self.create_table_tb_estoque()
        self.create_table_tb_cliente()
        self.create_table_tb_pedido()
        self.create_table_tb_item_pedido()
        self.create_table_tb_pagamento()



    def read_table(self, table_name, columns=None, where=None):
        '''
        Lê uma tabela do banco de dados e retorna um DataFrame.
        Tem como padrão o database "america_gestao"

        Argumentos:
            table_name: Nome da tabela a ser lida
            columns: Colunas a serem lidas (pode ser uma lista ou None para todas as colunas)
            where: Condição WHERE para filtrar os dados (pode ser None para não filtrar)
        '''
        try:
            conn = self.conn
            if conn is not None:
                query = (
                    f"SELECT {', '.join(columns) if columns else '*'} "
                    f"FROM {table_name}"
                )
                if where:
                    query += f" WHERE {where}"

                df = pd.read_sql(query, conn)
                return df
            else:
                print("Erro ao conectar ao banco de dados.")
                return None
        except Exception as e:
            print(f"Erro ao ler a tabela {table_name}: {e}")
            return None



    # Criação das tabelas do banco de dados

    def create_table_tb_fornecedor(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_fornecedor (
                id_fornecedor SERIAL PRIMARY KEY,
                nome_fornecedor VARCHAR(100),
                cnpj_fornecedor VARCHAR(20),
                telefone_fornecedor VARCHAR(20),
                email_fornecedor VARCHAR(100),
                endereco_fornecedor TEXT
            );
        '''
        self.execute_query(query)    



    def create_table_tb_produto(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_produto (
                id_produto SERIAL PRIMARY KEY,
                nome_produto VARCHAR(100),
                tipo_corte VARCHAR(50),
                unidade_medida VARCHAR(20),
                preco_compra DECIMAL(10,2),
                preco_venda DECIMAL(10,2),
                id_fornecedor INT REFERENCES tb_fornecedor(id_fornecedor)
            );
        '''
        self.execute_query(query)
       


    def create_table_tb_entrada(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_entrada (
                id_entrada SERIAL PRIMARY KEY,
                data_entrada DATE,
                id_fornecedor INT REFERENCES tb_fornecedor(id_fornecedor)
            );
        '''
        self.execute_query(query)
    


    def create_table_tb_produto_entrada(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_produto_entrada (
                id_item_entrada SERIAL PRIMARY KEY,
                id_entrada INT REFERENCES tb_entrada(id_entrada),
                id_produto INT REFERENCES tb_produto(id_produto),
                quantidade INT,
                preco_total DECIMAL(10,2),
                validade DATE,
                lote VARCHAR(50)
            );
        '''
        self.execute_query(query)
    


    def create_table_tb_estoque(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_estoque (
                id_estoque SERIAL PRIMARY KEY,
                item_entrada INT REFERENCES tb_produto_entrada(id_item_entrada),
                quantidade_disponivel INT,
                localizacao VARCHAR(100)
            );
        '''
        self.execute_query(query)
    


    def create_table_tb_cliente(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_cliente (
                id_cliente SERIAL PRIMARY KEY,
                nome_cliente VARCHAR(100),
                cnpj_cliente VARCHAR(20),
                endereco_cliente TEXT,
                telefone_cliente VARCHAR(20),
                email_cliente VARCHAR(100),
                tipo_cliente VARCHAR(20)
            );
        '''
        self.execute_query(query)
    


    def create_table_tb_pedido(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_pedido (
                id_pedido SERIAL PRIMARY KEY,
                id_cliente INT REFERENCES tb_cliente(id_cliente),
                data_pedido DATE,
                status VARCHAR(50),
                valor_total DECIMAL(10,2)
            );
        '''
        self.execute_query(query)
    


    def create_table_tb_item_pedido(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_item_pedido (
                id_item_saida SERIAL PRIMARY KEY,
                id_pedido INT REFERENCES tb_pedido(id_pedido),
                id_produto INT REFERENCES tb_produto(id_produto),
                quantidade INT,
                unidade_medida VARCHAR(20),
                preco_unitario DECIMAL(10,2)
            );
        '''
        self.execute_query(query)

    
    
    def create_table_tb_pagamento(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tb_pagamento (
                id_pagamento SERIAL PRIMARY KEY,
                id_pedido INT REFERENCES tb_pedido(id_pedido),
                data_pagamento DATE,
                lote_saida VARCHAR(50),
                valor_pago DECIMAL(10,2),
                metodo_pagamento VARCHAR(50),
                status VARCHAR(50)
            );
        '''
        self.execute_query(query)