# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:24:05 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("KİTAP DEĞERLENDİRME UYGULAMASI")
st.subheader("Lütfen değerlendirme yapağınız verileri giriniz")

st.sidebar.header("burası yeni menü")
kitap_ismi = st.sidebar.text_input("Lütfen kitap ismini giriniz")
puan = st.sidebar.slider("değerlendirme",1,10)
yorum = st.sidebar.text_area("yorum yapınız")
submit = st.sidebar.button("yorum ekle")

if submit:
    with open("metin.txt","a", encoding="utf-8") as file:
        file.write(f"{kitap_ismi},{puan},{yorum}\n")
    st.write("değerlendirmeniz kaydedilmiştir.")
with open("metin.txt","r",encoding="utf-8") as file:
    metinler = file.read()
    st.write(metinler)