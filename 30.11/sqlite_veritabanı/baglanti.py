# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:30:28 2024

@author: Hewlett-Packard
"""

import sqlite3

#SqlİTE VERİTABANINA BAĞLANMA
baglanti = sqlite3.connect('veritabani.db')

#Bağlantı üzerinde bir imleç oluşturma
cursor = baglanti.cursor()
"""
cursor.execute('''CREATE TABLE kullanıcılar
               (id INTEGER PRIMARY KEY, isim TEXT, yas INTEGER)
               ''')
"""
#veri ekleme
cursor.execute("INSERT INTO kullanıcılar (isim,yas) VALUES (?,?)",('AHMET',30))
cursor.execute("INSERT INTO kullanıcılar (isim,yas) VALUES (?,?)",('MEHMET',25))

#Değişiklikleri kaydetme
baglanti.commit()