import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
from PIL import Image
import io

def faz_campinho(largura_campo,altura_campo,lista):
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6
    retangulo_destaque = patches.Rectangle((largura_quad * lista[0], altura_quad * lista[2]), largura_quad * (lista[1] - lista[0] + 1), altura_quad * (lista[3] - lista[2] + 1), linewidth=1, edgecolor='red', facecolor='none')
    return retangulo_destaque
    

# Função para desenhar o campo de futebol com um quadrado abrangendo os quadrados selecionados
def desenho_zona(local):
    fig, ax = plt.subplots(figsize=(8, 5))
    x1 = 0
    x2 = 1
    x3 = 2
    x4 = 3
    x5 = 4
    x6 = 5
    x7 = 6
    x8 = 7
    x9 = 8

    y1 = 0
    y2 = 1
    y3 = 2
    y4 = 3
    y5 = 4
    y6 = 5
    lado_a = {"D1.1": [x3,x3,y4,y5],
              "D1.2": [x3,x3,y6,y6],
              "D2.1": [x2,x2,y6,y6],
              "D2.2": [x1,x1,y6,y6],
              "D3": [x1,x2,y5,y5],
              "E1.1": [x3,x3,y2,y3],
              "E1.2": [x3,x3,y1,y1],
              "E2.1": [x2,x2,y1,y1],
              "E2.2": [x1,x1,y1,y1],
              "E3": [x1,x2,y2,y2]
}
    # Definindo o tamanho do campo
    largura_campo = 50
    altura_campo = 60

    # Desenhando o campo de futebol
    retangulo_campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, edgecolor='green', facecolor='none')

    # Adicionando o retângulo abrangendo os quadrados (x1, y3), (x1, y4), (x2, y3) e (x2, y4)
    largura_quad = largura_campo / 9
    altura_quad = altura_campo / 6
    plt.text(4, 28, "Área", fontsize=10, color='white')
    retangulo_destaque = patches.Rectangle((largura_quad * x1, altura_quad * y3), largura_quad * (x2 - x1 + 1), altura_quad * (y4 - y3 + 1), linewidth=1, edgecolor='red', facecolor='none')
    retangulo_destaque.set_facecolor('red')
    ax.add_patch(retangulo_destaque)
    ax.add_patch(retangulo_campo)

    plt.ylim(0, altura_campo)  # Define os limites do eixo Y
    plt.axvline(x=largura_campo / 2.1, color='green', linestyle='-', linewidth=1)



    #quadrados do Campo, Lado A
    for parte in lado_a:
        retangulo_destaque = faz_campinho(largura_campo,altura_campo,lado_a[parte])
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)
    

    #Preenche o quadrado respectivo do local do campo que saiu o cruzamento.
    for parte in lado_a:
        retangulo_destaque = faz_campinho(largura_campo, altura_campo, lado_a[parte])
        # Adicionando preenchimento colorido a alguns quadrados
        if parte in [local]:
            retangulo_destaque.set_facecolor('orange')
        else:
            retangulo_destaque.set_facecolor('none')  # Mantém outros quadrados sem preenchimento
        ax.add_patch(retangulo_destaque)
        ax.add_patch(retangulo_campo)

    #escrever o Nome da Área e A porcentagem
    #E2.2
    plt.text(1.5, 3.5, "E2.2", fontsize=10, color='blue')
    #E2.1
    plt.text(7, 3.5, "E2.1", fontsize=10, color='blue')
    #E1.2
    plt.text(12.5, 3.5, "E1.2", fontsize=10, color='blue')
    #E1.1
    plt.text(12.5, 18, "E1.1", fontsize=10, color='blue')
    #E3
    plt.text(4.5, 14, "E3", fontsize=10, color='blue')

    #areas D
    #D2.2
    plt.text(1.5, 53.5, "D2.2", fontsize=10, color='blue')
    #D2.1
    plt.text(7, 53.5, "D2.1", fontsize=10, color='blue')
    #D1.2
    plt.text(12.5, 53.5, "D1.2", fontsize=10, color='blue')
    #D1.1
    plt.text(12.5, 40, "D1.1", fontsize=10, color='blue')
    #D3
    plt.text(4.5, 44, "D3", fontsize=10, color='blue')
    

    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    # Salvar a figura como uma imagem em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Carregar a imagem gerada pelo Matplotlib
    imagem_matplotlib = Image.open(buffer)

    # Obter as dimensões da imagem gerada
    largura, altura = imagem_matplotlib.size

    # Definir a região de corte (pegando apenas a parte da esquerda)
    regiao_corte = (0, 0, largura // 2, altura)  # Corta da esquerda até a metade da largura

    # Aplicar o corte na imagem gerada pelo Matplotlib
    parte_esquerda = imagem_matplotlib.crop(regiao_corte)

    return parte_esquerda

