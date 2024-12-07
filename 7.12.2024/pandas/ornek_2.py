# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:02:39 2024

@author: Hewlett-Packard
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split

data =pd.read_csv('meslek.csv', encoding='ISO-8859-1')

df = pd.DataFrame(data)
print(df)

X = df.drop('meslek', axis=1)
y = df['meslek']

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2, random_state=42)

scaler_1 =StandardScaler()
scaler_2 =MinMaxScaler()

X_train_scaler1 = scaler_1.fit_transform(X_train)
X_train_scaler2 = scaler_2.fit_transform(X_train)

X_test_scaler1 = scaler_1.fit_transform(X_test)

print("Eğitim seti:\n",X_train_scaler1)
print("test seti: \n",X_test_scaler1)














