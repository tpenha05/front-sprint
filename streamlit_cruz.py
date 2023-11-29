import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from funcoes_cruzamentos import dic_cruzamentos
from funcoeees import ataque, defesa, resultado_cruzamentos, desfecho_por_quantidade, numero_ataque, numero_defesa
from collections import OrderedDict


#dicionarios para filtros
defesas_por_time = {}
ataques_por_time = {}
resultados_por_time = {}
desfechos_quant_por_time = {}
participacao_def_por_time = {}
participacao_ataque_por_time = {}


#time = id do time, "5" para o redbull e "1" para o palmeiras
for time in dic_cruzamentos["time"]:
    # Sub-dicionarios para filtros
    aparicoes_defesa= {}
    aparicoes_ataque= {}
    dic_resultados = {}
    dic_desfechos_quant = {}
    dic_part_def= {}
    dic_part_ataque = {}

    cruzamentos = dic_cruzamentos["time"][time]["rupturas"]
    for cruzamento in cruzamentos:
       
        #recolhendo dados da defesa
        aparicoes_defesa = defesa(cruzamento,aparicoes_defesa)

        #recolhendo dados do ataque
        aparicoes_ataque = ataque(cruzamento,aparicoes_ataque)

        # resultados dos cruzamentos
        dic_resultados = resultado_cruzamentos(cruzamento, dic_resultados)

        # dic_desfechos_quant = desfecho_por_quantidade(cruzamento, dic_desfechos_quant)

        dic_part_ataque = numero_ataque(cruzamento,dic_part_ataque)

        dic_part_def = numero_ataque(cruzamento,dic_part_def)



    #grafico dos cruzamentos por camisa dos jogadores dos respectivos times
    chaves = list(dic_part_ataque.keys())
    valores = list(dic_part_ataque.values())
    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(chaves, valores)
    # Definindo título e rótulos dos eixos
    ax.set_title(f'Cruzamentos do {dic_cruzamentos["time"][time]["nome"]}')
    ax.set_xlabel('Número da camisa')
    ax.set_ylabel('Contribuições em Cruzamentos')
    # Mostrando o gráfico no Streamlit
    st.pyplot(fig)


    # Calculando as porcentagens
    valores = list(dic_resultados.values())
    total = len(cruzamento["desfecho"])
    porcentagens = [(valor / total) * 100 for valor in valores]
    # Criando o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(porcentagens, labels=dic_resultados.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Mantém o aspecto circular do gráfico
    # Definindo título
    ax.set_title('Distribuição em porcentagem')
    # Mostrando o gráfico no Streamlit
    st.pyplot(fig)
    

    destaques = dict(sorted(aparicoes_ataque.items(), key=lambda item: item[1], reverse=True)[:5])
    for destaque in destaques.keys():
        st.markdown(f"{destaque} : {destaques[destaque]}")

    #dicionario dos dados gerais dos times.
    defesas_por_time[f'adversario do {dic_cruzamentos["time"][time]["nome"]}'] = aparicoes_defesa
    ataques_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = aparicoes_ataque
    resultados_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_resultados
    desfechos_quant_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_desfechos_quant
    participacao_ataque_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_part_ataque
    participacao_def_por_time[f'adversário do {dic_cruzamentos["time"][time]["nome"]}'] = dic_part_def

palmeiras = dic_cruzamentos["time"]["1"]
lista_id = []
for id in range(len(palmeiras["rupturas"])):
    lista_id.append(f"cruzamento {id + 1}")


opcao_selecionada = st.selectbox('Selecione uma opção', lista_id)
id = int(opcao_selecionada.split(" ")[1])



print (resultados_por_time)
