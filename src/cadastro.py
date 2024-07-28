
from relatorio import gerar_relatorio_mensal, gerar_relatorio_diario
from calendar import monthrange
from datetime import date
from gerarResultados import *
import os
import json


META_PATH = os.path.join('dados', 'meta.json')
MENSAL_PATH = os.path.join('dados', 'mensal.json')
MESES_PATH = os.path.join('dados', "meses.txt")
MESES_COMPARADOS_PATH = os.path.join('dados', "meses_comparados.json")


# arrumar o nome das funcoes [x]
# terminar de documentar []
# arrumar o codigo de todas as funcoes para ficar legivel []


def cadastrar_consumo_mensal(consumoDiario):

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


def enviar_dados_mensais():

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


def cadastrar_meta(tarifa, meta, data = date.today()):

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


def comparar_mes_com_a_meta(meta, consumido):
    """
    Compara o valor consumido com a meta e retorna a porcentagem do consumido em relação à meta.

    Parâmetros:
    meta (float): A meta estabelecida.
    consumido (float): O valor consumido.

    retorna:
    float: A porcentagem do valor consumido em relação à meta.

    Levanta:
    ValueError: Se `meta` ou `consumido` não forem do tipo float.
    ZeroDivisionError: Se `meta` for zero.
    """

    if not isinstance(meta, float):
        raise ValueError('A meta foi informada de forma errada. Deve ser um número do tipo float.')
    
    if not isinstance(consumido, float):
        raise ValueError('O consumido foi informado de forma errada. Deve ser um número do tipo float.')

    if meta == 0:
        raise ZeroDivisionError('A meta não pode ser zero.')

    try:
        porcentagem = (consumido * 100) / meta
        return porcentagem
    except Exception as e:
        raise RuntimeError(f'Ocorreu um erro ao calcular a porcentagem: {e}')


def verificar_total_economizado(meta, consumido):
    """
    Calcula o valor economizado com base na meta e no valor consumido.

    Parâmetros:
    meta (float): A meta estabelecida.
    consumido (float): O valor consumido.

    retorna:
    float: O valor economizado (meta - consumido).

    levanta:
    ValueError: Se `meta` ou `consumido` não forem do tipo float.
    """

    if not isinstance(meta, float):
        raise ValueError('A meta foi informada de forma errada. Deve ser um número do tipo float.')

    if not isinstance(consumido, float):
        raise ValueError('O consumido foi informado de forma errada. Deve ser um número do tipo float.')

    economizado = meta - consumido
    return economizado


def verificar_mes_que_mais_economizou(lista):

    lista_maior = []

    for i in lista:
        lista_maior.append(i[1])

    numeros_ordenados = sorted(lista_maior)
    return numeros_ordenados[0]


def salva_comparacao_de_meses(porcentagens_dos_meses_com_a_meta = [], total_economizado_em_cada_mes = [], mes_que_mais_economizou = []):


    with open(MESES_PATH, 'r') as arq:
        lista_com_resultado_de_todos_os_meses = json.load(arq)

    lista_de_porcentagens = []
    lista_do_total_economizado = []

    for i, j, k in lista_com_resultado_de_todos_os_meses:
        lista_de_porcentagens.append([i, comparar_mes_com_a_meta(j,k)])
        lista_do_total_economizado.append([i, verificar_total_economizado(j,k)])
    
    porcentagens_dos_meses_com_a_meta = lista_de_porcentagens
    total_economizado_em_cada_mes = lista_do_total_economizado
    mes_que_mais_economizou = verificar_mes_que_mais_economizou(lista_de_porcentagens)

    dict_mes = {
        "porcentagens_dos_meses_com_a_meta": porcentagens_dos_meses_com_a_meta,
        "total_economizado_em_cada_mes": total_economizado_em_cada_mes,
        "mes_que_mais_economizou": mes_que_mais_economizou

    }

    with open (MESES_COMPARADOS_PATH, "w") as arq:
        json.dump(dict_mes,arq, indent=1)
        


def salvar_dados_para_comparar_os_meses(mes = date.today().month, lista_com_resultado_de_todos_os_meses = []):
    
    '''
        FALTA ARRUMAR O CODIGO E DOCUMENTAR
    '''
    with open(META_PATH, 'r') as arq:
        meta_ = json.load(arq)

    
    lista_de_consumo_deste_mes = [mes, meta_["meta"]]

    with open(MENSAL_PATH, 'r') as arq:
        consumido_neste_mes = json.load(arq)

    lista_de_consumo_deste_mes.append(consumido_neste_mes)

    try: 
        with open(MESES_PATH, 'r') as arq:
            lista_com_resultado_de_todos_os_meses = json.load(arq)
        
        lista_com_resultado_de_todos_os_meses.append(lista_de_consumo_deste_mes)

    except:
        print('teste123')

    with open(MESES_PATH, 'w') as meses:
        json.dump(lista_com_resultado_de_todos_os_meses, meses)


def cadastrar_consumo (consumo, data = date.today()):

    '''
        Serve para gerar o relatorio diario ou mensal

        Parâmetros:
        consumo: é o consumo informado pelo usuario 
    
    '''

    try:
        if not isinstance(consumo, float):
            raise ValueError(f'O consumo deve ser um float')
        
        cadastrar_consumo_mensal(consumo)

        if data.day != monthrange(data.year, data.month)[1]:
            return gerar_relatorio_diario(consumo)

        return gerar_relatorio_mensal(enviar_dados_mensais())
    
    except Exception as e:
        print(f'Um erro aconteceu no {e}')
        raise


# salva_comparacao_de_meses()