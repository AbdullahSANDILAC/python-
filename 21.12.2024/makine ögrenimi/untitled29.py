# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:38:52 2024

@author: ARIBİLGİ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df_2 = pd.read_csv(r"sat_ev_2.csv")
df_2.drop("Unnamed: 0", axis = 1, inplace = True)

df = df_2.copy()
df = df([["Fiyat","Oda","Alan","Yas","Kat"]])
X = df.drop(["Fiyat"], axis = 1)
y = df["Fiyat"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25, random_state = 42)
model = LinearRegression()
model.fit(X,y)
y_pred = model.predict(X)

acc = mean_squared_error(y_test,y_pred)
print("Ortalama Kare Hata-MSE", acc)