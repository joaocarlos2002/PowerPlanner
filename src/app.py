from cadastro import cadastrarConsumo
from cadastro import cadastrarMeta
from gerarResultados import *
from imprimir import *
from relatorio import *
from datetime import date



META_PATH = os.path.join('dados', 'meta.json')


def app():
    print(imprimirTextoInicial())
    
    
    data = date.today()

    with open(META_PATH, 'r') as metas:
        metas_ = json.load(metas)

    if data.day == metas_['ultimo_dia_do_mes']:
        cadastrarConsumo(gerarConsumo()) 
        cadastrarMeta(gerarTarifa(), gerarMeta()) 
        
    else: 
        cadastrarConsumo(gerarConsumo()) 
        
if __name__ == '__main__':
    app()