# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:31:09 2024

@author: Hewlett-Packard
"""


import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

ogr = "Seda"
not1 = 75

cursor.execute("UPDATE ogrenciler SET not_ortalamasi=? WHERE isim=?",(not1,ogr))
if cursor.rowcount >0:
    print("kayır güncelleme başarılı")
else:
    print(f"hatalı işlem kullanıcı bulunamadı: {ogr}")



baglanti.commit()
baglanti.close()