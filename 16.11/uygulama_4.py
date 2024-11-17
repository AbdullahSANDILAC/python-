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
    st.write(f"***Kitap Adı : {kitap_ismi}")
    st.write(f"***Değerlendirme : {puan}")
    st.write(f"***Yorum : {yorum}")
    st.write("-----------------------")