import streamlit as st

from geral import *
from collections import OrderedDict
from graficos_cruzamentos import * 

st.set_page_config(layout="wide")

st.title("CRUZAMENTOS")
col1, col2 = st.columns(2)
with col1:
    with st.container():
        col_grafico, col_grafico_adv = st.columns(2)
        with col_grafico:
            grafico_frequencia(porcentagem_pal, nome_palmeiras)
        
        with col_grafico_adv:
            grafico_frequencia(porcentagem_adv, nome_adversario)

    st.write("---")
    with st.container():
        coluna_casa, coluna_visitante = st.columns(2)
        with coluna_casa:
            st.markdown(f"Destaques {nome_palmeiras} :")
            for jogador in destaques_pal:
                st.markdown(f"{jogador},   {destaques_pal[jogador]}")
      
        with coluna_visitante:
            st.markdown(f"Destaques {nome_adversario} :")
            for jogador in destaques_adv:
                st.markdown(f"{jogador},   {destaques_adv[jogador]}")
    st.write("---")
    with st.container():
        col_grafico, col_grafico_adv = st.columns(2)
        with col_grafico:
            grafico_cruza_camisa(n_aparicoes_palmeiras_ataque, nome_palmeiras)
            grafico_resultados(desfechos_pal, len(palmeiras_cruzamentos), nome_palmeiras)
        with col_grafico_adv:
            grafico_cruza_camisa(n_aparicoes_adversario_ataque, nome_adversario)
            grafico_resultados(desfechos_adv, len(adversario_cruzamentos), nome_adversario)

with col2:

    #Caixa para selecionar o cruzamento, pegando o id do cruzamento, sendo ele (id-1)
    lista_id = []
    for id in range(len(palmeiras_cruzamentos)):
        lista_id.append(f"cruzamento {id + 1}")
    opcao_selecionada = st.selectbox('Selecione uma opção', lista_id)
    opcao_selecionada = opcao_selecionada.split(" ")
    id = int(opcao_selecionada[1]) -1
    st.write("---")

    with st.container():
        st.markdown(f"aqui o video do cruzamento {id +1 }")
    st.write("---")

    
    coluna1, coluna2, coluna3 = st.columns(3)
    with st.container():

        with coluna1:
            #jogadores ataque
            st.write("Jogadores Ataque:")
            for jogador in jogadores_ataque(palmeiras_cruzamentos[id]):
                st.markdown(f"{jogador}")

        with coluna2:
            #jogadores Defesa
            st.write("Jogadores Defesa:")
            for jogador in jogadores_defesa(palmeiras_cruzamentos[id]):
                st.markdown(f"{jogador}")

        with coluna3:
            #lugar do Campo.
            st.write("zona")
            st.markdown(busca_zona(palmeiras_cruzamentos[id]))