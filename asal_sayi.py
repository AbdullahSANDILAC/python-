# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:18:36 2024

@author: Hewlett-Packard
"""

sayi =int(input("Sayınızı giriniz:"))

if sayi>1:
    for i in range(2,sayi):
       if sayi % i == 0:
          print(f"{sayi} sayısı asal sayı değildir.")
          break
    else:
       print(f"{sayi} asal bir sayıdır")

else:
    print(sayi,"asal sayi değildir")
    
    