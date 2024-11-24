# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:33:44 2024

@author: Hewlett-Packard
"""
"""
class Araba:
    def __init__(self,marka):
        self.__marka = marka
        
    def get_marka(self):
        return self.__marka
    
    def set_marka(self, yeni_marka):
        self.__marka = yeni_marka

araba =Araba("Toyota")

#get metodu ile özelliğin değerini alabiliriz
print(araba.get_marka()) #çıktı:Toyota


#set metodu ile özelliğin değerini değiştirebiliriz
araba.set_marka("Honda")
print(araba.get_marka()) #çıktı:Honda
"""


class Araba:
    def __init__(self,marka,model,yil):
        self.__marka = marka #__marka özelliği kapsüllendi
        self.__model = model
        self.__yil = yil
        
    def get_marka(self):
        return self.__marka
    def set_marka(self,yeni_marka):
        self.__marka = yeni_marka
    
    def get_model(self):
        return self.__model
    def set_model(self,yeni_model):
        self.__model = yeni_model
        
        
    def get_yil(self):
        return self.__yil
    def set_yil(self,yeni_yil):
        self.__yil = yeni_yil
    
    def bilgileri_goster(self):
        print(f"Araba:{self.__marka},{self.__model},({self.__yil})")

#araba nesnesini oluşturalım
araba1 = Araba("Toyota", "Corolla", "2020")

araba1.set_marka("Mersedes")

araba1.set_model("model1")

araba1.bilgileri_goster()

















