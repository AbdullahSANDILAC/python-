# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
#ornek1
meyve = input("Bir meyve adı giriniz:")

if meyve=="elma":
  print("evet, elma bir meyvedir")
elif meyve=="karpuz":
  print("evet karpuz bir meyvedir")
elif meyve=="armut":
  print("evet armut bir meyvedir")
else:
  print(meyve,"gerçekten bir meyve midir?")

#☺rnek2

sayi=int(input("sayı giriniz:"))

if (sayi % 2 ==0):
    print("girilen sayı çifttir")
else:
    print("girilen sayı tektir.")


#♥ornek3

sayi=int(input("sayı giriniz:"))

if (sayi>0):
    if(sayi % 2 ==0):
        print("girilen sayı pozitif çift sayıdır")
    else:
        print("girilen sayı pozitif ancak tek sayıdır")
else:  
    if(sayi%2==0):
        print("girilen sayı negatif çift sayıdır.")
    else:
        print("girilen sayı negatif tek sayıdır")


#ornek4
email = 'email@gizem.com'
password = "1234567"

girilenemail = input("email:")
girilenpassword = input("şifre:")

uzunluk = len(girilenpassword)

if (uzunluk>7 and uzunluk<10):
    if(girilenemail == email):
        if(girilenpassword == password):
            print("giriş başarılı")
        else:
            print("şifrenizi kontrol ediniz")
    else:
        print("email kontrol ediniz")
else:
    print("şifreniz 7 karakterden az10 karakterden fazla olamaz")          

#ornek4 farklı yöntem
email = "fundacanbulut2@gmail.com"
parola = "1234567"

email1 = input("Emalinizi giriniz:")
parola2 = input("Parolanızı giriniz:")

parola_uzunluk = len(parola2)

if parola_uzunluk >=7 and parola_uzunluk < 10:
    if email== email1 and parola == parola2:
        print("Sisteme giriş yapıldı.")
    elif email == email1 and parola != parola2:
        print("Parolanız yanlıştır.")
    elif email != email1 and parola == parola2:
        print("Emailiniz yanlıştır.")
    elif email != email1 and parola != parola2:
        print("Parolanız ve emailiniz yanlıştır.")
    else:
        print("Sisteme giriş yapılamadı.")

else:
    print("Parola uzunluğunuzu kontrol edin.")


#ornek5

a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

if (a>b) and (a>c):
    print("a b ve c saysından büyüktür")
elif (b>a) and (b>c):
    print("b en büyük sayıdır")
elif (c>a) and (c>b):
    print("c en büyük sayıdır")
"""
#ornek6
"""
kişinin ad, kilo, boy bilgilerini alalım. 
kilo indexlerini hesaplayalım
formül = (kilo/boy uzunluğunu karesi) 2**3=8 pow(2,3)=8
0-18.4 => Zayıf
18.5-24.9 => Normal
25.0-29.9 => Fazla Kilolu
30.0-34.9 => Şişman (Obez)

"""
ad = input("adınız:")
kilo = float(input("kilonuz:"))
boy = float(input("Boyunuz:"))

index = (kilo) / (boy**2)

print(index)

if (index>=0.0) and (index<=18.4):
    print("{} kilo indeksin: {} ve değerlendirme sonucun zayıf".format(ad,index))
elif (index>18.47) and (index<=24.9):
    print(f"{ad} kilo indeksin:{index} degerlendirme sonucun normal")
elif (index>24.9 and index<=29.9):
    print(f"{ad} kilo indeksin:{index} değerlendirme sonucun kilolu")
elif (index>29.9 and index<=45.9):
    print(f"{ad} kilo indeksin:{index} değerlendirme sonucun obez")
else:
    print("bilgileriniz yanlış")

    












  