# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:46:13 2024

@author: Hewlett-Packard
"""

from sklearn.linear_model import Lasso, Ridge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X,y = make_regression( n_samples=100, n_features=3, noise=0.1, random_state=42)
X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42)

lasso_model = Lasso(alpha=0.1) #regülarizasyon parametresi
lasso_model.fit(X_train,y_train)

ridge_model = Ridge()
ridge_model.fit(X_train, y_train)

test_hata = mean_squared_error(y_test,ridge_model.predict(X_test))
print("ridge model test hatası:",test_hata)

#Eğitim ve test hatalarını hesaplama
train_error = mean_squared_error(y_train, lasso_model.predict(X_train))
test_error = mean_squared_error(y_test, lasso_model.predict(X_test))

print("Eğitim hatası:",train_error)
print("test hatası:",test_error)

"""
eğitim hatası:modelin eğitim seti üzerindeki performasını ölçer. 
modelin verilerine ne kadar iyi uyum sağladığını gösterir
test hatası : modelin test verileri üzerindeki performansını ölçer,
modelin eğitim verileri dışındaki yeni verilere ne kadar iyi uyum sağladığını gösteriri

eğitim hatası ie test hatası arasındaki fark büyük olduğunda, model aşırı öğrenme sorunu yaşıypr demektir
eğitim ve test hata değerleri birbirine yakın ise , model iyi bir genelleme yeteğinine sahiptir yani yeni 
verilere uygulanabilirbu durumda bu model güvenilirdir ve daha güvenilir 
tahminler yapabilir deriz
"""