import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
from .geral import *

def faz_campinho(largura_campo,altura_campo,lista):
    largura_quad = largura_campo / 4.5
    altura_quad = altura_campo / 6
    retangulo_destaque = patches.Rectangle((largura_quad * lista[0], altura_quad * lista[2]), largura_quad * (lista[1] - lista[0] + 1), altura_quad * (lista[3] - lista[2] + 1), linewidth=1, edgecolor='black', facecolor='none')
    return retangulo_destaque
    

# Função para desenhar o campo de futebol com um quadrado abrangendo os quadrados selecionados
def desenho_zona(lado_a, local):
    fig, ax = plt.subplots(figsize=(4, 5))

    # Definindo o tamanho do campo
    largura_campo = 50
    altura_campo = 60

    # Desenhando o campo de futebol
    retangulo_campo = patches.Rectangle((0, 0), largura_campo-16.8, altura_campo, linewidth=2, edgecolor='black', facecolor='none')

    largura_quad = largura_campo / 4.5
    altura_quad = altura_campo / 6

    # Adicionando o retângulo abrangendo os quadrados (x1, y3), (x1, y4), (x2, y3) e (x2, y4)
    retangulo_destaque = patches.Rectangle(((0, altura_quad * 2)), largura_quad * (1 - 0 + 1), altura_quad * (3 - 2 + 1), linewidth=1, edgecolor='green', facecolor='none')
    retangulo_destaque.set_facecolor('#62ba17')
    plt.text(8, 28, "Área", fontsize=10, color='black') #cor da escrita "Área"
    ax.add_patch(retangulo_destaque)

    
    #quadrados do Campo, Lado A
    for parte in lado_a:
        retangulo_destaque = faz_campinho(largura_campo,altura_campo,lado_a[parte])
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)
    
    
    for chave in escrita_a.keys():
        plt.text(escrita_a[chave][0],escrita_a[chave][1]-2,chave,fontsize=9, color='black')
        
    for parte in lado_a:
        retangulo_destaque = faz_campinho(largura_campo, altura_campo, lado_a[parte])
        # Adicionando preenchimento colorido a alguns quadrados
        if parte in [local]:
            retangulo_destaque.set_facecolor('#F6AE2D')
        else:
            retangulo_destaque.set_facecolor('none')  # Mantém outros quadrados sem preenchimento
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)
    
    # Configurações do gráfico
    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    return fig

# Exibindo o campo de futebol com o quadrado abrangente no Streamlit
# zona = palmeiras_cruzamentos[id]["zona"]
# figura_cortada = desenhar_campo_com_quadrado(lado_a,zona)
# st.pyplot(figura_cortada)
