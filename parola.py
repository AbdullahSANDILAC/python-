# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:41:30 2024

@author: Hewlett-Packard
"""

#Kullanıcıdan 2 kez parayı girmesini isteyerek, iki defa aynı parola 
#girildiğinde giriş yapan farklı girildiğinde uyaran python kodu

s = 0
y = 0
parola = 12345

for sayi in range(1,3):
    cevap = int(input("Parolanızı giriniz"))
    if cevap == parola:
        s+=1
    else:
        y+=1
if s==2:
    print(s," kere doğru nparola girdiniz, giriş yapıldı")
else:
    print(y,"kere parolanızı yanlış girdiniz")