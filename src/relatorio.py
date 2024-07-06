from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json





METAPATH = os.path.join('dados', 'meta.json')
CONSUMOPATH = os.path.join('dados', 'consumo.json')

FONTE = os.path.join('fontes', 'RubikOne-Regular.ttf')
IMAGEM = os.path.join('templates', 'relatorio.png')
# IMAGEMMENSAL = os.path.join("templates", "relatorio_mensal.png")




def criarRelatorioDiario():
    relatorio = Image.open(IMAGEM)
    draw = ImageDraw.Draw(relatorio)

    with open(METAPATH, "r") as metas:
        metas_ = json.load(metas)
        
    with open(CONSUMOPATH, "r") as consumos:
        consumo_ = json.load(consumos)
        
    custo_por_dia_previsto = (metas_['meta'] /30) * metas_['tarifa']
    consumo_por_dia_previsto = (metas_['meta'] /30)
    meta = str(metas_['meta'])
    consumido = str(consumo_['consumo'])
    
    draw.text((675,470), metas_['data'], font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,600), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    draw.text((675,730), f'{meta} KW', font=ImageFont.truetype(FONTE, 40), fill=(255, 74, 59))
    

    
    # draw.text((1100,870), f'R$: {custo_por_dia_previsto:.2f}', font=ImageFont.truetype(FONTE, 30), fill=(0,0,0))
    # draw.text((1140,1000), f'{consumo_por_dia_previsto:.2f}', font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
        
        


    relatorio.save(f"Relatorio-{metas_['data']}.png", 'PNG')
        


def criarRelatorioMensal(consumo : float = 0, mes: str = 'teste'):
    print(1)
#     relatorio = Image.open(IMAGEMMENSAL)
#     draw = ImageDraw.Draw(relatorio)
    
    
#     with open(METAPATH, "r") as metas:
#         metas_ = json.load(metas)
        
#     with open(CONSUMOPATH, "r") as consumos:
#         cosnumo_ = json.load(consumos)
        
        
#     draw.text((675,558), metas_['data'], font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
    
#     relatorio.save(f"Relatorio-{mes}.png", 'PNG')
    
# criarRelatorioDiario()