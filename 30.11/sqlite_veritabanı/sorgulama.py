# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:33:46 2024

@author: Hewlett-Packard
"""

import sqlite3

baglanti = sqlite3.connect('veritabani.db')

cursor = baglanti.cursor()

#VERİ SORGULAMA
cursor.execute("SELECT * FROM kullanıcılar")

#Sorgulanan verileri alıp veri değişkenine atadık.
veri = cursor.fetchall()
for satir in veri:
    print(satir)
    
baglanti.close()