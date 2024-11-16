# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:17:49 2024

@author: Hewlett-Packard
"""

from my_library import toplama,cikarma,carpma,bolme,islem
print (islem())
try:
    secim=input("1-2-3-4- ten birisini seçiniz.")
    sayi1=float(input("1.sayı: "))
    sayi2=float(input("2.sayı: "))
    if secim=='1':
        print("Sonuc=",toplama(sayi1, sayi2))
    elif secim=='2':
        print("Sonuc=",cikarma(sayi1, sayi2))
    elif secim=='3':
        print("Sonuc=",carpma(sayi1, sayi2))
    elif secim=='4':
        print("Sonuc=",bolme(sayi1, sayi2))
    else:
     print("Geçersiz seçenek. Lütfen '1', '2', '3', '4' yazın.")
except ValueError:
   
     print("Geçersiz sayı. ")