import streamlit as st
from .geral import *
from .graficos_cruzamentos import * 
from .esboço_campo import * 
from .metade_certa import *
# st.set_page_config(layout="wide")

def dash_cruzamento():
    clube_usuario = st.session_state['clube']
    if primeiro_time["nome"] == clube_usuario:
        time_usuario = primeiro_time
        time_usuario_cruzamento = primeiro_time_cruzamentos
    elif segundo_time["nome"] == clube_usuario:
        time_usuario = segundo_time
        time_usuario_cruzamento = segundo_time_cruzamentos

    st.title("CRUZAMENTOS")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(    f"<h1 style='text-align: center;'>{nome_primeiro_time} x {nome_segundo_time}</h1>", 
        unsafe_allow_html=True)
        with st.container():
            st.pyplot(desenhar_campo_com_quadrado(porcentagem_primeiro_time, porcentagem_segundo_time,lado_a,lado_b))
            # col_grafico, col_grafico_segundo_time = st.columns(2)
            # with col_grafico:
            #     grafico_frequencia(porcentagem_primeiro_time, nome_primeiro_time)
            
            # with col_grafico_segundo_time:
            #     grafico_frequencia(porcentagem_segundo_time, nome_segundo_time)

        st.write("---")
        with st.container():
            coluna_casa, coluna_visitante = st.columns(2)
            with coluna_casa:
                st.markdown(f"Destaques {nome_primeiro_time} :")
                for jogador in destaques_primeiro_time:
                    st.markdown(f"{jogador},{destaques_primeiro_time[jogador]}")
                    
        
            with coluna_visitante:
                st.markdown(f"Destaques {nome_segundo_time} :")
                for jogador in destaques_segundo_time:
                    st.markdown(f"{jogador},   {destaques_segundo_time[jogador]}")
        st.write("---")
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
        for id in range(len(time_usuario_cruzamento)):
            lista_id.append(f"cruzamento {id + 1}")
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
            
            st.markdown(f"aqui o video do cruzamento {id +1 }")
        st.write("---")

        
        coluna1, coluna2, coluna3 = st.columns(3)
        with st.container():

            with coluna1:
                #jogadores ataque
                st.write("**Jogadores Ataque:**")
                for jogador in jogadores_ataque(time_usuario_cruzamento[id]):
                    st.markdown(f"{jogador}")

            with coluna2:
                #jogadores Defesa
                st.write("**Jogadores Defesa:**")
                for jogador in jogadores_defesa(time_usuario_cruzamento[id]):
                    st.markdown(f"{jogador}")

            with coluna3:
                #lugar do Campo.
                st.markdown("**Zona do Campo**")
                zona = time_usuario_cruzamento[id]["zona"]
                figura_cortada = desenho_zona(lado_a,zona)
                st.pyplot(figura_cortada)

