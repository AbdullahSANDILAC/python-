# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:02:17 2024

@author: Hewlett-Packard
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1,1],[1,2],[2,2],[2,3]]) #bağımmsız değişken
y = np.dot(X, np.array([1,2])) +3 #bağımlı değişken
"""
model oluşturalım, modeli eğitelim
tahmin değerlerini alalım
gerçek değerleri ve tahmin değerleini yazdıralım
"""
model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)

print("Gerçek değerler:",y)
print("Tahmin edilen değerler:",y_pred)

accuracy = model.score(X,y)
print("Modelin Doğruluğu:",accuracy)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter (X[:,0],X[:,1],y, color='blue', label='Gerçek değerler')
ax.scatter(X[:,0],X[:,1],y_pred, color='red', label='Tahmin edilen değerler')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('y')
plt.title("Çoklu Doğrusal regresyon")
plt.legend()
plt.show()

"""
bu kod iki bağımsız değişkenin (X1 VE X2) bir bağımlı değişken y üzerindeki etkisinini
modellemek için çoklu doğrusal regresyon modelinin oluşturur ve eğtitr. 
Daha sonra modelin gerçek değerler ile tahmin edilen değerlerinin 
karşılaştırır ve doğruluğu ölçer. Son olarak veriyi 3D uzayda görselleştirir

"""











