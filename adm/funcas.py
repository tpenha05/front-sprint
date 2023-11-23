import streamlit as st
import imagens



def mostrar_times(times):
    with st.container():
        col1, col2 = st.columns(2)
        # Divide a tela em duas colunas


        # pedidos = requests.get(f'{BASE_URL}pedidos').json()["pedidos"]
            
        with col1:
            for id in range(len(times)):
                if id//2 == 0:
                    st.markdown(f"[{times[id]}](https://www.google.com)", unsafe_allow_html=True)

        with col2:
            for id in range(len(times)):
                if id //2 == 1:
                    st.markdown(f"[{times[id]}](https://www.google.com)", unsafe_allow_html=True)

        
def ordenar_lista_alfabetica(lista):
    return sorted(lista)



def header():
    # Divide a tela em 5 colunas
    col1, col2, col3, col4, col5 = st.columns(5)

    # Coluna do Logo (1ª coluna)
    with col1:
        logo_path = f"{imagens.logo}"  # Substitua pelo caminho do seu logo
        logo = st.image(logo_path, width=125)  # Ajuste a largura conforme necessário

    # Coluna do Nome da Empresa (2ª coluna)
    with col2:
        nome_empresa = "Delta Goal"
        link_nome_empresa = st.empty()
        link_nome_empresa.markdown(f"<p style='font-size: 20px; text-align: center;'><a href='#'>{nome_empresa}</a></p>", unsafe_allow_html=True)

    # Coluna do Hiperlink 1 (3ª coluna)
    with col3:
        url_link1 = "https://seu-link-1.com"
        link1 = st.empty()
        link1.markdown(f"<p style='font-size: 20px; text-align: center;'><a href='{url_link1}' target='_self'>Deletar Time</a></p>", unsafe_allow_html=True)

    # Coluna do Hiperlink 2 (4ª coluna)
    with col4:
        url_link2 = "http://localhost:8502/add_clube"
        link2 = st.empty()
        link2.markdown(f"<p style='font-size: 20px; text-align: center;'><a href='{url_link2}' target='_self'>Adicionar Time</a></p>", unsafe_allow_html=True)

    # Coluna do Hiperlink 3 (5ª coluna)
    with col5:
        url_link3 = "https://seu-link-3.com"
        link3 = st.empty()
        link3.markdown(f"<p style='font-size: 20px; text-align: center;'><a href='{url_link3}' target='_self'>Times</a></p>", unsafe_allow_html=True)
    
