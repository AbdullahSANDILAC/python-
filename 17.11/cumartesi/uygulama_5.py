# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:56:14 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("Not Hesaplama uygulaması")
st.subheader("Ders notu için notlarınızı giriniz")

vize=st.number_input("vize:")
final=st.number_input("final:")
ort=vize*0.4+final*0.6
submit=st.button("Hesapla")

if submit:
    if ort>=85 and ort<=100:
        st.success("Notunuz: AA Geçtiniz.")
        st.write(f"ortalamanız: {ort}")
    elif ort>=70 and ort<85:
        st.success("Notunuz: BA Geçtiniz.")
        st.write(f"ortalamanız: {ort}")
    elif ort>=60 and ort<70:
        st.success("Notunuz: CA Geçtiniz.")
        st.write(f"ortalamanız: {ort}")
    else:
        st.success("Notunuz: DD Kaldınız.")
        st.write(f"ortalamanız: {ort}")
else:
    st.error("girilen deger hatalı")
        
        
        
        
        
        