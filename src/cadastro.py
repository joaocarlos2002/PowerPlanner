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
        
        with open(os.path.join("dados", "meta.json"), "w") as metas:
            json.dump(meta_, metas,indent=1)
            
    def cadastrarConsumo(self, consumo: int = 0):
        lista_de_consumidos = []
        consumo_ = {
                    'consumo': consumo,
                    'dia': date.day
                }
        if not os.path.exists('dados'):
            os.makedirs('dados')
        
        if os.path.exists(CONSUMOPATH):
            with open(CONSUMOPATH, "w") as consumos:
                consumoAnterior = json.load(consumos[0][self.mes])
                lista_de_consumidos.append(consumoAnterior)
                
                
        else:
            with open(CONSUMOPATH, "w") as consumos:


                lista_do_mes = [{
                    f'{self.mes}': [consumo_]
                }]
                
                json.dump(lista_do_mes)
            
        
        
        
        

        
                

                

                
                




      
teste = Cadastro()
teste.cadastrarConsumo(100)
# teste