# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:43:46 2024

@author: Hewlett-Packard
"""

import streamlit as st
import requests

st.title("Rastgele Şaka Makinesi")
st.write("en iyi şakaları burada bulacaksınız")
st.image("resim.png")
submit= st.button("şaka goster")

if submit:
    url= "https://v2.jokeapi.dev/joke/Any?safe-mode"
    cevap = requests.get(url)
    if cevap.status_code == 200:
        veri = cevap.json() #¶bir http yanıtının içeriğini json formatında dönüştürmwek için kullanılır
        if veri["type"] == "single":
            sakaicerik = veri["joke"]
        else:
            sakaicerik="{}.....{}".format(veri["setup"],veri["delivery"])
        st.markdown(f"<h2 style = 'text-align:center;color:blue'>{sakaicerik}</h2>" , unsafe_allow_html=True)
    else:
        print("hata var siteye bağlanamadı.")
    st.write("------------------------")