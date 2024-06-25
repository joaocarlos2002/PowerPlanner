from calendar import monthrange
from datetime import date
from relatorio import criarRelatorioDiario
import json
import os


METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')

class Cadastro:
    def __init__(self):
        self.data = date.today()
        self.dia = self.data.day
        self.mes = self.data.month
        self.ano = self.data.year

    def cadastrarMeta(self, tarifa: int, meta: int):
        meta_ = {
            'data': self.data.isoformat(),
            'mes_da_meta': self.mes,
            'dia_de_cadastro_da_meta': self.dia,
            'ultimo_dia_do_mes': monthrange(self.ano,self.mes )[1],
            'meta': meta,
            'tarifa': tarifa
        }
        
        with open(os.path.join("dados", "meta.json"), "w") as metas:
            json.dump(meta_, metas,indent=1)
            
    def cadastrarConsumo(self, consumo: int = 0):
        consumo_ = {
            'consumo': consumo,
            'dia': self.data.day
        }

        try:
            if not os.path.exists('dados'):
                os.makedirs('dados')

            if os.path.exists(CONSUMOPATH):
                with open(CONSUMOPATH, "r") as consumos:
                    listaConsumo = json.load(consumos)
            else:
                listaConsumo = []

            updated = False

            for item in listaConsumo:
                if item['dia'] == self.data.day:
                    item['consumo'] = consumo  
                    updated = True
                    break

            if not updated:
                listaConsumo.append(consumo_)

            with open(CONSUMOPATH, "w") as consumos:
                json.dump(listaConsumo, consumos, indent=1)

        except:
            print("Erro ao cadastrar consumo")



      
teste = Cadastro()
teste.cadastrarConsumo(100)
# teste