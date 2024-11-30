# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:34:15 2024

@author: Hewlett-Packard
"""

import sqlite3 

baglanti = sqlite3.connect('ogrenci.db')
cursor = baglanti.cursor()

cursor.execute("DELETE FROM ogrenciler WHERE isim='Seda' and id = 3")

baglanti.commit()
baglanti.close()