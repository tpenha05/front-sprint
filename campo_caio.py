import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st

# Função para desenhar o campo de futebol com um quadrado abrangendo os quadrados selecionados
def desenhar_campo(Lista_porcentagem=None):
    if Lista_porcentagem is None:
        return None
    fig, ax = plt.subplots(figsize=(8, 5))

    # Definindo o tamanho do campo
    largura_campo = 100
    altura_campo = 60

    # Desenhando o campo de futebol com a cor verde
    retangulo_campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, edgecolor='black', facecolor='green')
    ax.add_patch(retangulo_campo)





    # Dividindo o campo em 5 partes com linhas verticais
    for i in range(1, 5):
        plt.plot([i * largura_campo / 5, i * largura_campo / 5], [0, altura_campo], color='gray')

    # Adicionando uma linha na metade do campo
    meio_campo = largura_campo / 2
    plt.plot([meio_campo, meio_campo], [0, altura_campo], color='white')

    # Adicionando um círculo no meio do campo com apenas o contorno
    raio_circulo = 3
    circulo = patches.Circle((meio_campo, altura_campo / 2), raio_circulo, edgecolor='white', facecolor='none', linewidth=2)
    ax.add_patch(circulo)

    raio_circulo = 0.5
    circulo = patches.Circle((meio_campo, altura_campo / 2), raio_circulo, edgecolor='white', facecolor='none', linewidth=2)
    ax.add_patch(circulo)

    raio_circulo = 0.5
    circulo = patches.Circle((85, altura_campo / 2), raio_circulo, edgecolor='white', facecolor='none', linewidth=2)
    ax.add_patch(circulo)

    raio_circulo = 0.5
    circulo = patches.Circle((15, altura_campo / 2), raio_circulo, edgecolor='white', facecolor='none', linewidth=2)
    ax.add_patch(circulo)


    # Adicionando retângulos representando as áreas do campo
    altura_area = altura_campo / 2.5  # Ajuste para um meio-termo
    area_lado_esquerdo = patches.Rectangle((0, altura_campo / 2 - altura_area / 2), largura_campo / 5, altura_area, linewidth=2, edgecolor='white', facecolor='none')
    area_goleiro_esquerdo = patches.Rectangle((0,22), largura_campo / 14, 16, linewidth=2, edgecolor='white', facecolor='none')

    area_lado_direito = patches.Rectangle((largura_campo - largura_campo / 5, altura_campo / 2 - altura_area / 2), largura_campo / 5, altura_area, linewidth=2, edgecolor='white', facecolor='none')
    area_goleiro_direito = patches.Rectangle((93,22), largura_campo / 14, 16, linewidth=2, edgecolor='white', facecolor='none')


    plt.text(7, 50, f"{Lista_porcentagem[2]}", fontsize=10, color='White') #cor da escrita "Área"
    plt.text(26, 50, f"{Lista_porcentagem[4]}", fontsize=10, color='White') #cor da escrita "Área"
    plt.text(50, 50,f"", fontsize=10, color='black') #cor da escrita "Área"
    plt.text(66, 50, f"{Lista_porcentagem[0]}", fontsize=10, color='White') #cor da escrita "Área"
    plt.text(86, 50, f"{Lista_porcentagem[6]}", fontsize=10, color='White') #cor da escrita "Área"

    
    #só tirar a "porcentagem" e colocar a porcentagem respectiva da àrea!!!!!
    plt.text(2, 45, f"  {Lista_porcentagem[1]}", fontsize=14, color='White') #cor da escrita "Área"
    plt.text(22, 45, f"  {Lista_porcentagem[3]}", fontsize=14, color='White') #cor da escrita "Área"
    plt.text(42, 45, f" ", fontsize=14, color='black') #cor da escrita "Área"
    plt.text(62, 45, f"  {Lista_porcentagem[5]}", fontsize=14, color='White') #cor da escrita "Área"
    plt.text(82, 45, f"  {Lista_porcentagem[7]}", fontsize=14, color='White') #cor da escrita "Área"


    


    ax.add_patch(area_lado_esquerdo)
    ax.add_patch(area_goleiro_esquerdo)

    ax.add_patch(area_lado_direito)
    ax.add_patch(area_goleiro_direito)

    # Configurações do gráfico
    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    return fig

# Exibindo o campo de futebol com o quadrado abrangente no Streamlit
figura = desenhar_campo()
st.pyplot(figura)
