# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:32:46 2024

@author: Hewlett-Packard
"""

from datetime import datetime

tarih=datetime.today()
cevap=input("Bir seçenek yazınız:  (tarih/yıl/ay/gün/saat/dakika/saniye/salise:  ")
yıl=tarih.year
ay=tarih.month
gün=tarih.day
saat=tarih.hour
dakika=tarih.minute
saniye=tarih.second
salise=tarih.microsecond

if cevap =="tarih":
    print("tarih:",tarih)
elif cevap =="yıl":
    print("yıl:",yıl)
elif cevap =="ay":
    print("ay:",ay)
elif cevap == "gün":
    print("gün:",gün)
elif cevap =="saat":
    print("saat:",saat)
elif cevap =="dakika":
    print("dakika:",dakika)
elif cevap =="saniye":
    print("saniye:",saniye)
elif cevap =="salise":
    print("salise:",salise)
else:
    print("Geçersiz seçenek. Lütfen 'tarih', 'yıl', 'ay', 'gün', 'saat', 'dakika', 'saniye' veya 'salise' yazın.")
    
    
    
    
    
    
    