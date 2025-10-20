import streamlit as st
bordro=True
gelir=1500000

oran1 = [0.15,0.2,0.27,0.35]
oran2 = [0.15,0.27,0.35]
gelir1 = [158000,330000,1200000,4300000]
gelir2 = [158000,330000,800000,4300000]
kalan = gelir
vergi = 0
a=0
if bordro==True:
   for i, dilim in enumerate(gelir1):
        if kalan <= 0:
           break
        tutar = min(kalan, dilim-a)
        vergi += oran1[i] * tutar
        kalan -= tutar
        a = dilim
else:
    for i, dilim in enumerate(gelir2):
        if kalan <= 0:
            break
        tutar = min(kalan, dilim-a)
        vergi += oran2[i] * tutar
        kalan -= tutar
        a = dilim

net=gelir-vergi
ay=gelir/12
aynet=net/12

print("Yıllık Gelir",gelir,"Yıllık Net Gelir",net,"Aylık Brüt Gelir",ay,"Aylık Net Gelir",aynet,"Toplam Vergi",vergi)

#pip freeze > requirements.txt