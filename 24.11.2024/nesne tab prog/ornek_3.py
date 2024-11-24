# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:22:20 2024

@author: Hewlett-Packard
"""

class Ogrenci:
    def __init__(self,ad,soyad,numarasi):
        self.ad = ad
        self.soyad = soyad
        self.numarasi = numarasi
    def ogrenci_bilgileri(self):
        print(f"Öğrenci ad: {self.ad} ögrenci soyad:{self.soyad},ogrenci numarası:{self.numarasi}")


ogrenci1 = Ogrenci("YUSUF", "YILMAZ", "247")
ogrenci2 = Ogrenci("gizem", "arslan", 254)

ogrenci1.ogrenci_bilgileri()
ogrenci2.ogrenci_bilgileri()