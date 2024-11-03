# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:18:55 2024

@author: Hewlett-Packard
"""

from my_library import toplama,carpma,cikarma, bolme, islem


print(islem())

secim = input("Yapmak isteğiniz işlemi seçin(1-2-3-4):")
sayi1 = float(input("Birinci sayıyı giriniz:"))
sayi2 = float(input("İkinci sayıyı giriniz:"))

if secim=='1':
    print("Sonuc=",toplama(sayi1, sayi2))
elif secim=='2':
    print("Sonuc=",cikarma(sayi1, sayi2))
elif secim=='3':
    print("sonuc=",carpma(sayi1, sayi2))
elif secim=='4':
    print("sonuc=",bolme(sayi1, sayi2))
else:
    print("Geçersiz giriş.lütfen dikkat ediniz.")
