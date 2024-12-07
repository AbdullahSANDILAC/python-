# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:00:00 2024

@author: Hewlett-Packard
"""
"""
veri ön işleme(data preprocessing)
veri temizleme
#dropna(),fillna()
veri dönüştürme
özllik serçimi
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

veri = {
        'boy':[170,165,180,175,160,150],
        'kilo':[70,65,80,75,62,50],
        'yas':[30,25,35,32,28,25],
        'gelir':[5000,6000,7000,5500,6500,5500],
        'cinsiyet':['erkek','kadın','erkek','erkek','kadın','kadın']}


df = pd.DataFrame(veri)
#özellik seçimi, hedef değişken ayırma
X = df.drop('cinsiyet', axis=1)
y = df['cinsiyet']

X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.2,random_state=42)

scaler =StandardScaler()

X_train_scaler = scaler.fit_transform(X_train)
X_test_scaler = scaler.fit_transform(X_test)

print("Eğitim seti:\n",X_train_scaler)
print("test seti:\n",X_test_scaler)






