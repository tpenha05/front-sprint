from funcoes_cruzamentos import dic_cruzamentos
from funcoeees import ataque, defesa, resultado_cruzamentos, desfecho_por_quantidade, numero_ataque, numero_defesa
from collections import OrderedDict


#dicionarios para filtros
defesas_por_time = {}
ataques_por_time = {}
resultados_por_time = {}
desfechos_quant_por_time = {}
participacao_def_por_time = {}
participacao_ataque_por_time = {}


#time = id do time, "5" para o redbull e "1" para o palmeiras
for time in dic_cruzamentos["time"]:
    # Sub-dicionarios para filtros
    aparicoes_defesa= {}
    aparicoes_ataque= {}
    dic_resultados = {}
    dic_desfechos_quant = {}
    dic_part_def= {}
    dic_part_ataque = {}

    cruzamentos = dic_cruzamentos["time"][time]["rupturas"]
    for cruzamento in cruzamentos:
       
        #recolhendo dados da defesa
        aparicoes_defesa = defesa(cruzamento,aparicoes_defesa)

        #recolhendo dados do ataque
        aparicoes_ataque = ataque(cruzamento,aparicoes_ataque)

        # resultados dos cruzamentos
        dic_resultados = resultado_cruzamentos(cruzamento, dic_resultados)

        # dic_desfechos_quant = desfecho_por_quantidade(cruzamento, dic_desfechos_quant)

        dic_part_ataque = numero_ataque(cruzamento,dic_part_ataque)

        dic_part_def = numero_ataque(cruzamento,dic_part_def)

 
    destaques = dict(sorted(aparicoes_ataque.items(), key=lambda item: item[1], reverse=True)[:5])


    defesas_por_time[f'adversario do {dic_cruzamentos["time"][time]["nome"]}'] = aparicoes_defesa
    ataques_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = aparicoes_ataque
    resultados_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_resultados
    desfechos_quant_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_desfechos_quant
    participacao_ataque_por_time[f'{dic_cruzamentos["time"][time]["nome"]}'] = dic_part_ataque
    participacao_def_por_time[f'adversário do {dic_cruzamentos["time"][time]["nome"]}'] = dic_part_def
    print (destaques)






palmeiras = dic_cruzamentos["time"]["1"]
redbull =  dic_cruzamentos["time"]["5"]
print (palmeiras)