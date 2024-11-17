# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:53:07 2024

@author: Hewlett-Packard
"""
"""
with open("dosya.txt","r+",encoding="utf-8") as dosya:
    liste = dosya.readlines()
    print(liste)
    liste.insert(4,"4.satıra kayıt eklendi\n")
    print(liste)
    dosya.seek(0)
    for i in liste:
        dosya.write(i)
    dosya.close
"""
with open("dosya.txt","r+",encoding="utf-8") as dosya:
    liste = dosya.readlines()
    print(liste)
    liste.remove("4.satıra kayıt eklendi\n")
    print(liste)
    dosya.close()
with open("dosya.txt","w",encoding="utf-8") as dosya:
    dosya.seek(0)
    for i in liste:
        dosya.write(i)
dosya.close()
    
    
    
    
    
    
    