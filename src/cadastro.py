from relatorio import gerarRelatorioDiario
from relatorio import gerarRelatorioMensal
from calendar import monthrange
from datetime import date
from gerarResultados import *
import os
import json


META_PATH = os.path.join('dados', 'meta.json')
MENSAL_PATH = os.path.join('dados', 'mensal.json')


def cadastrarConsumoMensal(consumoDiario):

    '''
        Cadastra o consumo mensal 

        Parâmetros
        consumoDiario: é o consumo informado pelo usuário, que no caso está sendo gerado automaticamente 

        Levanta
        FileNotFoundError: esse erro ocorre quando ele não encontra o MENSAL_PATH
        json.JSONDecodeError: Esse erro ocorre quando o Python tenta decodificar um arquivo JSON, mas não consegue porque o conteúdo do arquivo não está em um formato JSON válido.
        IOError: Esse erro ocorre quando há um problema ao tentar abrir ou ler um arquivo, como se o arquivo não existir ou não puder ser acessado por algum motivo.

    '''

    if not isinstance(consumoDiario, (float)):
        raise ValueError("O consumo diário deve ser float")

    try:
        if not os.path.exists(MENSAL_PATH):
            raise FileNotFoundError(f'O arquivo {MENSAL_PATH} não foi encontrado')
        
        with open(MENSAL_PATH, 'r') as mensal:
            consumido = json.load(mensal)
        
        if not isinstance(consumido, float):
            raise ValueError(f'O valor do consumo mensal deve ser um float')
        
        consumoMensal = consumido + consumoDiario

        with open(MENSAL_PATH, 'w') as mensal:
            json.dump(consumoMensal, mensal)


    except FileNotFoundError as arquivo_nao_encontrado:
        print(f'O arquivo {arquivo_nao_encontrado} não foi encontrado')
        raise

    except json.JSONDecodeError as decoder_mal_sucedida:
        print(f'não é possivel ler o arquivo json {decoder_mal_sucedida}')
        raise

    except IOError as leitura_mal_sucedida:
        print(f'Leitura do arquivo json foi mal sucedida {leitura_mal_sucedida}')
        raise

    except Exception as e:
        print(f' Um erro aconteceu {e}')
        raise


def enviarDadosMensais():

    '''
        serve para retornar o valor do consumo mensal para a função 'cadastrarConsumo'

        Parâmetros:
        não tem 

        Levanta
        FileNotFoundError: esse erro ocorre quando ele não encontra o MENSAL_PATH
        IOError: ocorrer quando existe um erro ao ler o arquivo     

    '''

    try:
        if not os.path.exists(MENSAL_PATH):
            raise FileNotFoundError(f'O arquivo {MENSAL_PATH} não foi encontrado')
        
        with open(MENSAL_PATH, 'r') as mensal:
            consumido = json.load(mensal)

        if not isinstance(consumido, float):
            raise ValueError(f'O valor do consumo mensal deve ser um float')   

        return consumido 
    

    except FileNotFoundError as arquivo_nao_encontrado:
        print(f'O arquivo {arquivo_nao_encontrado} não foi encontrado')
        raise

    except IOError as leitura_mal_sucedida:
        print(f'Leitura do arquivo json foi mal sucedida {leitura_mal_sucedida}')
        raise

    except Exception as e:
        print(f' Um erro aconteceu no {e}')


def cadastrarMeta(tarifa, meta, data = date.today()):

    '''
        serve para cadastrar a meta estabelecida no json respectivo 

        Parâmetros:
        tarifa: tarifa informada pelo usuario 
        meta: mmeta informada pelo usuario

        Levanta:
        FileNotFoundError: esse erro ocorre quando ele não encontra o MENSAL_PATH ou META_PATH
        json.JSONDecodeError: ocorrer quando existe um erro ao ler o arquivo
    
    '''

    try:
        if not isinstance(tarifa, float):
            raise ValueError(f'A tarifa foi informada errada')
        
        if not isinstance(meta, float):
            raise ValueError(f'A meta foi informada errada')
        
        if not os.path.exists(MENSAL_PATH):
            raise FileNotFoundError(f'O arquivo {MENSAL_PATH} não foi encontrado')
        
        meta_ = {
            'data': data.isoformat(),
            'mes_da_meta': data.month,
            'dia_de_cadastro_da_meta': data.day,
            'ultimo_dia_do_mes': monthrange(data.year, data.month)[1],
            'meta': meta,
            'tarifa': tarifa
        }

        with open(META_PATH, 'w') as metas:
            json.dump(meta_, metas, indent= 1)

    except FileNotFoundError as arquivo_nao_encontrado:
        print(f'O arquivo {arquivo_nao_encontrado} não foi encontrado')
        raise

    except json.JSONDecodeError as decoder_mal_sucedida:
        print(f'não é possivel ler o arquivo json {decoder_mal_sucedida}')
        raise
  
    except Exception as e:
        print(f'Um erro aconteceu no {e}')
        raise

def cadastrarConsumo(consumo, data = date.today()):

    '''
        Serve para gerar o relatorio diario ou mensal

        Parâmetros:
        consumo: é o consumo informado pelo usuario 
    
    
    '''

    try:
        if not isinstance(consumo, float):
            raise ValueError(f'O consumo deve ser um float')
        
        cadastrarConsumoMensal(consumo)

        if data.day != monthrange(data.year, data.month)[1]:
            gerarRelatorioDiario(consumo)
        else:
            gerarRelatorioMensal(enviarDadosMensais())
    
    except Exception as e:
        print(f'Um erro aconteceu no {e}')
        raise


