from calendar import monthrange
from datetime import date
import json
import os



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
            
    def cadastrarConsumo(self, consumo):
        consumo_ = {
            'consumo': consumo,
            'dia': self.data.day
        }

        CAMINHO = os.path.join("dados", "consumo.json")
        
        with open(CAMINHO, "w") as consumos:
                json.dump(consumo_, consumos, indent=1)
      
