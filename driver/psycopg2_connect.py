# Importando Libs
from dotenv import load_dotenv, find_dotenv
import os
import psycopg2
import urllib.parse

# Carregar variáveis do arquivo .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

class PostgresConnect():
    '''Classe responsável por gerenciar a conexão com o banco de dados usando psycopg2'''

    def __init__(self):
        self.username = os.getenv("USER_BD")
        self.password = os.getenv("PASSWORD_BD")
        self.host = "localhost"
        self.port = "5432"
        self.database = "fornecedor_carnes"
        self.conn = self.connect()

    def connect(self):
        '''Cria e retorna uma conexão com o banco de dados PostgreSQL'''

        try:
            # Codifica o password para uso seguro na string de conexão, se necessário
            encoded_password = urllib.parse.quote_plus(self.password)
            conn = psycopg2.connect(
                dbname=self.database,
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except Exception as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            return None
        


    def execute_query(self, query, params=None):
        """Executa uma consulta SQL sem retorno de dados."""

        if self.conn:
            try:
                cur = self.conn.cursor()
                cur.execute(query, params)
                self.conn.commit()
                cur.close()
                self.conn.close()
            except Exception as e:
                print(f"Erro ao executar query: {e}")

    def close_connection(self):
        '''Fecha a conexão com o banco de dados'''

        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Erro ao fechar a conexão com o banco de dados: {e}")