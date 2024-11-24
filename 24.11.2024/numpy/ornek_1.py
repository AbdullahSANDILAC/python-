# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:33:33 2024

@author: Hewlett-Packard
"""

import numpy as np

#Liste kullanarak vektör oluşturma
v = np.array([1,2,3,4,5])
print("liste kullanarak vektor oluşturma",v)

v = np.arange(1,10)
print("arange fonk. kullanrak vektor oluşturma",v)

v=np.linspace(0,1,10)
print("linspace fonk. kullanarak vektor oluşturma",v)

a = np.array([1,2,3])
b = np.array([7,8,9])

toplam = a+b
print("toplam",toplam)

cıkarma = a-b
print("çıkarma",cıkarma)

carpma = a*b
print("carpma",carpma)

bolme =b/a
print("bolme",bolme)



#Liste kullanarak matris oluşturma
matris = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print("matris \n",matris)

sifir_matris = np.zeros((3,4))
print("sifir matrisi \n",sifir_matris)

birler_matris = np.ones((2,3))
print("birler matrisi \n",birler_matris)


A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])

toplam = A+B
print("matris toplamı \n",toplam)

cıkarma = A-B
print("cıkarma sonucu\n",cıkarma)

carpma = np.dot(A,B) #veya A.dot(B)
print("matris carpımı\n",carpma)


transpoz = A.transpose()
print("A matrisinin transpozu\n",transpoz)
a_transpoz =A.T
print("2.yöntem\n",a_transpoz)

matris = np.array([[1,2,3],
                   [4,5,6]])
bilgi_matris = np.shape(matris)
print("matrisin boyutu(satır ve sütun sayısı):",bilgi_matris)

yeni_sekil = np.reshape(matris,(3,2))
print("matrisin yeni şekli\n",yeni_sekil)

toplam_matris =np.sum(matris)
print("matris elemanlrını toplamı:",toplam_matris)

ortalama_matris = np.mean(matris)
print("elemenalrının ortalaması:",ortalama_matris)

enb_matris_elemanı = np.max(matris)
print("en büyük eleman:",enb_matris_elemanı)

enk_matris_eleman = np.min(matris)
print("en küçük eleman:",enk_matris_eleman)

v = np.array([1,2,3,4,5])

indeks_max = np.argmax(v)
indeks_min = np.argmin(v)
print("en büyük eleman indeksi",indeks_max)
print("en küçük eleman indeksi",indeks_min)

v = np.array([9,7,5,6,4,1,8])
v_sirali = np.sort(v)
print("sırali vektor",v_sirali)

indeks_sirasi = np.argsort(v)
print(indeks_sirasi)


matris = np.array([[7,4,1],
                  [2,5,8],
                  [9,6,3]])

filtre1= matris > 5
print("filte\n",filtre1)

filtrelenmis_matris = matris[filtre1]
print("filtrelenmis matris:\n",filtrelenmis_matris)


filtre2= matris % 2 == 0
print("filte\n",filtre2)

filtrelenmis_matris = matris[filtre2]
print("filtrelenmis matris:\n",filtrelenmis_matris)

matris1 = np.array([[7,8],
                    [3,4]])
matris2 = np.array([[4,5],
                    [1,2]])
birlesmis_matris1 = np.concatenate((matris1,matris2))
print("satır bazında birleştirme:\n",birlesmis_matris1)

birlesmis_matris2 = np.concatenate((matris1,matris2), axis=1)
print("sütun bazında birleştirme:\n",birlesmis_matris2)



















