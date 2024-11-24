# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:57:33 2024

@author: Hewlett-Packard
"""
"""
class Arac:
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    def bilgileri_goster(self):
        print(f"Aracın:{self.marka},{self.model},{self.yil}")


#miras alan sınıf
class Araba(Arac):
    def __init__(self,marka,model,yil,yakit_turu):
        super().__init__(marka,model,yil)
        self.yakit_turu = yakit_turu
    def bilgileri_goster(self):
        print(f"Araba:{self.marka},{self.model},{self.yil}, yakit turu:{self.yakit_turu}")
        
araba1 = Araba("Toyota","Model1",2020,"Benzin")
araba1.bilgileri_goster()
        
araba2 = Arac("honda", "model1", 2014) 
araba2.bilgileri_goster()     
"""


class Anasinif:
    def __init__(self):
        print("Ana sınıfın __init__ metodu çalıştı")
    
class Altsinif(Anasinif):
    def __init__(self):
        super().__init__()
        print("Alt sınıfın __init metodu çalıştı")


#Altsinif sınıfının başlatıcı metodu hem kendi işlemlerini hemde 
#üst sınıfın bailatıcı metodunu çağırarak üst sınıfın başlangıç 
#işlemlerini gerçekleştirir


Altsinif()


