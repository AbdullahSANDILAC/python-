# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:53:03 2024

@author: Hewlett-Packard
"""

try:
    #potansiyel hata olabilcek kodlar buraya yazılır
    sayi=int(input("giriş yapınız:"))
except ValueError:
    #Eğer valuearror hatası oluşursa buraki kodlar çalışır
    print("Lütfen geçerli bir sayı giriniz")
except KeyboardInterrupt:
    print("Kullanıcı işlemi iptal etti")

 
    
try:
    #potansiyel hata olabilcek kodlar buraya yazılır
    sayi=int(input("giriş yapınız:"))
except ValueError:
    #Eğer valuearror hatası oluşursa buraki kodlar çalışır
    print("Lütfen geçerli bir sayı giriniz")
else:
    print("Başarılı bir giriş yaptınız")
    
    
    
try:
    #potansiyel hata olabilcek kodlar buraya yazılır
    sayi=int(input("giriş yapınız:"))
except ValueError:
    #Eğer valuearror hatası oluşursa buraki kodlar çalışır
    print("Lütfen geçerli bir sayı giriniz")
finally:
    #her durumda çalıştırılam kodu içerir.
    #dosya kapatma, bağlantı sonlandırma gibi





