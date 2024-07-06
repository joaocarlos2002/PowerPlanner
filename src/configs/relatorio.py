from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json





METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')

FONTE = os.path.join('fontes', 'RubikOne-Regular.ttf')
IMAGEM = os.path.join('templates', 'relatorio.png')
IMAGEMMENSAL = os.path.join('templates', 'relatorio_mensal.png')


def criarRelatorioDiario():
    relatorio = Image.open(IMAGEM)
    draw = ImageDraw.Draw(relatorio)

    with open(METAPATH, "r") as metas:
        metas_ = json.load(metas)
        
    with open(CONSUMOPATH, "r") as consumos:
        consumo_ = json.load(consumos)
        
    custoPorDiaPrevisto = (metas_['meta'] /30) * metas_['tarifa']
    consumoPorDiaPrevisto = (metas_['meta'] /30)
    meta = str(metas_['meta'])
    consumido = str(consumo_['consumo'])
    CustoDiario = consumo_['consumo'] * metas_['tarifa']
    
    draw.text((675,470), metas_['data'], font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,600), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,730), f'{consumido} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    
    draw.text((180,1015), f'R$: {custoPorDiaPrevisto:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((1050,1015), f'{consumoPorDiaPrevisto:.2f} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,1200), f'R$: {CustoDiario:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))

    relatorio.save(f"Relatorio-{metas_['data']}.png", 'PNG')

def criarRelatorioMensal(consumido : float = 0, mes = 'teste' ):
    
    relatorio = Image.open(IMAGEMMENSAL)
    draw = ImageDraw.Draw(relatorio)
    
    with open(METAPATH, "r") as metas:
        metas_ = json.load(metas)

    meta = str(metas_['meta'])
    custoTotal = consumido * metas_['tarifa']
    
    draw.text((675,470), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,600), f'{consumido} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,1250), f'R$: {custoTotal:.2f}', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))    
    
    relatorio.save(f"Relatorio-{mes}.png", 'PNG')
    

