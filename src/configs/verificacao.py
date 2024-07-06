from calendar import monthrange
from configs.relatorio import criarRelatorioDiario
from configs.relatorio import criarRelatorioMensal



def verificar(dia: int = 1, mes: int = 1, ano: int = 1, consumo: int = 0):
    if dia != monthrange(ano, mes)[1]:
        return criarRelatorioDiario()
    else:
        return criarRelatorioMensal(consumo)
    

    
