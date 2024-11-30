# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:13:21 2024

@author: Hewlett-Packard
"""

import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

cursor.execute("SELECT * FROM ogrenciler")

veriler = cursor.fetchall()
for satir in veriler:
    print(satir)
    
baglanti.close()