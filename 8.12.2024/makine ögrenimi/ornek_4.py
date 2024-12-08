# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:47:04 2024

@author: Hewlett-Packard
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1,2],
              [2,3],
              [3,4],
              [4,5],
              [5,6]]) #X1 VE X2 ÖZELLİK
y = np.array([8,3,4,9,5])

model = LinearRegression()
model.fit(X,y)
y_pred = model.predict(X)

plt.scatter(X[:,0],y,color='blue')
plt.plot(X[:,0],y_pred, color='red')
plt.xlabel('X1')
plt.ylabel('y')
plt.title('Coklu linear regresyon')
plt.show()
