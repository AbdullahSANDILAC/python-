# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:52:08 2024

@author: Hewlett-Packard
"""

import requests

istek = requests.get("https://www.google.com/")
print(istek.status_code,"başarılı google bağlanıyor")