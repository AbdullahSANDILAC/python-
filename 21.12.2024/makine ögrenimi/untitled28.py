# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:11:13 2024

@author: ARIBİLGİ
"""

import pandas as pd

df = pd.read_csv("istanbul_satilik_evler_2023.csv")

print(df.head())
print(df.Oda.unique())

df.loc[df.Fiyat == "Belirtilmemiş","Fiyat"] = "0"
df.loc[df.Yas == "0(Yeni)","Yas"] == "0"
df.to_csv("sat_ev.csv")

df = pd.read_csv("sat_ev.csv")
df.drop("Unnamed: 0", axis = 1, inplace = True)

df_2 = df.copy()
df_3 = df.copy()

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

df_3["Fiyat"] = le.fit_transform(df_2.Fiyat)
df_3["Oda"] = le.fit_transform(df_2.Oda)
df_3["Alan"] = le.fit_transform(df_2.Alan)
df_3["Yas"] = le.fit_transform(df_2.Yas)
df_3["Kat"] = le.fit_transform(df_2.Kat)

df_3.to_csv("sat_ev_2.csv")