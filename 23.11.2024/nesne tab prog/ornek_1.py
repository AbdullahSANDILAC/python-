# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:49:08 2024

@author: Hewlett-Packard
"""

class Araba:
    #__init__ metodu sınıfın kurucu metodu olup, bir araba nesnesi oluştururken çağrılır.
    #bu metot, araba nesnesinin başlanğıç durumunu tanımlar ve nesneye özellikjler atar
    def __init__(self,marka,model,yil):
        #self.marka arba sınınfına ait bir özelliktir ve araba nesnesinin marka özelliğini temsil eder
        self.marka = marka
        self.model = model
        self.yil = yil
     
    #bilgileri goster metodu, araba sınıfına ait bir yöntemdir ve araba nesnesinin bilgilerini gosterir
    def bilgileri_goster(self):
        print(f"Araba:{self.marka},{self.model},{self.yil}")
        
arac = Araba("BMW", "BMW1", "2008") 
arac.bilgileri_goster()

class Araba_Hız:
    def __init__(self,renk,marka):
        self.renk = renk
        self.marka = marka
    def hizlan(self):
        print(self.renk+"araba hızlanıyor, aracın markası"+self.marka)
    def yavasla(self):
        print(self.renk+"araba yavaşlıyor, aracın marlası"+self.marka)

#bu satırlarda araba_hiz sınıfına ait iki nesne oluşturduk bmw ve audi olarak
bmw = Araba_Hız("kırmızı", "BMW")
audi = Araba_Hız("sarı", "AUDI")

audi.hizlan()
bmw.yavasla()





