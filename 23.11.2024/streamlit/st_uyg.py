# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:05:06 2024

@author: Hewlett-Packard
"""

import streamlit as st 

tab1, tab2, tab3, tab4 =st.tabs(["yazma ve metin Öğleri","Grafik Öğleri", "Giriş Araçları","Durum Öğleri"])

with tab1:
    st.title("Stremalit Kütüphanesi")
    st.markdown(" başlık türleri")
    with st.echo():
        st.title("başlık")
        st.header("alt başlık")
        st.subheader("bir alt başlık")
        
with tab2:
    st.markdown("st.area_chart kullanımı")
    with st.echo():
        gunler = ["pazaqrtesi","salı","çarşamba","perşembe","cuma"]
        st.area_chart(gunler)
    st.markdown("st.line_chart kullanımı")
    with st.echo():
        gunler = ["pazaqrtesi","salı","çarşamba","perşembe","cuma"]
        st.line_chart(gunler)
    st.markdown("st.bar_chart kullanımı")
    with st.echo():
        gunler = ["pazaqrtesi","salı","çarşamba","perşembe","cuma"]
        st.bar_chart(gunler)

with tab3:
    st.markdown("st.slider kullanımı")
    with st.echo():
        yas = st.slider("Kaç yaşındasınız",0,130,22)
        st.write("Ben",yas,"yaşındayım")
    st.markdown("st.multıselect kullanımı")
    with st.echo():
        secenek = st.multiselect(
            'Farori renginiz nedir?',
            ['Yesşil',"Sarı","Kırmızı","Mavi"],
            ['Sarı',"Kırmızı"])
        st.write("Seçimleriniz",secenek)

with tab4:
    with st.echo():
        st.image("resim.png")
        
    "---"
    
    st.markdown("* st.balloons kullanımı")
    with st.echo():
        st.balloons()
        
    "---"
    
    st.markdown("* st.snow kullanımı")
    with st.echo():
        st.snow()
        
    "---"
    
    st.markdown("* st.error kullanımı")
    with st.echo():
        st.error("Hata mesajı!")
        
    "---"
    
    st.markdown("* st.warning kullanımı")
    with st.echo():
        st.warning("Uyarı mesajı!")
        
    "---"
    
    st.markdown("* st.info kullanımı")
    with st.echo():
        st.info("Bilgi mesajı!")
        
    "---"
    
    st.markdown("* st.success kullanımı")
    with st.echo():
        st.success("Başarı mesajı!")
        
        
        
        
        
        
        
        
        