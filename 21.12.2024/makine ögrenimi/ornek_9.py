# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:09:20 2024

@author: Hewlett-Packard
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("Doğruluk:",acc)

model_2 = RandomForestClassifier(random_state=42) 
model_2.fit(X_train,y_train)
y_pred_2=model_2.predict(X_test)

acc_2=accuracy_score(y_test, y_pred_2)
print("Random forest - Doğruluk:", acc_2)







