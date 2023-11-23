import streamlit as st
from datetime import date
import imagens
import requests
from funcas import *
import pandas as pd
import plotly.express as px
from datetime import datetime

#colocar o conteúdo na pagina inteira.
st.set_page_config(layout="wide")

#base da url do admin, para puxar os dados com o back
url_base = "http://127.0.0.1:5000/admin"
response = requests.get(url_base)

pagina_atual = "home"

# header
with st.container():
    header()
st.header("",divider='rainbow')

# Mensagem de Bem Vindo do Admin
st.markdown(f"<p style='font-size: 48px; display: flex; flex-direction: column; align-items: center; text-align: center;'> Bem Vindo ADM</p>",unsafe_allow_html=True)
st.write("---")

time = ["Palmeiras",
        "Corinthians",
        "SaoPaulo",
        "Santos", 
        "Flamengo",
        "Vasco",
        "Fluminense"
        ]

with st.container():

    col1, col2, col3 = st.columns(3)
    st.container()
    with col1:
        opcoes_selecionadas = st.multiselect("Selecione os times:", ordenar_lista_alfabetica(time))
        st.write("Você selecionou as seguintes frutas:")
        for fruta in opcoes_selecionadas:
            st.write(fruta)
            st.markdown(f"{fruta} tem X partidas analizadas, e Y partidas para serem analizadas")
            if st.button(f"Acessar {fruta}", key=fruta):
                st.write("muito obg")
            st.write("---")

    with col2:
        st.write(f"Aqui mostra o gráfico de jogos analisados por times")
        st.title("Visualização de Dados")
        df = pd.DataFrame({
            'X': [1, 2, 3, 4, 5],
            'Y': [10, 11, 12, 13, 14],
            'Z': [20, 21, 22, 23, 24]
        })
        tabela = st.toggle("  ")
        if tabela:
            st.dataframe(df)

        st.title("gráfico de disperção")
        # Gráfico de dispersão interativo usando Plotly Express
        grafico_dispercao = st.toggle(" ")
        if grafico_dispercao:
            fig = px.scatter(df, x='X', y='Y', size='Z', title='Gráfico de Dispersão Interativo')
            st.plotly_chart(fig, use_container_width=True)  # Definindo para usar toda a largura da coluna

        dados = {'Categoria': ['A', 'B', 'C', 'D'],
                'Valores': [30, 40, 20, 10]}
        df_2 = pd.DataFrame(dados)

        # Título do aplicativo
        st.title("Grafico de pizza")
        grafico_pizza = st.toggle("")
        if grafico_pizza:
        # Gráfico de pizza interativo usando Plotly Express
            fig = px.pie(df_2, values='Valores', names='Categoria', title='Gráfico de Pizza Interativo')
            st.plotly_chart(fig, use_container_width=True)  # Definindo para usar toda a largura da coluna
        


    with col3:
        st.write("Funcionalidades")
        st.title("Adicionar Jogo")
        jogo = st.toggle("a")
        if jogo:
            st.selectbox("Time Mandante", ordenar_lista_alfabetica(time))
            st.number_input("Placar Time Mandante", min_value=0, max_value=30)

            st.selectbox("Time Visitante", ordenar_lista_alfabetica(time))
            st.number_input("Placar Time Visitante", min_value=0, max_value=30)

            data_jogo = st.date_input("Dia que o jogo ocorreu", date(2019, 7, 6))
 
            uploaded_files = st.file_uploader("Escolha um arquivo CSV", accept_multiple_files=True, key="fileuploader", type=["JSON"])
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)

            if st.button("Adicionar partida"):
                st.write("Você adicionou a partida no banco de dados")




st.write("---")

st.container()

