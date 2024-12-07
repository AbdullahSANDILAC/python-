# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:20:42 2024

@author: Hewlett-Packard
"""

import pandas as pd

veri = pd.read_csv('veri.csv')
df = pd.DataFrame(veri)

print(df)

print(df[df['Plaka']>40])
print(df['Plaka']>40) #bool değeri döndürür

print(df[(df['Plaka']<10) & (df['Yil']==2022)])

print(df[df['Sehir'].isin(['İstanbul','Bursa','Amasya'])])
print(df[~df['Sehir'].isin(['İstanbul','Bursa','Amasya'])])

print(df[df['Sehir'].isnull()])
print(df[df['Sehir'].notnull()])

stack_df =df.stack()
print(stack_df)



