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
        self.dia = date.day
        self.mes = date.month
        self.ano = date.year
        

    def cadastrarMeta(self, tarifa: int, meta: int):
        meta_ = {
            'data': self.data.isoformat(),
            'mes_da_meta': self.mes,
            'dia_de_cadastro_da_meta': self.dia,
            'ultimo_dia_do_mes': monthrange(self.ano,self.mes )[1],
            'meta': meta,
            'tarifa': tarifa
        }
        
        with open(METAPATH, "w") as metas:
            json.dump(meta_, metas,indent=1)
            
    def cadastrarConsumo(self, consumo: int = 0):
        
        consumoMensal = consumo 

        consumo_ = {
            'consumo': consumo,
            'data': str(self.dia),
        }
        
        with open(CONSUMOPATH, "w") as consumos:  
            json.dump(consumo_, consumos, indent=4)
            
        # criarRelatorioDiario()            
        
        # if self.dia != monthrange(self.ano,self.mes )[1]:
        #     criarRelatorioDiario()
        # else:
        #     criarRelatorioMensal(consumoMensal, self.mes.strftime("%B"))

teste = Cadastro()
teste.cadastrarConsumo(1212312313120)

# teste