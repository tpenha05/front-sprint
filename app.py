import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Dados de exemplo para autenticação
usuarios_cadastrados = {
    'usuario1': 'senha123',
    'usuario2': 'senha456',
    '1':'1'
}

# Função para verificar as credenciais
def verifica_credenciais(username, senha):
    return usuarios_cadastrados.get(username) == senha

# Função para adicionar novos usuários
def adicionar_usuario(username, senha):
    if username not in usuarios_cadastrados:
        usuarios_cadastrados[username] = senha
        return True
    return False

# Função principal para o aplicativo
def main():
    if 'usuario' not in st.session_state or st.session_state.usuario is None:
        login_cadastro()
    else:
        paginas()

def login_cadastro():
    st.title("Data Goal")

    # Abas para Login e Cadastro
    tab1, tab2 = st.tabs(["Login", "Cadastrar"])

    # Aba de Login
    with tab1:
        st.header("Faça login")
        username = st.text_input("Usuário:", key="login_username")
        senha = st.text_input("Senha:", type='password', key="login_password")

        if st.button("Login"):
            if verifica_credenciais(username, senha):
                st.success("Login bem-sucedido!")
                st.session_state.usuario = username
                st.rerun()
            else:
                st.error("Credenciais inválidas. Tente novamente.")

    # Aba de Cadastro
    with tab2:
        st.header("Cadastrar novo usuário")
        new_username = st.text_input("Novo usuário:", key="new_username")
        new_password = st.text_input("Nova senha:", type='password', key="new_password")

        if st.button("Cadastrar"):
            if adicionar_usuario(new_username, new_password):
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.error("Usuário já existe.")

# Função para exibir a página inicial
def pagina_inicial():
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial. Selecione uma opção na barra lateral para navegar.")

# Função para exibir a página de visualização de dados
def pagina_dados():
    st.title("Visualização de Dados")
    df = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [10, 11, 12, 13, 14],
        'Z': [20, 21, 22, 23, 24]
    })
    st.dataframe(df)
    st.title("Exemplo de Plotly no Streamlit")

    # Gráfico de dispersão interativo usando Plotly Express
    fig = px.scatter(df, x='X', y='Y', size='Z', title='Gráfico de Dispersão Interativo')
    st.plotly_chart(fig)

    dados = {'Categoria': ['A', 'B', 'C', 'D'],
         'Valores': [30, 40, 20, 10]}
    df_2 = pd.DataFrame(dados)

    # Título do aplicativo
    st.title("Exemplo de Gráfico de Pizza no Streamlit")

    # Gráfico de pizza interativo usando Plotly Express
    fig = px.pie(df_2, values='Valores', names='Categoria', title='Gráfico de Pizza Interativo')
    st.plotly_chart(fig)


# Função para exibir a página de configurações
def pagina_configuracoes():
    st.title("Configurações")
    # Adicione configurações ou opções aqui

def pagina_partidas(partidas):
    st.title("Partidas")

    df_partidas = pd.DataFrame(partidas)
    df_partidas['data'] = pd.to_datetime(df_partidas['data'], format='%d/%m/%Y').dt.date

    if df_partidas.empty:
        st.write("Não há partidas cadastradas.")
        return

    adversarios = ["Todos"] + sorted(df_partidas['adversario'].unique().tolist())
    adversario_selecionado = st.selectbox("Selecione o Adversário", adversarios)

    min_data, max_data = df_partidas['data'].min(), df_partidas['data'].max()
    data_inicial, data_final = st.slider(
        "Selecione o Intervalo de Datas",
        min_value=min_data,
        max_value=max_data,
        value=(min_data, max_data),
        format="DD/MM/YYYY"
    )

    df_filtrado = df_partidas.copy()
    if adversario_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['adversario'] == adversario_selecionado]
    df_filtrado = df_filtrado[(df_filtrado['data'] >= data_inicial) & (df_filtrado['data'] <= data_final)]

    st.dataframe(df_filtrado)


partidas_teste = [
    {"clube": "Palmeiras", "adversario": "Bragantino", "data": "21/09/2022", "resultado": "1x1"},
    {"clube": "Palmeiras", "adversario": "Vasco", "data": "21/09/2021", "resultado": "33x8"},
    {"clube": "Palmeiras", "adversario": "Barcelona", "data": "22/10/2022", "resultado": "7x1"}]

# Função principal para controlar a navegação entre as páginas
def paginas():
    # Criando uma barra lateral personalizada com um seletor de página
    st.sidebar.title("Dashboard")
    opcao_pagina = st.sidebar.radio("Escolha a Página:", ["Página Inicial", "Quebra de linha de defesa", "Cruzamento", "Partidas"])

    # Carregando a página selecionada
    if opcao_pagina == "Página Inicial":
        pagina_inicial()
    elif opcao_pagina == "Quebra de linha de defesa":
        pagina_dados()
    elif opcao_pagina == "Cruzamento":
        pagina_configuracoes()
    elif opcao_pagina == "Partidas":
        pagina_partidas(partidas_teste)

# Chamando a função principal para iniciar o aplicativo
if __name__ == "__main__":
    main()
