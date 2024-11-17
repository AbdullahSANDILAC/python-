# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:22:16 2024

@author: Hewlett-Packard
"""

"""API --- UYGULAMA PROGRAMLAMA ARAYÜZÜ
JSON --- VERİLERİ DEPOLAMAK VE İLETMEK İÇİN OKUNABİLİR VERİ BİÇİMİ
"""

import json

#bir python sözlüğünü json biçimine dönüştürme
veri = {"ad":"melisa","yas":30, "sehir":"istanbul"}
json_veri = json.dumps(veri)

print("JSON VERİSİ OLUŞTU:",json_veri)


#JSON biçimindeki veriyi  python sözlüğüne dönüştürme
json_veri = '{"ad": "melisa", "yas": 30, "sehir": "istanbul"}'
python_soz = json.loads(json_veri)

print("PYTHON VERİSİ OLUŞTU",python_soz)