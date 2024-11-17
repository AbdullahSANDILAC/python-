# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:13:49 2024

@author: ARIBILGI
"""

#kullanıcadan isim mail kullanıcı ekle fonksiyonu gönder ve kullanıcılar .json yazıyor sonra kullancılar.json ı göstersin.

import json



def kullanici_goster():
    with open("kullanicilar.json","r",encoding="utf-8") as file:
        data=json.load(file)
        for kullanicilar in data["kullanicilar"]:
            print("kullanıcı adı",kullanicilar["isim"],",kullanıcı mail:",kullanicilar["e-posta"])
            
def kullanici_ekle(isim,mail):
    with open("kullanicilar.json","r",encoding="utf-8") as file:
        veri=json.load(file)
        yeni_id=len(veri["kullanicilar"])+1
        yeni_kullanci={"id":yeni_id,
                       "isim":isim,
                       "e-posta":mail}
        veri["kullanicilar"].append(yeni_kullanci)
        
    with open("kullanicilar.json","w",encoding="utf-8") as file:
        json.dump(veri, file)
isim=input("lütfen isim giriniz: ")
mail=input("lütfen mail giriniz: ")

kullanici_ekle(isim, mail)
kullanici_goster()  
        