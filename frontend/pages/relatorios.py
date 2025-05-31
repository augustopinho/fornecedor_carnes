import streamlit as st
import pandas as pd

from models.database_psycopg_manager import Manage_database

def crud_section(title, table_name, columns, id_column, db_manager):
    st.header(title)
    df = db_manager.read_table(table_name)
    
    # Exibe a tabela antes do formulário de inserção
    st.subheader(f"Tabela de {title}")
    if df is not None and not df.empty:
        st.dataframe(df)
    else:
        st.info("Nenhum registro encontrado.")

    st.subheader(f"Adicionar novo {title[:-1]}")
    new_data = {}
    for col in columns:
        if col != id_column:
            new_data[col] = st.text_input(f"{col.replace('_', ' ').capitalize()} ({title[:-1]})", key=f"{table_name}_{col}_add")
    if st.button(f"Adicionar {title[:-1]}", key=f"add_{table_name}"):
        cols = ', '.join([col for col in columns if col != id_column])
        vals = ', '.join(['%s'] * (len(columns) - 1))
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"
        db_manager.execute_query(query, tuple(new_data[col] for col in columns if col != id_column))
        st.success(f"{title[:-1]} adicionado com sucesso!")
        st.experimental_rerun()

    st.subheader(f"Editar/Excluir {title[:-1]}")
    if df is not None and not df.empty:
        selected = st.selectbox(f"Selecione o {title[:-1]} para editar/excluir", df[id_column])
        selected_row = df[df[id_column] == selected].iloc[0]
        edit_data = {}
        for col in columns:
            if col != id_column:
                edit_data[col] = st.text_input(f"{col.replace('_', ' ').capitalize()} (editar)", value=str(selected_row[col]), key=f"{table_name}_{col}_edit")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Atualizar {title[:-1]}", key=f"update_{table_name}"):
                set_clause = ', '.join([f"{col} = %s" for col in columns if col != id_column])
                query = f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = %s"
                db_manager.execute_query(query, tuple(edit_data[col] for col in columns if col != id_column) + (selected,))
                st.success(f"{title[:-1]} atualizado com sucesso!")
                st.experimental_rerun()
        with col2:
            if st.button(f"Excluir {title[:-1]}", key=f"delete_{table_name}"):
                query = f"DELETE FROM {table_name} WHERE {id_column} = %s"
                db_manager.execute_query(query, (selected,))
                st.success(f"{title[:-1]} excluído com sucesso!")
                st.experimental_rerun()

def show():
    st.title("Relatórios Dinâmicos")

    db_manager = Manage_database()

    crud_section(
        "Fornecedores",
        "tb_fornecedor",
        ["id_fornecedor", "nome_fornecedor", "cnpj_fornecedor", "telefone_fornecedor", "email_fornecedor", "endereco_fornecedor"],
        "id_fornecedor",
        db_manager
    )

    crud_section(
        "Produtos",
        "tb_produto",
        ["id_produto", "nome_produto", "tipo_corte", "unidade_medida", "preco_compra", "preco_venda", "id_fornecedor"],
        "id_produto",
        db_manager
    )

    crud_section(
        "Clientes",
        "tb_cliente",
        ["id_cliente", "nome_cliente", "cnpj_cliente", "endereco_cliente", "telefone_cliente", "email_cliente", "tipo_cliente"],
        "id_cliente",
        db_manager
    )