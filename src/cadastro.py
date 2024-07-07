from relatorio import gerarRelatorioDiario
from relatorio import gerarRelatorioMensal
from calendar import monthrange
from datetime import date
from gerarResultados import *
import os
import json





META_PATH = os.path.join('dados', 'meta.json')
MENSAL_PATH = os.path.join('dados', 'mensal.json')

def cadastrarConsumoMensal(consumoDiario):
    with open(MENSAL_PATH, 'r') as mensal:
        consumido = json.load(mensal)
    
    consumoMensal = consumido + consumoDiario

    with open(MENSAL_PATH, 'w') as mensal:
        json.dump(consumoMensal, mensal)

def enviarDadosMensais():
    with open(MENSAL_PATH, 'r') as mensal:
        consumido = json.load(mensal)

    return consumido 

def cadastrarMeta(tarifa, meta, data = date.today()):
    meta_ = {
        'data': data.isoformat(),
        'mes_da_meta': data.month,
        'dia_de_cadastro_da_meta': data.day,
        'ultimo_dia_do_mes': monthrange(data.year, data.month)[1],
        'meta': meta,
        'tarifa': tarifa
    }

    with open(META_PATH, 'w') as metas:
        json.dump(meta_, metas, indent= 1)

def cadastrarConsumo(consumo, data = date.today()):
    if data.day != monthrange(data.year, data.month)[1]:
        cadastrarConsumoMensal(consumo)
        gerarRelatorioDiario(consumo)
    else:
        cadastrarConsumoMensal(consumo) 
        gerarRelatorioMensal(enviarDadosMensais)


