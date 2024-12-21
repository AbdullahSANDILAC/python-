# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:44:45 2024

@author: ARIBİLGİ
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("banana_quality.csv", encoding = "ISO-8859-1")
print(df.head())
print(df.info())
print(df.duplicated().sum())
print(df.isnull().sum())
print(df.describe())

plt.figure(figsize = (10,4))
cols = ["c", "brown"]
plt.subplot(1,2,1)
sns.barplot(x = df["Kalite"].value_counts().index,y = df["Kalite"].value_counts(),palette = cols)
plt.ylabel("")
plt.subplot(1,2,2)
plt.pie(x = df["Kalite"].value_counts(),labels = df["Kalite"].value_counts().index,shadow = True, explode = [0.01,0.00],startangle = 30, autopct = "%0.2f%%",colors = cols)
plt.legend(labels = ["good", "bad"],loc = (1,0.8),fontsize = "small")
plt.tight_layout()
plt.show()

scaler = StandardScaler()
df.iloc[:,:-1] = scaler.fit_transform(df.iloc[:,:-1])
print("ilocc\n",df.iloc[:,:-1])

X = df.drop(["Kalite"],axis = 1)
y = df["Kalite"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3, random_state = 42)

model_list = [RandomForestClassifier(),LogisticRegression(),KNeighborsClassifier(),DecisionTreeClassifier()]
model_name_liste = []
model_acc = []

for i in model_list:
    model = i.fit(X_train,y_train)
    model_name = model.__class__.__name__
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    model_name_liste.append(accuracy)
    model_acc.append(accuracy)
    print(f"{model_name}, doğruluk : {accuracy:.3f}\n")