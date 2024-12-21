# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:57:17 2024

@author: Hewlett-Packard
"""

from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X,y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)

ridge_model = Ridge()#düzenleme katsayısını belirler

ridge_model.fit(X_train, y_train)

y_pred= ridge_model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error:",mse)