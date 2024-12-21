# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:10:14 2024

@author: Hewlett-Packard
"""

import pandas as pd
"""
df =pd.read_csv("istanbul_satilik_evler_2023.csv")

print(df.head())
print(df.Oda.unique())
df.loc[df.Fiyat == "Belirtilmemiş","Fiyat"] ="0"
df.loc[df.Yas == "0(Yeni)","Yas"] ="0"
df.to_csv("sat_ev.csv")
"""

#bu kısımda kategorik ifadeleri etiketleme işlemi yapalım

df = pd.read_csv("sat_ev.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)

df_2 = df.copy()
df_3 = df.copy()

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

df_3["Fiyat"] = le.fit_transform(df_2.Fiyat)
df_3["Oda"] = le.fit_transform(df_2.Oda)
df_3["Alan"] = le.fit_transform(df_2.Alan)
df_3["Yas"] = le.fit_transform(df_2.Yas)

df_3.loc[df_3.Kat == "0", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "1", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "2", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "3", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "4", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "5", "Kat"] = "1-10"
df_3.loc[df_3.Kat == "6", "Kat"] = "1-10"

df_3["Kat"] = le.fit_transform(df_2.Kat)

df_3.to_csv("at_ev_2.csv")













