# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:30:34 2024

@author: Hewlett-Packard
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,3,4,5,6])

model=LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)

plt.scatter(X, y, color='blue')
plt.plot(X,y_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Basit linear regresyon')
plt.show()
