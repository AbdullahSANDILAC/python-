# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:16:36 2024

@author: Hewlett-Packard
"""

import streamlit as st

def toplama_islemi(sayi1,sayi2):
    return sayi1+sayi2

st.title("Toplama Uygulaması")

sayi1 = st.number_input("Birinci sayı:")
sayi2 = st.number_input("ikinci sayi:")

#sonuc = toplama_islemi(sayi1, sayi2)
#st.success(f"Toplama sonucu: {sonuc}")

if st.button("Topla"):
    sonuc = toplama_islemi(sayi1, sayi2)
    st.success(f"Toplama sonucu: {sonuc}")