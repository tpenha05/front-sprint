import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



#grafico dos cruzamentos por camisa dos jogadores dos respectivos times
def grafico_cruza_camisa(aparicoes_ataque, nome):
    chaves = list(aparicoes_ataque.keys())
    valores = list(aparicoes_ataque.values())
    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(chaves, valores)
    # Definindo título e rótulos dos eixos
    ax.set_title(f'Cruzamentos do {nome}')
    ax.set_xlabel('Número da camisa')
    ax.set_ylabel('Contribuições em Cruzamentos')
    # Mostrando o gráfico no Streamlit
    return st.pyplot(fig)


def grafico_resultados(dic_resultados,tamanho, time):
    valores = list(dic_resultados.values())
    porcentagens = [(valor / tamanho) * 100 for valor in valores]
    # Criando o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(porcentagens, labels=dic_resultados.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Mantém o aspecto circular do gráfico
    # Definindo título
    ax.set_title('Distribuição em porcentagem')
    # Mostrando o gráfico no Streamlit
    return st.pyplot(fig)


def grafico_frequencia(dic_porcentagens, time):
    # Criando o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(dic_porcentagens.values(), labels=dic_porcentagens.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Mantém o aspecto circular do gráfico
    # Definindo título
    ax.set_title(f'Desfechos dos Cruzamentos {time}')
    # Mostrando o gráfico no Streamlit
    return st.pyplot(fig)


