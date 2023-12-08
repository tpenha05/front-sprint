import streamlit as st
from cruzamentos.geral import *
from cruzamentos.dash_filtrado import *

# zonas = ["Selecionar", "E2.2","E2.1","E1.2","E1.1","E3","D2.2","D2.1","D1.2","D1.1","D3"]

zona_time_1 = ["Selecionar"]
for id in range(len(primeiro_time_cruzamentos)):
    if primeiro_time_cruzamentos[id]["zona"] not in zona_time_1:
        zona_time_1.append(primeiro_time_cruzamentos[id]["zona"])

zona_time_2 = ["Selecionar"]
for id in range(len(segundo_time_cruzamentos)):
    if segundo_time_cruzamentos[id]["zona"] not in zona_time_2:
        zona_time_2.append(segundo_time_cruzamentos[id]["zona"])        

filtro = {"zonas": [],
          "desfecho": [],
          "jogador" : []}

desfechos = ["Selecionar","Bem-Sucedido", "Perdido", "Bloqueado"]
jogadores_1 = ["Selecionar"]
for i in range(len(jogadores_primeiro_time)):
    jogadores_1.append(jogadores_primeiro_time[i])

jogadores_2 = ["Selecionar"]
for i in range(len(jogadores_segundo_time)):
    jogadores_2.append(jogadores_segundo_time[i])

tab1, tab2 = st.tabs([f"{nome_primeiro_time}", f"{nome_segundo_time}"])

with tab1:
    with st.expander("Filtros"):
        col1, col2 = st.columns(2)
        with col1:
            Zona_1 = st.selectbox('Filtro por zona', zona_time_1)
            filtro["zonas"] = Zona_1

            jogador_time_1 = st.selectbox('Filtro por jogador primeiro time', jogadores_1)
            filtro["jogador"] = jogador_time_1

            desfechos_1 = st.selectbox('Filtro por desfecho primeiro time', desfechos)
            filtro["desfecho"] = desfechos_1

        cruzamentos_1 = primeiro_time_cruzamentos
        if (filtro["zonas"] != "Selecionar") or (filtro["jogador"] != "Selecionar") or (filtro["desfecho"]) != "Selecionar":
            cruz_filtrado = []
            for i in range(len(cruzamentos_1)):
                if (filtro["zonas"] in cruzamentos_1[i]["zona"]) or (filtro["jogador"] in cruzamentos_1[i]["nome_jogadores_time_cruzando"]) or (filtro["desfecho"] in cruzamentos_1[i]["desfecho"]):
                    cruz_filtrado.append(cruzamentos_1[i])
            cruzamentos_1 = cruz_filtrado
            dashboard_cruzamento_filtrado(cruzamentos_1)
with tab2:
    with st.expander("Filtros"):
        col1, col2 = st.columns(2)
        with col1:
            Zona_2 = st.selectbox('Filtro por zona time', zona_time_2)
            filtro["zonas"] = Zona_2

            jogador_time_2 = st.selectbox('Filtro por jogador segundo time', jogadores_2)
            filtro["jogador"] = jogador_time_2

        with col2:
            desfechos_2 = st.selectbox('Filtro por desfecho segundo time', desfechos)
            filtro["desfecho"] = desfechos_2
            print(desfechos_2)

        cruzamentos_2 = segundo_time_cruzamentos
        if (filtro["zonas"] != "Selecionar") or (filtro["jogador"] != "Selecionar") or (filtro["desfecho"]) != "Selecionar":
            cruz_filtrado = []
                
            for i in range(len(cruzamentos_2)):
                if (filtro["zonas"] in cruzamentos_2[i]["zona"]) or (filtro["jogador"] in cruzamentos_2[i]["nome_jogadores_time_cruzando"]) or (filtro["desfecho"] in cruzamentos_2[i]["desfecho"]):
                    cruz_filtrado.append(cruzamentos_2[i])
            cruzamentos_2 = cruz_filtrado
            dashboard_cruzamento_filtrado(cruzamentos_2)
            
    
            print(cruz_filtrado)