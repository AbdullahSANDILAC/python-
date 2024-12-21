# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:29:38 2024

@author: Hewlett-Packard
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error

canser = load_breast_cancer()
X = canser.data
y = canser.target

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model=ElasticNet(alpha=0.1, l1_ratio=0.5,random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Ortalama Kare Hata(MSE):",mse)