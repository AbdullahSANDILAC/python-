# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:48:07 2024

@author: Hewlett-Packard
"""

import streamlit as st
import sqlite3


baglanti = sqlite3.connect('yemek.db')
cursor= baglanti.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS yemek(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    icerik TEXT NOT NULL,
    turu TEXT NOT NULL)
''')

def yemek_ekle(name,icerik,turu):
    cursor.execute("INSERT INTO yemek (name,icerik,turu) VALUES (?,?,?)",(name,icerik,turu))
    baglanti.commit()
    
def yemek_ara(arananveri):
    cursor.execute("SELECT * FROM yemek WHERE name like?",('%'+arananveri+'%',))
    data =cursor.fetchall()
    return data

st.title("YEMEK TARİFLERİ UYGULAQMASI")
menu = ["yemek tarifi ekle","yemek tarifleri","yemek ara"]
secenek = st.sidebar.selectbox("menü",menu)

if secenek == "yemek tarifi ekle":
    st.subheader("yemek tarifi ekleme formu")
    
    yemek_adi = st.text_input("yenek adını giriniz:")
    yemek_icerik = st.text_area("yemek tarifif açıklaması:")
    yemek_turu = st.text_input("yemek türü:")
    submit = st.button("tarif ekle")
    if submit:
        yemek_ekle(yemek_adi,yemek_icerik,yemek_turu)
        st.success("tarif eklendi")

elif secenek=="yemek ara":
    st.subheader("yemek arama alanı")
    aranan = st.text_input("lütfen yemek adını giriniz:")
    submit = st.button("Yemek ara")
    if submit:
        sonuc = yemek_ara(aranan)
        if sonuc:
            for veri in sonuc:
                st.write(f"**yemek adı**: {veri[1]}")
                st.write(f"**yemek icerik**: {veri[2]}")
                st.write(f"**yemek tütü**: {veri[3]}")
        else:
            st.write("yemek bulunamadı")
    
    
    
    
    
    

