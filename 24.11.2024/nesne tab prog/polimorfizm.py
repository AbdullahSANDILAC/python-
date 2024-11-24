# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:44:43 2024

@author: Hewlett-Packard
"""

class Sekil:
    def alan_hesapla(self):
        pass 

class Dikdortgen(Sekil):
    def __init__(self, uzunluk,genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    def alan_hesapla(self):
        return self.uzunluk * self.genislik

class Kare(Sekil):
    def __init__(self,kenar):
        self.kenar = kenar
    def alan_hesapla(self):
        return self.kenar **2

def alan_hesapla_ve_yazdir(sekil):
    print(f"{type(sekil).__name__} alanı:{sekil.alan_hesapla()}")
    

sayi1 =int(input("bir sayı giriniz:"))

dikdortgen = Dikdortgen(sayi1, 3)
kare = Kare(4)

alan_hesapla_ve_yazdir(dikdortgen)
alan_hesapla_ve_yazdir(kare)
    
    
    
    
    
    
    