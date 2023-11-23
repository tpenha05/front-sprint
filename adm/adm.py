import streamlit as st
import imagens
import requests
from funcas import *



url_base = "http://127.0.0.1:5000/admin"
response = requests.get(url_base)




def app_adm(pagina_atual):

    if pagina_atual == "home":
        st.header("",divider='rainbow')
        st.header('Bem Vindo :blue[ADM] :sunglasses:')


        st.write("---")

        times = [
            "Palmeiras",
            "Corinthians",
            "SaoPaulo",
            "Santos", 
            "Flamengo",
            "Vasco",
            "Fluminense"
            ]


        with st.container():
        #dividir em dois os times 
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                mostrar_times(times)
            with col2:
                if st.button("Adicionar um Novo time"):
                    pagina_atual = "adicionar"
                    mostrar_times(times)
            with col3:

                if st.button("visualizar", on_click=None):
                    mostrar_times(times)

        st.write("---")

        with st.container():
            if st.button("deletar times "):
                col1, col2, col3, col4 = st.columns(4)
                for id in range(len(times)):
                    with col1:
                        st.button("deletar")

    elif pagina_atual == "adicionar":
        None
