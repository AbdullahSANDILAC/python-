# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:47:06 2024

@author: Hewlett-Packard
"""

#CRUD İŞLEMLERİ
#CREATE
#READ --SELECT
#UPDATE
#DELETE

import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

cursor.execute('''CREATE TABLE ogrenciler
               (id INTEGER PRIMARY KEY, isim TEXT, not_ortalamasi INTEGER)
               ''')
               
baglanti.commit()

cursor.execute("INSERT INTO ogrenciler (isim, not_ortalamasi) VALUES ('Kaan', 75)")

baglanti.commit()

baglanti.close()
