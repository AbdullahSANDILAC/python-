# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:40:17 2024

@author: Hewlett-Packard
"""

import pandas as pd
from io import StringIO

"""
pandas kullanımı:
    veri seti oluşturmak, veri setine bakmak,
    belirli sütunları seçmek, istatiksel veri elde etmek amacıyla ku7llanılır
"""
veri = StringIO("""Mağaza,Meyve,Fiyat
                A,elma,35
                A,muz,40
                B,elma,37
                B,çilek,45
                C,muz,45
                C,çilek,60
                D,avakado,95
                D,erik,85
                """)
                
                
df = pd.read_csv(veri)

print("ilk 5 satir:\n",df.head()) 
print(df.describe())  
meyveler = df['Meyve']   
print("meyve sütunundaki benzersiz değerler",meyveler.unique())
print("meyve sütunundaki değer sayıları",meyveler.value_counts())        

ortlama_fiyat = df['Fiyat'].mean()    
print("Ortalaam meyve fiyatı",ortlama_fiyat)           
                
veri_2 = StringIO("""ID,ad,soyad,depatman,maas,yas
                  1,ahmet,erdem,yazılım,45000,35
                  2,mehmet,yılmaz,aşçı,30000,46
                  3,zehra,aydın,yazılım,,23
                  4,gamze,soylu,öğrenci,,20
                  """)            
                
"""
ortlama maas=?
departmanlara göre çalışan sayısı =?
ortlama maas üstü maas alanlar =?   
"""  
df_2 = pd.read_csv(veri_2) 
print(df_2)     

ortalama_maas = df_2['maas'].mean()
print("ortalama maas:",ortalama_maas) 

d_cal_say = df_2['depatman'].value_counts()
print("depertmalnlara göre çalışan sayısı:\n",d_cal_say)

ort_ustu_maas = df_2[df_2['maas']>ortalama_maas]
print("ortalama üstü maas alanlar:\n",ort_ustu_maas)




 
                