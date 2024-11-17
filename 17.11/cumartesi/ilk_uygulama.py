# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:30:00 2024

@author: Hewlett-Packard
"""

import streamlit as st

st.title("Deneme mesajı")

st.header("Daha küçük boyutta başlık")
st.subheader("Alt başlıjk")
st.text("Metin gösterir")
st.write("metin gösterir")

st.button("Gönder")
st.checkbox("onay kutusu metini")
st.selectbox("iller",["adana","adıyaman","ankara","istanbul"])
st.radio("iller",["adana","adıyaman","ankara","istanbul"])
st.multiselect("iller",["adana","adıyaman","ankara","istanbul"])

st.text_input("tek satırlı metin girişi")
st.text_area("çok satırlı metin girişi")

st.date_input("tarih girişi")
st.time_input("saat girişi")

st.file_uploader("dosya yükleyici")



