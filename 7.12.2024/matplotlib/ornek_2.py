# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:31:32 2024

@author: Hewlett-Packard
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,7,10,20]

plt.plot(x,y) #grafiği çizme işlemi

#grafiği kişiselleştirme

plt.title('Grafik başlığı', fontsize =16, color='blue')
plt.xlabel('X ekseni', fontsize=12, color='green')
plt.ylabel('y ekseni', fontsize=12, color='red')
plt.xticks(fontsize=10, rotation=45, color='purple')
plt.yticks(fontsize=10,color='orange')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
plt.legend(['veri'], loc= 'upper left')

plt.show()#grafiği gösterme
