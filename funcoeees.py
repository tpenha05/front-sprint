def ataque(dic_do_cruzamento, dic_jogadores_ataque):
    jogadores_ataque = dic_do_cruzamento["nome_jogadores_time_cruzando"]
    lista_jogadores_ataque = jogadores_ataque.replace(" ", "").split(",")
    for jogador in lista_jogadores_ataque:
        if jogador not in dic_jogadores_ataque:
            dic_jogadores_ataque[jogador] = 1
        elif jogador in dic_jogadores_ataque:
            dic_jogadores_ataque[jogador] +=1
    return dic_jogadores_ataque

def defesa(dic_do_cruzamento, dic_jogadores_defesa):
    jogadores_defesa = dic_do_cruzamento["nome_jogadores_time_defendendo"]
    lista_jogadores_defesa = jogadores_defesa.replace(" ", "").split(",")
    for jogador in lista_jogadores_defesa:
        if jogador not in dic_jogadores_defesa:
            dic_jogadores_defesa[jogador] = 1
        elif jogador in dic_jogadores_defesa:
            dic_jogadores_defesa[jogador] +=1
    return dic_jogadores_defesa

def resultado_cruzamentos(dic_do_cruzamento, dic_resultados):
    desfecho = dic_do_cruzamento["desfecho"]
    if desfecho not in dic_resultados:
        dic_resultados[desfecho] = 1
    elif desfecho in dic_resultados:
        dic_resultados[desfecho] +=1
    return dic_resultados

def desfecho_por_quantidade(dic_do_cruzamento,dic_desfechos_quant):
    n_ataque = dic_do_cruzamento["quantidade_jogadores_time_atacando"]
    n_defesa = dic_do_cruzamento["quantidade_jogadores_defendendo"]
    if n_ataque > n_defesa :
        desfecho = dic_do_cruzamento["desfecho"]
        if desfecho not in dic_desfechos_quant:
            # dic_desfechos_quant["ataque maior"] = {}
            dic_desfechos_quant["ataque maior"][desfecho] = 1
        elif desfecho in dic_desfechos_quant:
            dic_desfechos_quant["ataque maior"][desfecho] +=1
        return dic_desfechos_quant
    elif n_ataque == n_defesa:
        desfecho = dic_do_cruzamento["desfecho"]
        if desfecho not in dic_desfechos_quant:
            dic_desfechos_quant["ataque igual"][desfecho] = 1
        elif desfecho in dic_desfechos_quant:
            dic_desfechos_quant["ataque igual"][desfecho] +=1
        return dic_desfechos_quant
    else: 
        desfecho = dic_do_cruzamento["desfecho"]
        if desfecho not in dic_desfechos_quant:
            dic_desfechos_quant["ataque menor"][desfecho] = 1
        elif desfecho in dic_desfechos_quant:
            dic_desfechos_quant["ataque menor"][desfecho] +=1
        return dic_desfechos_quant
    

def numero_ataque(dic_do_cruzamento, dic_jogadores_ataque):
    jogadores_ataque = dic_do_cruzamento["numero_jogadores_time_cruzando"]
    lista_jogadores_ataque = jogadores_ataque.replace(" ", "").split(",")
    for jogador in lista_jogadores_ataque:
        if jogador not in dic_jogadores_ataque:
            dic_jogadores_ataque[jogador] = 1
        elif jogador in dic_jogadores_ataque:
            dic_jogadores_ataque[jogador] +=1
    return dic_jogadores_ataque

def numero_defesa(dic_do_cruzamento, dic_jogadores_defesa):
    jogadores_defesa = dic_do_cruzamento["numero_jogadores_time_defendendo"]
    lista_jogadores_defesa = jogadores_defesa.replace(" ", "").split(",")
    for jogador in lista_jogadores_defesa:
        if jogador not in dic_jogadores_defesa:
            dic_jogadores_defesa[jogador] = 1
        elif jogador in dic_jogadores_defesa:
            dic_jogadores_defesa[jogador] +=1
    return dic_jogadores_defesa