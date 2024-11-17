# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:27:35 2024

@author: Hewlett-Packard
"""

dosya = open("yeni_metin.txt","w",encoding="utf-8")
dosya.write("bu yeni metin belgesidir\n")
dosya.write("python eğitimi")
dosya.close

dosya =open("yeni_metin.txt","r", encoding="utf-8")
for i in dosya:
    print(i)
dosya.close

dosya =open("yeni_metin.txt","r", encoding="utf-8")
bilgiler = dosya.readlines()
print(bilgiler)
print(bilgiler[1])
dosya.close

with open("yeni_metin.txt","r",encoding="utf-8") as dosya:
    for i in dosya:
        print(i,end="")

with open("yeni_metin.txt","r+", encoding="utf-8") as dosya:
    dosya.seek(6) #imlec 6.indiste
    dosya.write("burası 6.indis başlangıcı ")
    print(dosya.tell()) 



