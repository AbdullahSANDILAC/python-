# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:52:41 2024

@author: Hewlett-Packard
"""
"""
import json

veri = {"ad": "melisa", "yas": 30, "sehir": "istanbul"}
with open("veri.json","w") as dosya:
    json.dump(veri, dosya)

with open("veri.json","r") as dosya:
    veri = json.load(dosya)
print(veri)
"""

import json

data ={
       "isim":"gizem",
       "yas":"35",
       "sehir":"istanbul",
       "meslek":"eğitmen"}

with open("kullanicilar.json","w",encoding="utf-8") as file:
    json.dump(data,file, ensure_ascii=False)

with open("kullanicilar.json","r", encoding="utf-8") as file:
    data = json.load(file)
print(data)



