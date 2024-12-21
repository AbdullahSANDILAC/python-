# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:05:59 2024

@author: Hewlett-Packard
"""

"""
sınıflandırma kavramıgirdi verilerini belirli bir sınıfa atama işlemidir.
denetimli öğrenme kategorisine girer örnek sınıflandırma algoritmaları
"k-en yakın komşu algortiması(k-Nearest Neighbors),
 destek vektör makineler(support vector machines)"
 bir sınıflandırma algoritması, veriye ve problemin titpine bağlı olarak değişebilir
 karmaşıklık matrisi (confusion matrix)
 sınıflandırma sonuçlarını görselleştirmek için bir çeşit grafik oluşturma
 gerçek değerler ve tahmin edilen sınıfları karşılşaştırarak bir 
 karmaşikşık matrisi oluşturaulabilir veya doğruluk değerlerinin 
 sınıflara göre dağılımını gösteren bir çubuk grafiği oluştururlabilir
 """
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


iris = load_iris()
X = iris.data #özellikler
y = iris.target #hedef sınıflar

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)

#doğruluk hesaplama
acc = accuracy_score(y_test,y_pred)
print("test seti doğruluğu:",acc)

#karmaşıklık matrisini hesaplama
cm = confusion_matrix(y_test,y_pred)

#Karmaşıklık matrisinin görselleştirme
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, cmap ='Blues', fmt='d', xticklabels=iris.target_names,yticklabels=iris.target_names)
plt.xlabel('Tahmin edilen sınıflar')
plt.ylabel('Gerçek sınıflar')
plt.title('Karmaşıklık Matrisi')
plt.show()






