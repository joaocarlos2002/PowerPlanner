from calendar import monthrange
from datetime import date
from relatorio import criarRelatorioDiario
# from relatorio import criarRelatorioMensal
import json
import os


METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')
COSNUMOMENSALPATH = os.path.join('dados', 'consumo_mensal.json')



def cadastrarMeta( tarifa: float, meta: float):
    meta_ = {
        'data': date.day.isoformat(),
        'mes_da_meta': date.month,
        'ultimo_dia_do_mes': monthrange(date.year,date.month )[1],
        'meta': meta,
        'tarifa': tarifa
    }
        
    with open(METAPATH, "w") as metas:
        json.dump(meta_, metas,indent=1)
        
def CadastrarConsumo(consumido: int = 0):
    consumo_ = {
        'consumo': consumido,
        'dia': date.day
    }

    print(f'{consumo_}', date.day)

    with open(CONSUMOPATH, "w") as consumos:
        json.dump(consumo_, consumos, indent=1)

