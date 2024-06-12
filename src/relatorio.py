from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json


class Relatorio:
    def __init__(self):
        self.fonte = os.path.join("fonte", "RocaTwoRegular.ttf")
        self.imagem = os.path.join("imagem", "relatorio.jpg")
        
    def criarRelatorioDiario(self):
        with open(os.path.join("dados", "meta.json"), "r") as metas:
            metas_ = json.load(metas)
        
        with open(os.path.join("dados", "consumo.json"), "r") as consumo:
            consumo_ = json.load(consumo)

        
        relatorio = Image.open(os.path.join("templates", "relatorio.png"))
        draw = ImageDraw.Draw(relatorio)
        
            
        draw.text((675,558), metas_['data'], font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 25), fill=(0,0,0))
        
        custo_por_dia_previsto = (metas_['meta'] /30) * metas_['tarifa']
        draw.text((1100,870), f'R$: {custo_por_dia_previsto:.2f}', font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 30), fill=(0,0,0))
        
        consumo_por_dia_previsto = (metas_['meta'] /30)
        draw.text((1140,1000), f'{consumo_por_dia_previsto:.2f}', font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 30), fill=(0,0,0))
        
        draw.text((1140,1100), str(consumo_['consumo']), font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 30), fill=(0,0,0))
        draw.text((650,1520), str(consumo_['consumo']), font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 30), fill=(0,0,0))
        draw.text((650,1410), str(consumo_['consumo']), font=ImageFont.truetype(os.path.join("fontes", "Poppins-Regular.ttf"), 30), fill=(0,0,0))

        

        relatorio.save(f"Relatorio-{metas_['data']}.png", 'PNG')
        
teste=Relatorio()
teste.criarRelatorioDiario()