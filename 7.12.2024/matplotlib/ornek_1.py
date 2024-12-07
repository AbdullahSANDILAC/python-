# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:17:02 2024

@author: Hewlett-Packard
"""

import streamlit as st
import matplotlib.pyplot as plt

st.title("Matplotlip bar grafiği")

#veri notlarını tanımlama
kategori =['kategori a','kategori b','kategori c']
deger = [10,20,15]
fig,ax =plt.subplots()
ax.bar(kategori,deger)
ax.set_title("bar grafiği")
ax.set_xlabel("kategoriler")
ax.set_ylabel("değerler")

st.pyplot(fig)

