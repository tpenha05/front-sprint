import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
from geral import *

def faz_quadrado(largura_campo,altura_campo,lista):
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6
    retangulo_destaque = patches.Rectangle((largura_quad * lista[0], altura_quad * lista[2]), largura_quad * (lista[1] - lista[0] + 1), altura_quad * (lista[3] - lista[2] + 1), linewidth=1, edgecolor='red', facecolor='none')
    return retangulo_destaque
    

# Função para desenhar o campo de futebol com um quadrado abrangendo os quadrados selecionados
def desenhar_campo_com_quadrado(porcentagem_pal, porcentagem_adv, lado_a, lado_b):
    fig, ax = plt.subplots(figsize=(8, 5))
   
    lado_a = {"D1.1": [2,2,3,4],
              "D1.2": [2,2,5,5],
              "D2.1": [1,1,5,5],
              "D2.2": [0,0,5,5],
              "D3": [0,1,4,4],
              "E1.1": [2,2,1,2],
              "E1.2": [2,2,0,0],
              "E2.1": [1,1,0,0],
              "E2.2": [0,0,0,0],
              "E3": [0,1,1,1]
}
    lado_b = {"D1.1": [6,6,1,2],
              "D1.2": [6,6,0,0],
              "D2.1": [7,7,0,0],
              "D2.2": [8,8,0,0],
              "D3": [7,8,1,1],
              "E1.1": [6,6,3,4],
              "E1.2": [6,6,5,5],
              "E2.1": [7,7,5,5],
              "E2.2": [8,8,5,5],
              "E3": [7,8,4,4]}

    # Definindo o tamanho do campo
    largura_campo = 100
    altura_campo = 60

    # Desenhando o campo de futebol
    retangulo_campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, edgecolor='green', facecolor='none')

    # Adicionando o retângulo abrangendo os quadrados (0, 2), (0, 3), (1, 2) e (1, 3)
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6
    retangulo_destaque = patches.Rectangle((largura_quad * 0, altura_quad * 2), largura_quad * (1 - 0 + 1), altura_quad * (3 - 2 + 1), linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(retangulo_destaque)

    # #area outro lado
    retangulo_destaque = patches.Rectangle((largura_quad * 7, altura_quad * 2), largura_quad * (8 - 7 + 1), altura_quad * (3 - 2 + 1), linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(retangulo_destaque)

    #quadrados do Campo, Lado A
    for parte in lado_a:
        retangulo_destaque = faz_quadrado(largura_campo,altura_campo,lado_a[parte])
        ax.add_patch(retangulo_destaque)
    
    #quadrados do Campo, Lado B
    for parte in lado_b:
        retangulo_destaque = faz_quadrado(largura_campo,altura_campo,lado_b[parte])
        ax.add_patch(retangulo_destaque)
    
    ax.add_patch(retangulo_campo)

    # Adicionando informações
    plt.text(8, 28, "Área", fontsize=10, color='blue')
    plt.text(86, 28, "Área", fontsize=10, color='blue')

    #escrever o Nome da Área e A porcentagem
    #E2.2
    plt.text(3, 6, "E2.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["E2.2"]
    plt.text(0.5, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E2.1
    plt.text(14, 6, "E2.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["E2.1"]
    plt.text(12.5, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E1.2
    plt.text(25.5, 6, "E1.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["E1.2"]
    plt.text(24, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E1.1
    plt.text(25.5, 20, "E1.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["E1.1"]
    plt.text(24, 16, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E3
    plt.text(9, 16, "E3", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["E3"]
    plt.text(6.5, 12, f"{porcentagem: .2f}%", fontsize=10, color='black')

    #areas D
    #D2.2
    plt.text(3, 55, "D2.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["D2.2"]
    plt.text(0.5, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D2.1
    plt.text(14, 55, "D2.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["D2.1"]
    plt.text(12.5, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D1.2
    plt.text(25.5, 55, "D1.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["D1.2"]
    plt.text(24, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D1.1
    plt.text(25.5, 40, "D1.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["D1.1"]
    plt.text(24, 36, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D3
    plt.text(9, 46, "D3", fontsize=10, color='blue')
    porcentagem  = porcentagem_pal["D3"]
    plt.text(6.5, 42, f"{porcentagem: .2f}%", fontsize=10, color='black')


    #escrever o Nome da Área e B porcentagem
    #E2.2
    plt.text(92, 55, "E2.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["E2.2"]
    plt.text(89.5, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E2.1
    plt.text(80, 55, "E2.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["E2.1"]
    plt.text(78.5, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E1.2
    plt.text(70, 55, "E1.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["E1.2"]
    plt.text(68, 51, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E1.1
    plt.text(70, 40, "E1.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["E1.1"]
    plt.text(67.5, 36, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #E3
    plt.text(86, 46, "E3", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["E3"]
    plt.text(84.5, 42, f"{porcentagem: .2f}%", fontsize=10, color='black')

    #areas D
    #D2.2
    plt.text(93, 6, "D2.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["D2.2"]
    plt.text(89.5, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D2.1
    plt.text(80, 6, "D2.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["D2.1"]
    plt.text(78.5, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D1.2
    plt.text(70, 6, "D1.2", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["D1.2"]
    plt.text(68.5, 2, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D1.1
    plt.text(70, 20, "D1.1", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["D1.1"]
    plt.text(67.5, 16, f"{porcentagem: .2f}%", fontsize=10, color='black')
    #D3
    plt.text(86, 16, "D3", fontsize=10, color='blue')
    porcentagem  = porcentagem_adv["D3"]
    plt.text(84.5, 12, f"{porcentagem: .2f}%", fontsize=10, color='black')


    # Configurações do gráfico
    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    return fig

