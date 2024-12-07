# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:25:24 2024

@author: Hewlett-Packard
"""

import pandas as pd
import numpy as np
import sqlite3

data = {'İsim':['Ahmet','Mehmet','Ayşe','Fatma'],
        'Yas':[25,30,35,40],
        'Maas':[5000,6000,7000,8000]}

df = pd.DataFrame(data)
print(df)

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])

df_matris = pd.DataFrame(matris, columns=['A','B','C'])
print(df_matris)

#Json dosyasında DataFrame oluşturma
df_json = pd.read_json('search.json')
print(df_json)

baglanti = sqlite3.connect('../sqlite_veritabanı/ogrenci.db')
df_veri = pd.read_sql_query("select * from ogrenciler where not_ortalamasi>90", baglanti)
print(df_veri)

#seriler
print("SERİLER")
veri = [10,20,30,40,50]
seri = pd.Series(veri)
print(seri)

data = {'İsim':['Ahmet','Mehmet','Ayşe','Fatma'],
        'Yas':[25,30,35,40],
        'Maas':[5000,6000,7000,8000]}

df = pd.DataFrame(data)

#isim sütununu indeks olarak kullandık ve maas bilgileri ile pandas serisi oluşturduk
ser_df = df.set_index('İsim')['Maas']
print(ser_df)

print("INDEKS VE COLUMNS")
print("Index : ",df.index)
print("sütunlar:",df.columns)

#CSV dosyasını okuma
veri_csv = pd.read_csv('veri.csv')
df_csv = pd.DataFrame(veri_csv)
print(df_csv)

#excel dosyasını okuma
excel_df = pd.read_excel('excel_veri.xlsx')
excel_df = pd.DataFrame(excel_df)
print(excel_df)

#DataFrame'i CSV dosyasına yazma
veri_csv.to_csv('yeni_veri.csv', index=False)

#DataFramei excel dosyasına yazma
excel_df.to_excel('yeni_excel_veri.xlsx', index=False)

#temel veri gösterim metotları

veri = pd.read_csv('veri.csv')
df= pd.DataFrame(veri)

print("ilk 5 satırını göstermek\n", df.head())
print("Son 5 satırı göstermek\n",df.tail())
print("Dataframe hakkında bilgi almak")
print(df.info())

print("sayısal sütünlar için istatiksel bilgileri gösterrelim")
print(df.describe())

#temel seçme ve filtreleme metotları
print("belirli bir sütunu seçmek")
print(df['Sehir'])

print("pozisyon indeksiyle satırları ve sütunları seçmek")
print(df.iloc[0:5, 1:3])

print("etiket indeksiyle satırları ve stünları seçme")
print(df.loc[df['Sehir']=='Bursa'])

print("Koşullu bir sorgu kullanarak verileri filtreleme")
print(df.query('Plaka<10'))

#temel veri dönüştürme ve temizleme metotları
veri2 = pd.read_csv('veri2.csv')
df = pd.DataFrame(veri2)
print(df.head())

print("eksik değerleri içeren satırları kaldırır")
df_eksik = df.dropna()
print(df_eksik.head())

print("eksik değerlei belili değerle doldurma")
df_doldur = df.fillna(0)
print(df_doldur.head())

#bir fonsiyonu dataframe ve sütuna uygular
df['Plaka'] = df['Plaka'].apply(lambda x:x*2)
print(df.head())
"""
df['Sehir'].fillna('Bilinmiyor', inplace=True)
df['Sehir']=df['Sehir'].map(str.lower)
print(df.head())
"""

#temel veri birliştirme ve gruplama metotları

veri = pd.read_csv('veri.csv')
veri2 = pd.read_csv('veri2.csv')
df1 = pd.DataFrame(veri)
df2 = pd.DataFrame(veri2)

df_concat = pd.concat([df1,df2])
print(df_concat)

#sql tarzı birleştirme
df_merge = pd.merge(df1,df, on='Sehir')
print(df_merge)

#index tabanlı birleştirme
df_index = df1.join(df2,lsuffix='_left',rsuffix='_right')
print(df_index)

