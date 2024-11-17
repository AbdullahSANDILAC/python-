# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:45:39 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("Kullanıcı giriş formu")
st.subheader("Lütfen bilgileriniz giriniz")

k_kullanici = "admin"
k_sifre = "1234"

username = st.text_input("kullanıcı adınız giriniz:")
password = st.text_input("şifrenizi giriniz:")

if st.button("Giriş"):
    if username == k_kullanici and password == k_sifre:
        st.write("giriş başarılı")
        st.balloons()
    else:
        st.error("kullanıcı adı veya şifre hatalı")
    st.write("if koşulu çalıtı-------------")
else:
    st.write("henüz giriş yapılmadı")
        
        
        
        
        
        
