# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:28:43 2024

@author: Hewlett-Packard
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#ornek veri seti oluşturma
X, y = make_classification(n_samples=2000, n_features=5, n_classes=2, random_state=42)

#veriyi eğitim ve test setşlerine bolelim
X_train, X_test,y_train,y_test= train_test_split(X,y, test_size=0.2,random_state=42)


#KNN modeline olurturma ve eğitme
model =KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train)

#modeli kullanarak tahmin etme
y_pred = model.predict(X_test)
#Doğruluk değerleirni hesaplama
acc = accuracy_score(y_test, y_pred)
print("KNN- Doğruluk:",acc)

#LOgistic regredyon modelinin oluşturma ve eğitme
model_logistic=LogisticRegression()
model_logistic.fit(X_train, y_train)
#logistic regresyon modelinin kullanarak tahmin yapma
y_pred_logistic = model_logistic.predict(X_test)
#logistic regresyon doğruluk hesaplama
acc_logistic = accuracy_score(y_test,y_pred_logistic)
print("Logistic Regresyon-Doğruluk:",acc_logistic)


