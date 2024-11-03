# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:53:44 2024

@author: Hewlett-Packard
"""

import time
from datetime import timedelta, datetime

#zamanın saniye cinsinde degeri
zaman_saniye= time.time()
print(zaman_saniye)

#zamanı UTC'ye çevir

utc_zaman = datetime.utcfromtimestamp(zaman_saniye)
#print(utc_zaman)


#Türkiye saat dilimi (utc+3)
turkiye_saati = utc_zaman+timedelta(hours=3)

#Zamanı istediğimiz formatta ekrana yazdır
zaman_formati= turkiye_saati.strftime('%Y-%m-%d %H:%M:%S')
print("tÜRKİYE SAATİ:",zaman_formati)
"""
"""

from datetime import datetime
import pytz

#türkiye zaman diilimi
turkiye_zaman=pytz.timezone('Europe/Istanbul')
print(turkiye_zaman)

simdiki_zaman = datetime.now(tz=turkiye_zaman)

print("Türkiye şuan saati:",simdiki_zaman.strftime('%y-%m-%d %H:%M:%S'))

"""
strftime('%Y-%m-%d %H:%M:%S')

%A-->HAFTANIN GÜNÜN TAM ADI
%B--> AYIN TAM ADINI VERİR
½y-->yılın son iki rakamı

"""

# DİJİTAL SAAT


from datetime import datetime
import time

while True:
    yerel_saat= time.localtime()
    yenisaat = time.strftime("%H:%M", yerel_saat)
    print(yenisaat)
    time.sleep(60)


#ZAMANLAYICI OLUŞTURMA

while True:
    print("Suyunuzu içiniz")
    time.sleep(3600) #her bir saatte bir suyunuzu içiniz uyarısı verir.
    













