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

    relatorio = Image.open(IMAGEM)
    draw = ImageDraw.Draw(relatorio)

    with open(META_PATH, "r") as metas:
        metas_ = json.load(metas)

    custoPorDiaPrevisto = (metas_['meta'] /30) * metas_['tarifa']
    consumoPorDiaPrevisto = (metas_['meta'] /30)
    meta = str(metas_['meta'])
    CustoDiario = consumo * metas_['tarifa']

    draw.text((675,470), metas_['data'], font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,600), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,730), f'{consumo:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    
    draw.text((180,1015), f'R$: {custoPorDiaPrevisto:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((1050,1015), f'{consumoPorDiaPrevisto:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,1200), f'R$: {CustoDiario:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))

    caminhoParaSalvar =  os.path.join(CAMINHO_RESULTS, f"Relatorio-{metas_['data']}.png")
    relatorio.save(caminhoParaSalvar, 'PNG')

def gerarRelatorioMensal(consumido, mes = date.today().month):
    relatorio = Image.open(IMAGEM_MENSAL)
    draw = ImageDraw.Draw(relatorio)
    
    with open(META_PATH, "r") as metas:
        metas_ = json.load(metas)

    meta = str(metas_['meta'])
    custoTotal = consumido * metas_['tarifa']
    
    draw.text((675,470), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,600), f'{consumido:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,1250), f'R$: {custoTotal:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))    

    caminhoParaSalvar =  os.path.join(CAMINHO_RESULTS, f"Relatorio-{mes}.png")
    relatorio.save(caminhoParaSalvar, 'PNG')





    