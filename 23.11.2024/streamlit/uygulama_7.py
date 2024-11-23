# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:46:48 2024

@author: Hewlett-Packard
"""

import streamlit as st
import json

with open("kitaplar.json","r", encoding="utf-8") as file:
    kitap_listesi = json.load(file)
    for kitap in kitap_listesi["kitaplar"]:
        st.write("kitap adı:",kitap["adi"])
        st.write("kitap yazarı:",kitap["yazar"])
        st.write("kitap notunuz:",kitap["yorum"])
        st.write("---------------")
    
st.sidebar.header("kitap değerlendirme uygulaması")

kitap_adi = st.sidebar.text_input("kitap adını giriniz:")
kitap_yazar = st.sidebar.text_input("yazar adı:")
kitap_yorum = st.sidebar.text_input("yarumunuz")
submit = st.sidebar.button("yorum ekle")

if submit:
    kitap_listesi["kitaplar"].append({"adi":kitap_adi,"yazar":kitap_yazar,"yorum":kitap_yorum})
    with open ("kitaplar.json","w",encoding="utf-8") as file:
        json.dump(kitap_listesi,file)
    
    st.sidebar.success("kitap başarıyla eklendi")
    st.experimental_rerun() #bu komut sayfayı yeniler