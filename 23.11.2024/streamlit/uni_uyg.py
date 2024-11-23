# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:14:48 2024

@author: Hewlett-Packard
"""
import streamlit as st
import requests
import random

st.image("resim.png")
st.title("Rastgele Üniversite Gösterme Makinesi")

submit=st.button("Üniversite göster")

if submit:
    url="http://universities.hipolabs.com/search?country=Turkey"
    cevap = requests.get(url)
    if cevap.status_code ==200:
        data = cevap.json()
        #universite = data[0] #ilk üniversite seçtik
        universite = random.choice(data) #rastgele bir universite seçtik
        uni_name = universite["name"]
        uni_ulke = universite["country"]
        uni_web_sayfa = universite["web_pages"][0]
        st.markdown(f"<h2 style='text-align:center;color:green'>{uni_name}</h2>", unsafe_allow_html=True)
        st.write(f"Ülke:{uni_ulke}")
        st.write(f"web sitesi:{uni_web_sayfa}")
    else:
        st.error("Siteye bağlanılamadı.Lütfen tekrar deneyiniz.")