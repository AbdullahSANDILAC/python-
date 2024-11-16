# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:22:03 2024

@author: Hewlett-Packard
"""

s=4
from random import randint
dogrutahmin=False
rast_aralık=randint(1,10)
while(dogrutahmin==False):
    sayi=int(input("sayi giriniz:  (Yeniden başlamak için 0 'a basınız.Toplamda 4 deneme hakkınız bulunmaktadır.)"))
    
    if sayi==0  :
        s=4
        rast_aralık=randint(1,10)
        print("çıktınız","deneme hakkınız sıfırlandı,tekrar başlayabilirsiniz")  
    elif sayi<rast_aralık and sayi>0 and s>0:
        s-=1
        print("büyük sayı giriniz",s,"deneme hakkınız kaldı")
    elif sayi>rast_aralık and sayi>0 and s>0:
        s-=1
        print("küçük sayı giriniz",s,"deneme hakkınız kaldı")
    elif  s<=0 : 
        print("Hakkınız bitti,4 deneme hakkınızı kullandınız, tekrar başlayabilirsiniz")
        
    else:
        dogrutahmin=True
        print("doğru bildinizsayı:{}  {} .denemede sayıyı buldunuz".format(rast_aralık,5-s))