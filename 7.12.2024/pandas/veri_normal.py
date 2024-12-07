# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:36:16 2024

@author: Hewlett-Packard
"""

#VERİ NORMALLEŞTİRME
#MAX-MİN NORMALLEŞTİRME
#Z-SCORE-STANDART SCALER

import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

veri = {
        'boy':[170,165,180,175,160],
        'kilo':[70,65,80,75,62],
        'yas':[30,25,35,32,28]}

df = pd.DataFrame(veri)
print(df)

df_normal_minmax = MinMaxScaler().fit_transform(df)
print(df_normal_minmax)

df_normal_minmax = pd.DataFrame(df_normal_minmax, columns=df.columns)
print("Normalleştirilmiş veri(max-Min):")
print(df_normal_minmax)

print("*"*30)

df_normal_standart = StandardScaler().fit_transform(df)
print(df_normal_standart)

df_normal_standart = pd.DataFrame(df_normal_standart, columns=df.columns)

print("Normalleştirişmiş veri(standart scaler)")
print(df_normal_standart)

