# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:23:36 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("SORU - CEVAP UYULAMASI")

s1_cevap = st.text_input("türkiya'nin başkenti?")
s2_cevap = st.text_input("türkiya'nin bitki örtüsü?")
s3_cevap = st.text_input("akdeniz bitki örtüsü?")
s4_cevap = st.text_input("tüdünya kaç kıtadan oluşur")
s5_cevap = st.text_input("uçmayan kuş türü?")

submit=st.button("kontrol et")
skor=0

if submit:
    if s1_cevap=="ankara":
        st.success("doğru cevapladınız")
        skor = skor+1
    else:
        st.error("yanlış cevap")
    if s2_cevap=="maki":
        st.success("doğru cevapladınız")
        skor = skor+1
    else:
        st.error("yanlış cevap")
    if s3_cevap=="7":
        st.success("doğru cevapladınız")
        skor = skor+1
    else:
        st.error("yanlış cevap")
    if s4_cevap=="maki":
        st.success("doğru cevapladınız")
        skor = skor+1
    else:
        st.error("yanlış cevap")
    if s5_cevap=="tavuk":
        st.success("doğru cevapladınız")
        skor = skor+1
    else:
        st.error("yanlış cevap")
    st.write("sonuç",skor)
        
        
        
        
        