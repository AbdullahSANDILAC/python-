# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:16:05 2024

@author: Hewlett-Packard
"""

import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

ogr = "Seda"
not1 = 75

cursor.execute("UPDATE ogrenciler SET not_ortalamasi=? WHERE isim=?",(not1,ogr))

cursor.execute("UPDATE ogrenciler SET not_ortalamasi=95 WHERE id=1")

baglanti.commit()
baglanti.close()

