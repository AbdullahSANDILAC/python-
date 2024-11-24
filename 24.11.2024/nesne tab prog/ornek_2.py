# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:11:44 2024

@author: Hewlett-Packard
"""

class Araba:
    def __init__(self, marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    def bilgileri_goster(self):
        print(f"Araba:{self.marka},{self.model},{self.yil}")
        
araba1 = Araba("Toyota", "model1", "2000")
araba2 = Araba("Honda", "model2", "2018")

araba1.bilgileri_goster()
araba2.bilgileri_goster()
    