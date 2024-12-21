# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:38:36 2024

@author: Hewlett-Packard
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

from tkinter import *
from tkinter import messagebox

df_2 = pd.read_csv("son_sat_ev_3.csv")
df_2.drop("Unnamed: 0", axis=1,inplace=True)
df = df_2.copy()
df = df[["Fiyat","Oda","Alan","Yas","Kat"]]

X = df.drop(["Fiyat"], axis=1)
y = df["Fiyat"]

label_encoders ={}
for col in X.select_dtypes(include=["object"]).columns:
    label_encoders[col] = LabelEncoder()
    X[col] = label_encoders[col].fit_transform(X[col])
    
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

#pencere oluşturma

pencere = Tk()
pencere.title("Ev fiyat tahmini")

def tahmin_et():
    oda = int(entry_oda.get())
    alan = int(entry_alan.get())
    yas =int(entry_yas.get())
    kat = int(entry_kat.get())
    
    girdi = [[oda,alan,yas,kat]]
    tahmin = model.predict(girdi)
    #tahmini ikinci bir pencerede göster
    messagebox.showinfo("Tahmin",f"Tahmini fiyat:{tahmin[0]} tl")


label_oda =Label(pencere, text="Oda sayısı")
label_oda.grid(row=0,column=0)
entry_oda = Entry(pencere)
entry_oda.grid(row=0,column=1)


label_alan =Label(pencere, text="alan (m2)")
label_alan.grid(row=1,column=0)
entry_alan = Entry(pencere)
entry_alan.grid(row=1,column=1)

label_yas =Label(pencere, text="Bina Yaşı")
label_yas.grid(row=2,column=0)
entry_yas = Entry(pencere)
entry_yas.grid(row=2,column=1)

label_kat =Label(pencere, text="kat bilgisi")
label_kat.grid(row=3,column=0)
entry_kat = Entry(pencere)
entry_kat.grid(row=3,column=1)

#tahmin et butonu 
tahmin_buton = Button(pencere, text="Tahmin et", command=tahmin_et)
tahmin_buton.grid(row=4,columnspan=2)

pencere.mainloop()








    