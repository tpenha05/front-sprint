import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
from .geral import *

def faz_quadrado(largura_campo,altura_campo,lista):
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6
    retangulo_destaque = patches.Rectangle((largura_quad * lista[0], altura_quad * lista[2]), largura_quad * (lista[1] - lista[0] + 1), altura_quad * (lista[3] - lista[2] + 1), linewidth=1, edgecolor='black', facecolor='#529F40')
    return retangulo_destaque
    

# Função para desenhar o campo de futebol com um quadrado abrangendo os quadrados selecionados
def desenhar_campo_com_quadrado(porcentagem_pal, porcentagem_adv, lado_a, lado_b):
    fig, ax = plt.subplots(figsize=(8, 5))

    # Definindo o tamanho do campo
    largura_campo = 100
    altura_campo = 60

    # Desenhando o campo de futebol
    # campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, color='#62ba17')
    retangulo_campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, edgecolor='black', facecolor='none')
#  color='#62ba17'
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6

    retangulo_destaque = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=1, edgecolor='#62ba17', facecolor='none')
    retangulo_destaque.set_facecolor('#62ba17')
    ax.add_patch(retangulo_destaque)

    # Adicionando o retângulo abrangendo os quadrados (x1, y3), (x1, y4), (x2, y3) e (x2, y4)
    retangulo_destaque = patches.Rectangle((largura_quad * 0, altura_quad * 2), largura_quad * (1 - 0 + 1), altura_quad * (3 - 2 + 1), linewidth=1, edgecolor='green', facecolor='none')
    retangulo_destaque.set_facecolor('#62ba17')
    plt.text(8, 28, "Área", fontsize=10, color='black') #cor da escrita "Área"
    ax.add_patch(retangulo_destaque)


    # #area outro lado B
    retangulo_destaque = patches.Rectangle((largura_quad * 7, altura_quad * 2), largura_quad * (8 - 7 + 1), altura_quad * (3 - 2 + 1), linewidth=1, edgecolor='green', facecolor='none')
    retangulo_destaque.set_facecolor('#62ba17')
    plt.text(86, 28, "Área", fontsize=10, color='black') #cor da escrita "Área"
    ax.add_patch(retangulo_destaque)

    circulo_central = patches.Circle((largura_campo/2, altura_campo/2), radius=5, edgecolor="white", facecolor='none')
    ax.add_patch(circulo_central)

    circulo_bola = patches.Circle((largura_campo/2, altura_campo/2), radius=0.4, edgecolor="white", facecolor='white')
    ax.add_patch(circulo_bola)

    linha = patches.Rectangle((largura_campo/2, 0), 0, altura_campo, linewidth=1, edgecolor='white', facecolor='none')
    linha.set_facecolor('white')
    ax.add_patch(linha)


    #quadrados do Campo, Lado A
    for parte in lado_a:
        retangulo_destaque = faz_quadrado(largura_campo,altura_campo,lado_a[parte])
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)
    
    #quadrados do Campo, Lado B
    for parte in lado_b:
        retangulo_destaque = faz_quadrado(largura_campo,altura_campo,lado_b[parte])
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)
    
    for chave in escrita_a.keys():
        plt.text(escrita_a[chave][0],escrita_a[chave][1],chave,fontsize=10, color='white')
        porcentagem = porcentagem_pal[chave]
        plt.text(escrita_a[chave][2]-1,escrita_a[chave][3],f"{porcentagem: .2f}%", fontsize=10, color='black')

    for chave in escrita_b.keys():
        plt.text(escrita_b[chave][0],escrita_b[chave][1],chave,fontsize=10, color='white')
        porcentagem = porcentagem_adv[chave]
        plt.text(escrita_b[chave][2],escrita_b[chave][3],f"{porcentagem: .2f}%", fontsize=10, color='black')

    # Configurações do gráfico
    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    return fig

# Exibindo o campo de futebol com o quadrado abrangente no Streamlit
    # figura = desenhar_campo_com_quadrado(porcentagem_primeiro_time, porcentagem_segundo_time, lado_a, lado_b)
    # st.pyplot(figura)
