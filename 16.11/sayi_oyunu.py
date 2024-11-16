# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:17:27 2024

@author: Hewlett-Packard
"""

from random import randint

tahmin = randint(1,100)
dogrutahmin = False
sayac = 0
while (dogrutahmin==False):
    sayac+=1
    girilensayi = int(input("1-100 arasında sayı girin(çıkmak için sıfıra basın):"))
    if (girilensayi==0):
        print("oyundan çıktınız")
        break
    elif girilensayi < tahmin:
        print("Küçük sayı giridiniz.daha yüksek giriniz:")
        continue
    elif girilensayi > tahmin:
        print("Büyük sayı giridniz.Daha küçük giriniz:")
        continue
    else:
        dogrutahmin=True
        print("Dogru tahmin ettiniz.Rastgele üretilen sayı{}".format(tahmin))
        print("Tahmin sayınız:{}".format(sayac))
        