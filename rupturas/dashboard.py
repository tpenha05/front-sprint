# import streamlit as st
# import plotly.express as px
# from funcoes import *
# import os 
# from cruzamentos.dashboard import *
# import json 
# from rupturas.campo_caio import *
# from app import chama_dashboard_cruzamentos

# def dashboard_quebra(cores_personalizadas, df_rupturas, df_desfechos, contagem_desfechos, lista_porcentagem, dados, ):
#     with open("design/style/rupturas.css") as d:
#         st.markdown(f"<style>{d.read()}</style>", unsafe_allow_html=True)

#     json_rupturas = json.dumps(dados,indent=4,separators=(',', ': ')).encode('utf-8')
#     st.download_button(
#     label= "Baixar Rupturas",
#     data = json_rupturas,
#     file_name = "rupturas.json",
#     mime="application/json"
#     )
#     time = []
#     desfechos = []
#     jogadores = []
#     zonas = ['Zona 1', 'Zona 1 - B', 'Zona 2', 'Zona 2 - B']
#     for times in dados['time']:
#         time.append(dados['time'][times]['nome'])
#     for desfecho in dados['time']['1']['desfechos']:
#         desfechos.append(desfecho)
#     for jogador in df_desfechos:
#         jogadores.append(jogador)
#     with st.expander("Filtros"):
#         col1, col2 = st.columns(2)
#         with col1:
#             Zona = st.selectbox('Filtro por zona', zonas)
#             Desfecho = st.selectbox('Filtro por Desfecho', desfechos)
#         with col2:
#             Jogador = st.selectbox('Filtro por Jogador', jogadores)
#             Time = st.selectbox('Filtro por time', time)
#         Zona = Zona or None
#         Desfecho = Desfecho or None
#         Jogador = Jogador or None
#         Time = Time or None
#         chama_dashboard_cruzamentos(Desfecho, Zona, Jogador, Time)
#     col1, space, col2 = st.columns([8,1,8])

#     with col1:

#         print(lista_porcentagem)
#         figura = desenhar_campo(lista_porcentagem)
#         st.pyplot(figura)

#         # coluna1, coluna2 = st.columns([1,1])
#         # with coluna1:
#         fig = px.pie(contagem_desfechos, names='Desfecho', values='Quantidade', title='Quantidade de Desfechos', hover_data=['Porcentagem'])
#         st.plotly_chart(fig)
#         # with coluna2:
#         st.write('Quantidade de desfechos por jogador')
#         st.dataframe(df_desfechos, width=250)

#     with col2:
#         quantidade = []
#         for i in range(len(df_rupturas)-1):
#             quantidade.append(i)
#         st.subheader("Seleção de Rupturas")
#         jogada = st.selectbox('',quantidade)
#         st.write("---")
#         st.dataframe(df_rupturas)
#         # st.write('You selected:', jogada)