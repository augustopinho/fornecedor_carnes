# Modulos
from models.database_psycopg_manager import Manage_database
from frontend.pages import home, dashboard, relatorios

# Import Libs
import streamlit as st

# Instancia a classe de gerenciamento do banco de dados
db_manager = Manage_database()


# Modularização do streamlit
st.set_page_config(page_title="App Modular", layout="wide")

st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox("Escolha a página", ["Home", "Dashboard", "Relatórios"])

if pagina == "Home":
    home.show()
elif pagina == "Dashboard":
    dashboard.show()
elif pagina == "Relatórios":
    relatorios.show()