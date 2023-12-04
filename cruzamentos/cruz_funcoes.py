def conta_aparicoes_ataque(n_ou_nome, cruzamento, dic_aparicoes):
    jogadores_ataque = cruzamento[f"{n_ou_nome}_jogadores_time_cruzando"]
    lista_jogadores_ataque = jogadores_ataque.replace(" ", "").split(",")
    for jogador in lista_jogadores_ataque:
        if jogador not in dic_aparicoes:
            dic_aparicoes[jogador] = 1
        elif jogador in dic_aparicoes:
            dic_aparicoes[jogador] +=1
    return dic_aparicoes

def calcula_desfecho(lista_cruzamentos):
    desfechos = {}
    for id in range(len(lista_cruzamentos)):
        resultado = lista_cruzamentos[id]["desfecho"]
        if resultado not in desfechos:
            desfechos[resultado] = 1
        elif resultado in desfechos:
            desfechos[resultado] +=1
    return desfechos

def cria_dic_zona(dicionario_cruz):
    dic_zonas = {"D1.1": 0,
                 "D1.2": 0,
                 "D2.1": 0,
                 "D2.2": 0,
                 "D3" : 0,
                 "E1.1": 0,
                 "E1.2": 0,
                 "E2.1": 0,
                 "E2.2": 0,
                 "E3" : 0
                 }
    for cruzamento in dicionario_cruz:
        if cruzamento["zona"] not in dic_zonas:
            dic_zonas[cruzamento["zona"]] = 1
        else:
            dic_zonas[cruzamento["zona"]] += 1
    return dic_zonas

def porcentagem_zona(dicionario_cruzamento, tamanho):
    dic_zonas = cria_dic_zona(dicionario_cruzamento)
    for chave in dic_zonas:
        dic_zonas[chave] = dic_zonas[chave] / tamanho * 100
    return dic_zonas

def busca_zona(cruzamento):
    return cruzamento["zona"]

def jogadores_ataque(cruzamento):
    return cruzamento["nome_jogadores_time_cruzando"].split(",")

def jogadores_defesa(cruzamento):
    return cruzamento["nome_jogadores_time_defendendo"].split(",")

def pega_tempo_cruzamento(cruzamento):
    tempo = cruzamento["instante_cruzamento"].split(":")
    tempo = int(tempo[0])*3600 + int(tempo[1])*60 + int(tempo[2])
    return tempo
