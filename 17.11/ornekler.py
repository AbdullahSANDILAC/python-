# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:37:56 2024

@author: Hewlett-Packard
"""

#ornek1

def pozitif_cift_sayilari_bul(x):
    pozitif_ciftler= []
    for i in range(2,x+1,2):
        pozitif_ciftler.append(i)
    return pozitif_ciftler

sayi = int(input("bir sayı girin"))

cift_sayilar = pozitif_cift_sayilari_bul(sayi)
print("{} 'ye kadar olan pozitif çift sayilar:{}".format(sayi, cift_sayilar))


#ornek2
#Fibonacci Dizisi (10 eleman): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibonacci(n):
    fib_dizisi = [0,1]
    while len(fib_dizisi)<n:
        fib_dizisi.append(fib_dizisi[-1]+fib_dizisi[-2])
    return fib_dizisi

n = int(input("Kaç elemanlık dizi hesaplanak?:"))

a= fibonacci(n)
print("fibonacci dizsi({} elemanlı):{}".format(n,a))



#ornek 3
#kullanıcın girdiği bir metni ters çeviren fonksiyon yazınız
def ters_cevir(metin):
    kelimeler = metin.splitlines()
    for kelime in kelimeler:
        ters_cevrilmis_metin=kelime[::-1]
    return ters_cevrilmis_metin

girilen_metin = input("Bir metin girin")

ters_metin= ters_cevir(girilen_metin)
print("Ters Çevrilmiş Metin:{}".format(ters_metin))

def ters_cevir2(metin):
    kelimeler = metin.split()
    ters_cevrilmis_metin=''.join(kelime[::-1] for kelime in kelimeler)
    return ters_cevrilmis_metin


girilen_metin = input("Bir metin girin")

ters_metin= ters_cevir2(girilen_metin)
print("Ters Çevrilmiş Metin:{}".format(ters_metin))



kare_al = lambda x:x**2

sonuc=kare_al(4)
print("karesi:",sonuc)

toplama = lambda x,y:x+y
toplam = toplama(3,8)
print("toplam:",toplam)


sayilar = [1,2,3,4,5]
kareler = list(map(lambda x:x**2, sayilar))
print(kareler)








