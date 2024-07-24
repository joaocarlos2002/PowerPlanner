from cadastro import cadastrar_consumo 
from cadastro import cadastrar_meta
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
        cadastrar_consumo (gerarConsumo()) 
        cadastrar_meta(gerarTarifa(), gerarMeta()) 
        
    else: 
        cadastrar_consumo (gerarConsumo()) 
        
if __name__ == '__main__':
    app()