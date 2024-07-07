from configs.cadastro import Cadastro
import os
import json
from calendar import monthrange
from datetime import date
import random


METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')


def gerarTarifaAleatoria() -> float:
    return random.uniform(0.1, 3)

def gerarMetaAleatoria() -> float:
    return random.uniform(199, 10000)

def gerarConsumoAleatorio() -> float:
    return random.uniform(0, 100)


def app():

    cadastro = Cadastro()
    data = date.today()

    with open(CONSUMOPATH, 'r') as consumo:
        consumo_ = json.load(consumo)

    with open(METAPATH , 'r') as metas:
        metas_ = json.load(metas)


    if consumo_['data'] == data.day:
         pass
    else:
        cadastro.cadastrarConsumo(gerarConsumoAleatorio)

    if metas_['ultimo_dia_do_mes'] == data.day:
        cadastro.cadastrarMeta(gerarTarifaAleatoria, gerarMetaAleatoria)
    else:
        pass


if __name__ == "__main__":
    app()