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