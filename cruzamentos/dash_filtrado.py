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
# import ..app import trata_video_cruzamentos, pega_dados_videos
from IPython.display import HTML

def dashboard_cruzamento_filtrado(dic_cruzamento):
    #Caixa para selecionar o cruzamento, pegando o id do cruzamento, sendo ele (id-1)
    lista_id = []
    desfecho = []
    tempo = []
    for id in range(len(dic_cruzamento)):
        lista_id.append(f"Cruzamento {id + 1}")
    # tempos_cruzamentos = trata_video_cruzamentos(pega_dados_videos("cruzamentos.json"))

    st.subheader("Seleção de Cruzamentos")

    # Lista para seleção do cruzamento
    lista_id = []
    for id in range(len(dic_cruzamento)):
        lista_id.append(f"Cruzamento {id+1}")
    opcao_selecionada = st.selectbox(' ', lista_id)
    opcao_selecionada = opcao_selecionada.split(" ")
    id = int(opcao_selecionada[1]) -1 

    st.write("---")
    
    # Verifica se o cruzamento selecionado existe nos tempos dos vídeos
    
    desfecho = dic_cruzamento[id]["desfecho"]
    st.markdown(f"**Desfecho:** {desfecho}")   
    tempo_de_jogo = dic_cruzamento[id]["instante_cruzamento"]
    st.markdown(f"**Tempo de jogo:** {tempo_de_jogo}")

    #     # URL do vídeo com o tempo de início especificado
    #     video_url = f"https://drive.google.com/file/d/1vWm45opnuiYNN0s1FFKx8DBekp-YX30R/preview?t={start_time}"

    #     st.write("---")
    #     st.write(HTML(f'<iframe src="{video_url}" width="640" height="360"></iframe>'))
    # else:
    #     st.warning("Vídeo de cruzamento selecionado não encontrado.")

    st.write("---")
    coluna1, coluna2, coluna3 = st.columns([1,1,1.8])
    with st.container():

        with coluna1:
            #jogadores ataque
            st.write("**Atacando:**")
            for jogador in jogadores_ataque(dic_cruzamento[id]):
                st.markdown(f"{jogador}")

        with coluna2:
            #jogadores Defesa
            st.write("**Defendendo:**")
            for jogador in jogadores_defesa(dic_cruzamento[id]):
                st.markdown(f"{jogador}")

        with coluna3:
            #lugar do Campo.
            # st.markdown("**Zona do Campo**")
            zona = dic_cruzamento[id]["zona"]
            figura_cortada = desenho_zona(lado_a,zona)
            st.pyplot(figura_cortada)