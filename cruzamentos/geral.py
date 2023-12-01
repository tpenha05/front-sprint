import json
from cruz_funcoes import *

# Abre o arquivo JSON e lê seu conteúdo
with open('cruzamentos.json', 'r') as arquivo:
    dados_dict = json.load(arquivo)


""" Aqui eu assumo que o Palmeiras sempre será o time 1, separando os cruzamentos do Palmeiras e do RedBull,
    sabendo que poderia ser qualquer outro time jogando contra o Palmeiras, eu assumo que o adversário 
    é aquele cujo o id é diferente do id palmeirense. """
palmeiras = dados_dict["time"]["1"]
for time in dados_dict["time"]:
    if time != "1":
        adversario = dados_dict["time"][time]

#lista de dicionarios contendo todos os cruzamentos dos respectivos times
palmeiras_cruzamentos = palmeiras["rupturas"]
adversario_cruzamentos = adversario["rupturas"]


# Nome dos times.
nome_palmeiras = palmeiras["nome"]
nome_adversario = adversario["nome"]

#aparições nos ataques das equipes.
#palmeiras
aparicoes_palmeiras_ataque = {}
n_aparicoes_palmeiras_ataque = {}
for id in range(len(palmeiras_cruzamentos)):
    aparicoes_palmeiras_ataque = conta_aparicoes_ataque("nome",palmeiras_cruzamentos[id], aparicoes_palmeiras_ataque)
    n_aparicoes_palmeiras_ataque = conta_aparicoes_ataque("numero",palmeiras_cruzamentos[id], n_aparicoes_palmeiras_ataque)
#Adversário
aparicoes_adversario_ataque = {}
n_aparicoes_adversario_ataque = {}
for id in range(len(adversario_cruzamentos)):
    aparicoes_adversario_ataque = conta_aparicoes_ataque("nome",adversario_cruzamentos[id], aparicoes_adversario_ataque)
    n_aparicoes_adversario_ataque = conta_aparicoes_ataque("numero",adversario_cruzamentos[id], n_aparicoes_adversario_ataque)

#destaques das equipes
#palmeiras
destaques_pal = dict(sorted(aparicoes_palmeiras_ataque.items(), key=lambda item: item[1], reverse=True)[:5])
#adversário
destaques_adv = dict(sorted(aparicoes_adversario_ataque.items(), key=lambda item: item[1], reverse=True)[:5])


#porcentagem por zona (frequência)
porcentagem_pal = porcentagem_zona(palmeiras_cruzamentos, len(palmeiras_cruzamentos))
porcentagem_adv = porcentagem_zona(adversario_cruzamentos, len(adversario_cruzamentos))


#Busca zona da jogada.
zona = busca_zona(palmeiras_cruzamentos[5])
print(zona)


#Pega tempo do cruzamento por id e transforma em segundos
tempo = pega_tempo_cruzamento(palmeiras_cruzamentos[5])
print(tempo)

#Pega os desfechos dos cruzamentos
desfechos_pal = calcula_desfecho(palmeiras_cruzamentos)
desfechos_adv = calcula_desfecho(adversario_cruzamentos)



# Dicionario contendo valores (feitos a mão) para desenhar o campo
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

escrita_a = {"E2.2": [3, 6, 0.5, 2],
                 "E2.1": [14, 6, 12.5, 2],
                 "E1.2": [25.5, 6, 24, 2],
                 "E1.1": [25.5, 20, 24, 16],
                 "E3": [9, 16, 6.5, 12],
                 "D2.2": [3, 55, 0.5, 51],
                 "D2.1": [14, 55, 12.5, 51],
                 "D1.2": [25.5, 55, 24, 51],
                 "D1.1": [25.5, 40, 24, 36],
                 "D3": [9, 46, 6.5, 42],
                 }

escrita_b = {"E2.2": [92, 55, 89.5, 51],
                 "E2.1": [80, 55, 78.5, 51],
                 "E1.2": [70, 55, 67.5, 51],
                 "E1.1": [70, 40, 67.5, 36],
                 "E3": [86, 46, 84.5, 42],
                 "D2.2": [93,6,89.5,2],
                 "D2.1": [80,6,78.5,2],
                 "D1.2": [70,6,67.5,2],
                 "D1.1": [70,20,67.5,16],
                 "D3": [86,16,84.5,12],
                 }