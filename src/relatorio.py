from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import date
import os
import json


META_PATH = os.path.join('dados', 'meta.json')
CAMINHO_RESULTS = os.path.join('results')

FONTE = os.path.join('fontes', 'RubikOne-Regular.ttf')
IMAGEM = os.path.join('templates', 'relatorio.png')
IMAGEM_MENSAL = os.path.join('templates', 'relatorio_mensal.png')


def gerarRelatorioDiario(consumo):
    '''

    
    '''

    if not isinstance(consumo, (float)):
        raise ValueError("O consumo diário deve ser float")

    try:
        if not os.path.exists(IMAGEM):
            raise FileNotFoundError(f'O arquivo {IMAGEM} não foi encontrado')
        
        if not os.path.exists(CAMINHO_RESULTS):
            raise FileNotFoundError(f'O arquivo {CAMINHO_RESULTS} não foi encontrado')
        
        if not os.path.exists(META_PATH):
            raise FileNotFoundError(f'O arquivo {META_PATH} não foi encontrado')
        
        if not os.path.exists(FONTE):
            raise FileNotFoundError(f'O arquivo {FONTE} não foi encontrado')

        relatorio = Image.open(IMAGEM)
        draw = ImageDraw.Draw(relatorio)

        with open(META_PATH, "r") as metas:
            metas_ = json.load(metas)

        if not isinstance(metas_, dict):
            raise ValueError(f'O valor de meta_ deve ser um dict')

        custoPorDiaPrevisto = (metas_['meta'] / 30) * metas_['tarifa']

        if not isinstance(custoPorDiaPrevisto, float):
            raise ValueError(f'O valor de custoPorDiaPrevisto deve ser um float')

        consumoPorDiaPrevisto = (metas_['meta'] / 30)

        if not isinstance(consumoPorDiaPrevisto, float):
                    raise ValueError(f'O valor de consumoPorDiaPrevisto deve ser um float')

        meta = (metas_['meta'])

        if not isinstance(meta, float):
            raise ValueError(f'O valor de meta deve ser um str')

        CustoDiario = consumo * metas_['tarifa']

        if not isinstance(CustoDiario, float):
            raise ValueError(f'O valor de CustoDiario deve ser um float')

        try:
            draw.text((675,470), metas_['data'], font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((675,600), f'{meta:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((675,730), f'{consumo:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((180,1015), f'R$: {custoPorDiaPrevisto:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((1050,1015), f'{consumoPorDiaPrevisto:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((675,1200), f'R$: {CustoDiario:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))

        except Exception as e:
            print(f' Um erro aconteceu {e}')
            raise 

        caminhoParaSalvar =  os.path.join(CAMINHO_RESULTS, f"Relatorio-{metas_['data']}.png")

        if not os.path.exists(caminhoParaSalvar):
            raise FileNotFoundError(f'O arquivo {caminhoParaSalvar} não foi encontrado')


        relatorio.save(caminhoParaSalvar, 'PNG')
    
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

def gerarRelatorioMensal(consumido, mes = date.today().month):
    '''
    
    '''
    
    if not isinstance(consumido, (float)):
        raise ValueError("O consumido deve ser float")
    
    try:
        relatorio = Image.open(IMAGEM_MENSAL)
        draw = ImageDraw.Draw(relatorio)
        
        with open(META_PATH, "r") as metas:
            metas_ = json.load(metas)
        
        if not isinstance(metas_, dict):
                raise ValueError(f'O valor de meta_ deve ser um dict')


        meta = str(metas_['meta'])

        if not isinstance(meta, str):
                raise ValueError(f'O valor de meta deve ser um str')
        
        custoTotal = consumido * metas_['tarifa']

        if not isinstance(custoTotal, float):
                raise ValueError(f'O valor de custoTotal deve ser um float')
        try:
            draw.text((675,470), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((675,600), f'{consumido:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
            draw.text((675,1250), f'R$: {custoTotal:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59)) 

        except Exception as e:
            print(f' Um erro aconteceu {e}')
            raise  

        caminhoParaSalvar =  os.path.join(CAMINHO_RESULTS, f"Relatorio-{mes}.png")

        if not os.path.exists(caminhoParaSalvar):
                raise FileNotFoundError(f'O arquivo {caminhoParaSalvar} não foi encontrado')
    
        relatorio.save(caminhoParaSalvar, 'PNG')

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



    