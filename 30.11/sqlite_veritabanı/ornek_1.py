# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:07:47 2024

@author: Hewlett-Packard
"""

import streamlit as st
import sqlite3 

baglanti =sqlite3.connect('kayitlar.db')
cursor = baglanti.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    yas TEXT NOT NULL)
''')

st.title("basit kullanıcı kayıt uygulaması")

name = st.text_input("adınızı giriniz:")
yas = st.number_input("yaş giriniz:", min_value=0)
submit =st.button("Kaydet")

if submit:
    cursor.execute('INSERT INTO users (name,yas) VALUES (?,?)',(name,yas))
    baglanti.commit()
    st.success("kullanıcı başarıyla kaydedildi.")

kullanıcı_goster = st.button("kullanıcıları göster")
if kullanıcı_goster:
    st.header("Kullanıcılar")
    cursor.execute("select * from users")
    #alınana veriler bir liste olarak döner ve her bir öğe bir demet olarak temsil edilir
    data = cursor.fetchall()
    for veri in data:
        st.write(f"İsim: {veri[1]}, Yaş: {veri[2]}")
    
    
    
    
    
    
    
    
    
    