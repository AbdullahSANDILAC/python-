# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:17:28 2024

@author: Hewlett-Packard
"""
"""
print(*range(0,10,2))
print(*range(10,50,4))

print(*range(10,0,-1))

print(*range(-5,5))

print(*range(1,1)) #çıktı ()
print(*range(1,-1))
print(*range(0))

tr_harfler="şçöğüİı"
for a in tr_harfler:
    print(a)
print("--------------------------")    
sayılar="123456789"
for sayı in sayılar:
    print(sayı)


tr_harfler="şçöğüİı"
parola=input("parolanızı giriniz:")

for karakter in parola:
    if karakter in tr_harfler:
        print("parolada türkçe karakter kullanılamaz")
    else:
        print("parolanız geçerli")
        
        
       

for i in range(1,10,2):
    print(i)
    


sayilar =[10,20,30,40,50,"sayi"]

for sayi in sayilar:
    print(sayi)
        
meyveler=["elma","armut","kiraz"]

for a in meyveler:
    print(a)
    
renkler=("kırmızı","yeşil","mavi",1,2,3)

for b in renkler:
    print(b)
    
#index numaralaını yazdırmak istersek

for index,renk in enumerate(renkler):
    print(f"{index}:{renk}")
    

ogrenci=["Ahmet","Ali","Serkan","Seda","Merve","Gamze"]  

for index,isim in enumerate(ogrenci):
    print(f"{index}:{isim}")


ogrenciler={"142":"Ahmet","785":"Ali","456":"Serkan"}

for no,isim in ogrenciler.items():
    print(f"öğrenci numarası:{no}, Öğrenci Adı:{isim}")
    

for no in ogrenciler.keys():
    print(f"ogrenci numarası:{no}")
    
for isim in ogrenciler.values():
    print(f"ogrenci adı:{isim}")


 

sayilar =[1,2,3,4,5]
toplam = 0

for sayi in sayilar:
    toplam = toplam + sayi
    toplam += sayi
    
print("toplam=",toplam)



sayi=int(input("sayı giriniz:"))

if (sayi % 2 ==0):
    print("girilen sayı çifttir")
else:
    print("girilen sayı tektir.")
  
    
  
sayilar=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in sayilar:
    if (i % 2 ==0):
        print(i)

# sayılar listesindeki hangi sayılar 3'ün katıdır?

print("----------------------------")
for i in sayilar:
    if (i % 3 == 0) and (i>0):
        print(i)

print("----------------------------------")
#sayilar listesinde bulunan elemanların toplamı kaçtır?

topla = 0

for sayi in sayilar:
    topla +=sayi
print("toplam=",topla)

print("--------------------------------")

#sayilar listesindedeki tek sayıların karesini yazdırınız
#1 sayısının karesi=1
#3 sayısını  karesi=9

for sayi in sayilar:
    if (sayi % 2 == 1):
        print("{} sayının karesi= {}".format(sayi,sayi**2))

for i in range(1,101):
    if i%2==0:
        print(i)

sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))

for i in range(sayi1,sayi2):
    if i%2==1:
        print(i)

#kulanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan python for döngüsünü yazınız
#10-50-->10+11+12+13.....+50=?

sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))


toplam=0
for i in range(sayi1,sayi2+1):
    print(i)
    toplam +=i
print("{} ile {} arasındaki sayıların toplamı:{}".format(sayi1,sayi2,toplam))

#Kullanıcın girdiği sayının faktöriyeli
#Faktöriyel
#5! =5*4*3*2*1
#5! =1*2*3*4*5

carpim = 1
sayi=int(input("sayı giriniz:"))


for i in range(1,sayi+1):
    carpim *=i
print(sayi,"sayisının faöktöriyeli:",carpim)
"""
#İç İçe döngüler

sayilar =[1,2,3,4]

for sayi1 in sayilar:
    print("1.döngü çalışıyor sayi1={}".format(sayi1))
    for sayi2 in sayilar:
        print("2.döngü çalışıyor sayi2={}".format(sayi2))

#çarpım tablosu ÖÖÖDDDEEEEVVVV





























