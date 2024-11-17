# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:00:15 2024

@author: Hewlett-Packard
"""

def fonksiyon_adi(parametre1,parametre2,...):
    fonsiyonun gövdesi(code block)
    yapılacak işlemler buraya yazılır.
    return sonuc fonksiyon bir değer döndürebilir

def toplama(a,b):
    sonuc = a+b
    return sonuc

#fonksiyon çağırma
fonk_sonuc = toplama(3, 5)
print("toplama sonucu:",fonk_sonuc)

sayi1 = int(input("1.sayıyı giriniz:"))
sayi2 = int(input("2.sayıyı giriniz:"))
print("Toplam sonucu:",toplama(sayi1, sayi2))

def merhaba():
    print("HOŞGELDİNİZ")

merhaba()

def CARPMA(a,b):
    sonuc = a *b
    return sonuc

sayi1 = int(input("1.sayıyı giriniz:"))
sayi2 = int(input("2.sayıyı giriniz:"))
print("CARPIM sonucu:",CARPMA(sayi1, sayi2))




def selamla(isim="Misafir"):
    print("Merhaba",isim)
    
selamla("Ahmet")
selamla()


def CARPMA(a,b=1):
    sonuc = a *b
    return sonuc

fonk_sonuc = CARPMA(5)
print("CARPIM sonucu:",fonk_sonuc)

#liste ile çalışan fonksiyon

def ortlama_hesapla(notlar):
    toplam = sum(notlar)
    ortalama = toplam / len(notlar)
    return ortalama
    

not_listesi = [80,90,75,95,87]
ortalama = ortlama_hesapla(not_listesi)
print("Not ortalaması:", ortalama)







def liste_analizi(liste):
    en_buyuk = max(liste)
    en_kucuk = min(liste)
    toplam = sum(liste)
    ortalama = toplam / len(liste)
    return en_buyuk, en_kucuk, toplam, ortalama

notlar = [85,90,78,92,88]

buyuk, kucuk, toplam, ort = liste_analizi(notlar)

print(f"en büyük not:{buyuk}")

 
 
def tuple_fonksiyonu(*args):
    for a in args:
        print(a)
        
tuple_fonksiyonu(1,"iki",3.0,[4,5])
 


def eleman_analiz_et(*args):
    """
    verilen elemanları analiz eden fonsiyon
    destelenen veri türleri: int, float, str,list, dict
"""
    print("Analiz sonuçları")
    
    for arg in args:
        if isinstance(arg,int):
            print(f"Tamsayı:{arg}")
        elif isinstance(arg, float):
            print(f"ondalıklı sayı:{arg}")
        elif isinstance(arg, str):
            print(f"Metin:{arg}")
        elif isinstance(arg, list):
            print(f"liste:{arg}")
        elif isinstance(arg,dict):
            print(f"sözlük:{arg}")
        else:
            print(f"Bilinmeyen veri tütü:{arg}")

#fonsiyonu karmaşık argümanlarla çağıralım
eleman_analiz_et(10,"Merhaba",3.14,[1,2,3],{"anahtar":"deger"},78)
  
 
 
veri = 3.14
if isinstance(veri,(int,float)):
    print("but bir tan sayı veya ondalıklı sayıdır")
else:
    print("bu tam sayı veya ondalıklı sayı değildir.")

#sözlük ile çalışan fonsiyon

def dict_fonksiyon(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

dict_fonksiyon(ad="Gizem", soyad="Arslan", yas=30)
 
 
 
def sozluk_analizi(sozluk):
    if not sozluk:
        print("sozluk boş")
        return 
    print("Analiz sonucları:")
    for anahtar, deger in sozluk.items():
        print(f"{anahtar}:", end="")
        if isinstance(deger,int):
            print(f"Tamsayı:{deger}")
        elif isinstance(deger,float):
            print(f"ondalıklı sayı:{deger}")
        elif isinstance(deger, str):
            print(f"Metin:{deger}")
        elif isinstance(deger, list):
            print(f"liste:{deger}")
        elif isinstance(deger, dict):
            print(f"sözlük:{deger}")
        else:
            print(f"bilinmeyen veri türü:{deger}")

ornek_sozluk={
    "sayi":42,
    "pi":3.14,
    "mesaj":"Merhaba Python",
    "notlar":[1,2,3],
    "menü":{"tatlı":"künefe"}}

sozluk_analizi(ornek_sozluk)
        
 
#Fonksiyon içinde başka bir fonksiyon çağırma

def toplama(a,b):
    return a+b
 
def carpma_ve_toplama(x,y,z):
    sonuc_carpma = x*y
    sonuc_toplama = toplama(sonuc_carpma, z)
    return sonuc_toplama

sonuc = carpma_ve_toplama(3, 4, 5)
print("sonuc:",sonuc)





#Recursive(özyinelemeli) Fonksiyon

def faktoriyel(n):
    if n==0 or n==1:
        return 1 
    else:
        return n*faktoriyel(n-1)  #n!= n*(n-1)
    

sonuc = faktoriyel(5)
print("Faktoriyel sonucu:",sonuc)
 
 
 
 
 
 
 
 
 
 
 
 















