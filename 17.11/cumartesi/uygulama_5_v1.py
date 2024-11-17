# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:02:06 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("Üniversite Ortalama Hesaplama")
st.subheader("Ders Notu İçin Notlarınızı Giriniz : ")

vize = st.number_input("Vize : ")
final = st.number_input("Final : ")
ort = vize *0.4 + final * 0.6
submit = st.button("Hesapla")
if submit:
    if ort >= 45 and ort <= 60:
        st.write(f"Ortalamanız {ort}")
        st.error("Notunuz CC Geçemediniz :(")
    elif ort > 60 and ort <= 80:
        st.write(f"Ortalamanız {ort}")
        st.warning("Notunuz BB Zar Zorda Olsa Geçtiniz :s")
    elif ort > 80 and ort <= 100:
        st.write(f"Ortalamanız {ort}")
        st.success("Notunuz AA Geçtiniz :)")