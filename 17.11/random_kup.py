# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:36:59 2024

@author: Hewlett-Packard
"""

import random

rastgele_sayi = random.random()
print("Rastgele Ondalık Sayı:",rastgele_sayi)

tam_sayı = random.randint(1,10)
print("Rastgele Tan Sayı:",tam_sayı)

rast_aralık = random.randrange(1,10)
print("Rastgele aralıkta tam sayı:",rast_aralık)

#listeden rastgele sayı seçme

liste=[10,20,30,40,50,60]
random_eleman = random.choice(liste)
print("Rastgele Eleman:",random_eleman)

#Zlisteyi kariştırma

random.shuffle(liste)
print("Karışık Liste:",liste)

# normal dağılımlı rastgele sayı üretme
random_normal = random.gauss(0, 1)
print("Normal Dağılımlı Rastgele Sayı:", random_normal)







