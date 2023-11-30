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
# print(porcentagem_adv, porcentagem_pal)


#Busca zona da jogada.
zona = busca_zona(palmeiras_cruzamentos[5])
print(zona)


#Pega tempo do cruzamento por id e transforma em segundos
tempo = pega_tempo_cruzamento(palmeiras_cruzamentos[5])
print(tempo)

#Pega os desfechos dos cruzamentos
desfechos_pal = calcula_desfecho(palmeiras_cruzamentos)
desfechos_adv = calcula_desfecho(adversario_cruzamentos)
