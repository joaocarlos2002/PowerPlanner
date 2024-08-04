from cadastro import cadastrar_consumo, cadastrar_meta

# from gerarResultados import *
from imprimir import *
from relatorio import *
from datetime import date



META_PATH = os.path.join('dados', 'meta.json')
CONSUMO_PATH_RESULTS = os.path.join('results', f'Relatorio-{date.today()}.png')

with open(META_PATH, 'r') as metas:
        metas_ = json.load(metas)

data = date.today()

def app():
    while True:
        if data.day == metas_['ultimo_dia_do_mes']:
            try:
                consumo_diario = float(input('Digite o consumo diário: '))
                tarifa = float(input('Digite a tarifa: '))
                consumo_mensal = float(input('Digite o consumo mensal: '))

                return cadastrar_consumo(consumo_diario) and cadastrar_meta(tarifa, consumo_mensal)
            
            except ValueError:
                print('Digite um valor válido')
                continue
            
        else: 
            try:
                consumo_diario = float(input('Digite o consumo diário: '))
                return cadastrar_consumo(consumo_diario)
                
            except ValueError:
                print('Digite um valor válido')
                continue

if __name__ == '__main__':
    print(imprimirTextoInicial())

    print(data)
    print(os.path.exists(CONSUMO_PATH_RESULTS))

    if not os.path.exists(CONSUMO_PATH_RESULTS):
        app()

    else:
        print("Relatório já gerado")