# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:28:20 2024

@author: Hewlett-Packard
"""

"""

yapay zeka,derin öğrenme, makine öğrenmesi

makine öğremnesi
1-denetimli öğrenme
2-denetimsiz öğrenme
3-yarı denetimli öğrenme

temel kavramlar
veri
model
özellikler
etiketler
eğitim veriğ
terst verisi
doğruluk ---accuracy
aşırı öğrenme modelin eğitim verisine çok iyi uyması ancak yeni gelen 
görülmemiş verilere kötü bir şekilde uyması
yetersiz öğrenme 
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#örnek veri oluşturma
X = np.array([1,2,3,4,5]).reshape(-1,1) #bağımsız değişken
y = np.array([2,4,6,8,10]) #bağımlı değişken

#doğrusal regrasyon modelini oluşturma ve eğitme
model = LinearRegression()
model.fit(X,y)

slope = model.coef_[0]
intercept = model.intercept_

#model tarafında tahmin edilen değerleri alalım
y_pred = model.predict(X)

#veri ve regresyon doğrusunu görselleştirme
plt.scatter(X,y, color='blue',label ='Veri')
plt.plot(X,y_pred, color='red', label='Regrasyon doğrusu')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Doğrusal regrasyon')
plt.legend()
plt.show()






















