# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:52:48 2024

@author: Hewlett-Packard
"""
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('movie_rating.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS filmler(
    name TEXT,
    puan INTEGER)
''')
conn.commit()

st.title("film adı")
film_ad = st.text_input("film adi:")
puan = st.slider("puan",1,10)
submit = st.button("puan kaydet")

if submit:
    cursor.execute('INSERT INTO filmler (name,puan) VALUES (?,?)',(film_ad,puan))
    conn.commit()
    st.success("başarıyla kaydedildi")
    

cursor.execute('SELECT * FROM filmler')
data = cursor.fetchall()
df = pd.DataFrame(data, columns=['Film','Puan'])
if not df.empty:
    fig,ax = plt.subplots()
    ax.bar(df["Film"],df["Puan"])
    ax.set_title("film puanları")
    ax.set_xlabel("film adı")
    ax.set_ylabel("puan")
    st.pyplot(fig)
else:
    st.write("Henüz veri eklenemedi")
    

















