import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st

# Função para desenhar o campo de futebol dividido em 9 partes no eixo x e 6 partes no eixo y
def desenhar_campo_dividido():
    fig, ax = plt.subplots(figsize=(8, 5))

    # Definindo o tamanho do campo
    largura_campo = 100
    altura_campo = 70

    # Desenhando o campo de futebol
    retangulo_campo = patches.Rectangle((0, 0), largura_campo, altura_campo, linewidth=2, edgecolor='green', facecolor='none')

    # Dividindo o campo em 9 partes no eixo x
    for i in range(1, 9):
        linha_divisao_x = patches.ConnectionPatch((largura_campo / 9 * i, 0), (largura_campo / 9 * i, altura_campo), "data", "data", edgecolor='green', linestyle='dashed')
        ax.add_patch(linha_divisao_x)

    # Dividindo o campo em 6 partes no eixo y
    for j in range(1, 6):
        linha_divisao_y = patches.ConnectionPatch((0, altura_campo / 6 * j), (largura_campo, altura_campo / 6 * j), "data", "data", edgecolor='green', linestyle='dashed')
        ax.add_patch(linha_divisao_y)

    ax.add_patch(retangulo_campo)

    # Adicionando informações
    plt.text(5, 35, "Jogador A", fontsize=10, color='red')
    plt.text(80, 20, "Jogador B", fontsize=10, color='blue')

    # Configurações do gráfico
    plt.xlim(-5, largura_campo + 5)
    plt.ylim(-5, altura_campo + 5)
    plt.axis('off')

    return fig

# Exibindo o campo de futebol dividido no Streamlit
figura = desenhar_campo_dividido()
st.pyplot(figura)
