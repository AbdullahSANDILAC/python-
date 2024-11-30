# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:59:39 2024

@author: Hewlett-Packard
"""

import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

veriler = [
    ('Fatma',85),
    ('Seda',76),
    ('Ali',55)
    ]

#her bir veriyi veritabanına eklemek için döngü

for veri in veriler:
    cursor.execute("INSERT INTO ogrenciler (isim,not_ortalamasi) VALUES (?,?)",veri)

baglanti.commit()
baglanti.close()
    
