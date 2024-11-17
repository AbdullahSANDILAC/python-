# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:55:03 2024

@author: Hewlett-Packard
"""

import streamlit as st
import math 

st.title("Basit Bir Streamlit Uygulaması")

sayi = st.number_input("Bir sayı giriniz:")

if st.button("Karekök Hesapla"):
    karekok = math.sqrt(sayi)
    st.success(f"{sayi} sayısının karekökü: {karekok}")

st.text("Streamlit ile web tabanlı arayüz tasarlama örneği")