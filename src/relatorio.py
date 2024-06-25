from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json



FONTE = os.path.join("fontes", "Poppins-Regular.ttf")
IMAGEM = os.path.join("templates", "relatorio.png")
        
def criarRelatorioDiario(consumo: dict):
    relatorio = Image.open(IMAGEM)
    draw = ImageDraw.Draw(relatorio)

    with open(os.path.join("dados", "meta.json"), "r") as metas:
        metas_ = json.load(metas)

        custo_por_dia_previsto = (metas_['meta'] /30) * metas_['tarifa']
        consumo_por_dia_previsto = (metas_['meta'] /30)
    
        draw.text((675,558), metas_['data'], font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
        draw.text((1100,870), f'R$: {custo_por_dia_previsto:.2f}', font=ImageFont.truetype(FONTE, 30), fill=(0,0,0))
        draw.text((1140,1000), f'{consumo_por_dia_previsto:.2f}', font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
        draw.text((1140,1100), str(consumo['consumo']), font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
        draw.text((650,1520), str(consumo['consumo']), font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))
        draw.text((650,1410), str(consumo['consumo']), font=ImageFont.truetype(FONTE, 25), fill=(0,0,0))

        

        relatorio.save(f"Relatorio-{metas_['data']}.png", 'PNG')
        
