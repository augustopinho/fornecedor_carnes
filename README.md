# Fornecedor Carnes

Este projeto é um sistema web para gestão de fornecedores, produtos, estoque, clientes e pedidos, utilizando Python, Streamlit e PostgreSQL.

## O que o código faz?

O sistema permite:
- Gerenciar fornecedores, produtos, entradas de estoque, clientes, pedidos e pagamentos.
- Visualizar dashboards e relatórios via interface web.
- Persistir dados em um banco PostgreSQL.

A interface é construída com [Streamlit](https://streamlit.io/), e a comunicação com o banco de dados é feita usando [psycopg2](https://www.psycopg.org/).

## Ferramentas utilizadas

- **Python 3.8+**
- **Streamlit** (interface web)
- **psycopg2** (driver PostgreSQL)
- **dotenv** (para variáveis de ambiente)
- **PostgreSQL** (banco de dados relacional)
- **pandas** (manipulação de dados)

## Como configurar e rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/fornecedor_carnes.git
cd fornecedor_carnes
```

### 2. Instale o PostgreSQL

Certifique-se de ter o PostgreSQL instalado e rodando em sua máquina.  
Crie um banco de dados chamado `fornecedor_carnes`:

```bash
sudo -u postgres createdb fornecedor_carnes
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo (ajuste conforme seu ambiente):

```
USER_BD=seu_usuario_postgres
PASSWORD_BD=sua_senha_postgres
```

### 4. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Rode o sistema

```bash
streamlit run main.py
```

Acesse o endereço exibido no terminal (geralmente http://localhost:8501).

## Observações

- As tabelas do banco são criadas automaticamente na primeira execução.
- O arquivo `.env` e a pasta `venv/` já estão no `.gitignore` e não serão versionados.
- Certifique-se de que as credenciais do banco estejam corretas no `.env`.

---

**Dúvidas ou sugestões?**  
Abra uma issue ou entre em contato!