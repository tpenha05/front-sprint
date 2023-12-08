import streamlit as st
import plotly.express as px
from funcoes import *
import os 
from cruzamentos.dashboard import *
import json 
from rupturas.campo_caio import *
from app import trata_video_ruptura

def dashboard_quebra(cores_personalizadas, df_rupturas, df_desfechos, contagem_desfechos, lista_porcentagem, dados):
    with open("design/style/rupturas.css") as d:
        st.markdown(f"<style>{d.read()}</style>", unsafe_allow_html=True)

    json_rupturas = json.dumps(dados,indent=4,separators=(',', ': ')).encode('utf-8')
    st.download_button(
    label= "Baixar Rupturas",
    data = json_rupturas,
    file_name = "rupturas.json",
    mime="application/json"
    )

    col1, space, col2 = st.columns([8,1,8])
    with col1:
        figura = desenhar_campo(lista_porcentagem)
        st.pyplot(figura)

        # coluna1, coluna2 = st.columns([1,1])
        # with coluna1:
        fig = px.pie(contagem_desfechos, names='Desfecho', values='Quantidade', title='Quantidade de Desfechos', hover_data=['Porcentagem'])
        st.plotly_chart(fig)
        # with coluna2:
        st.write('Quantidade de desfechos por jogador')
        st.dataframe(df_desfechos, width=250)

    with col2:
        quantidade = []
        for i in range(len(df_rupturas)-1):
            if i != 0:
                quantidade.append(i)
        st.subheader("Seleção de Rupturas")

        tempos_rupturas = trata_video_ruptura(pega_dados_videos("quebra.json"))

        jogada = st.selectbox('',quantidade,key=quantidade)
        st.write("---")
        st.dataframe(df_rupturas)
        # st.write('You selected:', jogada)

        start_time = None
        if jogada in quantidade:
            start_time = tempos_rupturas[jogada][0]

        if start_time is not None:
            st.write(f"Tempo inicial selecionado: {start_time}")

            video_url = f"https://drive.google.com/file/d/1vWm45opnuiYNN0s1FFKx8DBekp-YX30R/preview?t={start_time}"

            st.write(f"Reproduzindo o vídeo a partir de {start_time} segundos:")
            st.write(HTML(f'<iframe src="{video_url}" width="640" height="360"></iframe>'))
        else:
            st.warning("Chave selecionada não encontrada no dicionário.")

