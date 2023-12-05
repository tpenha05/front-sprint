import streamlit as st
import pandas as pd
import plotly.express as px
from funcoes import *
from moviepy.editor import VideoFileClip
import os 
from PIL import Image
from datetime import date
from time import sleep
from .metade_certa import *
from .cruz_funcoes import *
from .esboço_campo import *
from .geral import *
from .graficos_cruzamentos import *

def dashboard_cruzamento():
    with open("design/style/cruzamento.css") as d:
            st.markdown(f"<style>{d.read()}</style>", unsafe_allow_html=True)

    clube_usuario = st.session_state['clube']
    if primeiro_time["nome"] == clube_usuario:
        # time_usuario = primeiro_time
        time_usuario_cruzamento = primeiro_time_cruzamentos
    elif segundo_time["nome"] == clube_usuario:
        # time_usuario = segundo_time
        time_usuario_cruzamento = segundo_time_cruzamentos

    # st.subheader("CRUZAMENTOS")
    col1,space, col2 = st.columns([120,15,120])
    with col1:
        st.subheader(f"{nome_primeiro_time} x {nome_segundo_time}")
        with st.container():
            st.pyplot(desenhar_campo_com_quadrado(porcentagem_primeiro_time, porcentagem_segundo_time,lado_a,lado_b))

        # st.write("---")
        with st.container():
            coluna_casa, coluna_visitante = st.columns(2)
            with coluna_casa:
                jogadores = []
                cruzamentos = []
                st.markdown(f"Destaques {nome_primeiro_time} :")

                for jogador in destaques_primeiro_time:
                    # st.write("---")
                    jogadores.append(jogador)
                    cruzamentos.append(destaques_primeiro_time[jogador])

                data_team1 = {'Jogador': jogadores,'Ordenar': cruzamentos}

                df = pd.DataFrame(data_team1)
                st.dataframe(data=df, width=250, hide_index=True)
        
            with coluna_visitante:
                jogadores_2 = []
                cruzamentos_2 = []
                st.markdown(f"Destaques {nome_segundo_time} :")
                for jogador in destaques_segundo_time:
                    jogadores_2.append(jogador)
                    cruzamentos_2.append(destaques_segundo_time[jogador])

                data_team2 = {'Jogador': jogadores_2,'Ordenar': cruzamentos_2}

                df = pd.DataFrame(data_team2)
                st.dataframe(data=df, width=250, hide_index=True)

        # st.write("---")

        with st.container():
            col_grafico, col_grafico_segundo_time = st.columns(2)
            with col_grafico:
                grafico_cruza_camisa(n_aparicoes_primeiro_time_ataque, nome_primeiro_time)
                grafico_resultados(desfechos_primeiro_time, len(primeiro_time_cruzamentos), nome_primeiro_time)
            with col_grafico_segundo_time:
                grafico_cruza_camisa(n_aparicoes_segundo_time_ataque, nome_segundo_time)
                grafico_resultados(desfechos_segundo_time, len(segundo_time_cruzamentos), nome_segundo_time)

    with col2:

        #Caixa para selecionar o cruzamento, pegando o id do cruzamento, sendo ele (id-1)
        lista_id = []
        desfecho = []
        tempo = []
        for id in range(len(time_usuario_cruzamento)):
            lista_id.append(f"Cruzamento {id + 1}")

        opcao_selecionada = st.selectbox('Selecione uma opção', lista_id)
        opcao_selecionada = opcao_selecionada.split(" ")
        id = int(opcao_selecionada[1]) -1
        st.write("---")
        
        with st.container():
            col_um, col_dois = st.columns(2)
            with col_um:
                desfecho = time_usuario_cruzamento[id]["desfecho"]
                st.markdown(f"**Desfecho:** {desfecho}")
                
            with col_dois:
                tempo_de_jogo = time_usuario_cruzamento[id]["instante_cruzamento"]
                st.markdown(f"**Tempo de jogo:** {tempo_de_jogo}")
            
        st.write("---")

        
        coluna1, coluna2, coluna3 = st.columns([1,1,1.8])
        with st.container():

            with coluna1:
                #jogadores ataque
                st.write("**Atacando:**")
                for jogador in jogadores_ataque(time_usuario_cruzamento[id]):
                    st.markdown(f"{jogador}")

            with coluna2:
                #jogadores Defesa
                st.write("**Defendendo:**")
                for jogador in jogadores_defesa(time_usuario_cruzamento[id]):
                    st.markdown(f"{jogador}")

            with coluna3:
                #lugar do Campo.
                # st.markdown("**Zona do Campo**")
                zona = time_usuario_cruzamento[id]["zona"]
                figura_cortada = desenho_zona(lado_a,zona)
                st.pyplot(figura_cortada)