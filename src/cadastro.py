from calendar import monthrange
from datetime import date
from relatorio import criarRelatorioDiario
from relatorio import criarRelatorioMensal
import json
import os


METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')
COSNUMOMENSALPATH = os.path.join('dados', 'consumo_mensal.json')


class Cadastro:
    def __init__(self):
        self.data_atual = date.today()
        self.dia = self.data_atual.day
        self.mes = self.data_atual.month
        self.ano = self.data_atual.year
        

    def cadastrarMeta(self, tarifa: int, meta: int):
        meta_ = {
            'data': self.data_atual.isoformat(),
            'mes_da_meta': self.mes,
            'dia_de_cadastro_da_meta': self.dia,
            'ultimo_dia_do_mes': monthrange(self.ano, self.mes)[1],
            'meta': meta,
            'tarifa': tarifa
        }
        
        with open(METAPATH, "w") as metas:
            json.dump(meta_, metas, indent=1)
            
    def cadastrarConsumo(self, consumo: int = 0):
        
        consumoMensal = consumo 

        consumo_ = {
            'consumo': consumo,
            'data': self.dia
        }
        
        with open(CONSUMOPATH, "w") as consumos: 
            json.dump(consumo_, consumos,  indent=4)        
        
        if self.dia != monthrange(self.ano, self.mes)[1]:
            return criarRelatorioDiario
        
        else:
            return criarRelatorioMensal
