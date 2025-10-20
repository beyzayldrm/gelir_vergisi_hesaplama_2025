import streamlit as st
st.set_page_config(page_title="2025 Gelir Vergisi Hesaplama", page_icon="💰", layout="centered")
st.markdown(
    "<h1 style='text-align:center; color:#007ACC;'>💰 2025 Gelir Vergisi Hesaplama</h1>",
    unsafe_allow_html=True
)
st.write("Yıllık brüt gelirini gir, gelir türünü seç; otomatik olarak vergi ve net kazanç hesaplanır. 💼")
gelir = st.number_input("Yıllık Brüt Gelir (TL)", min_value=0.0, step=1000.0, format="%.2f")
gelir_turu = st.radio("Gelir Türü Seçiniz", ["Ücretli (Bordrolu)", "Ücret Dışı"], horizontal=True)
if st.button("💡 Hesapla"):
    bordro = gelir_turu == "Ücretli (Bordrolu)"

    oran1 = [0.15, 0.2, 0.27, 0.35]
    oran2 = [0.15, 0.27, 0.35]
    gelir1 = [158000, 330000, 1200000, 4300000]
    gelir2 = [158000, 330000, 800000, 4300000]

    kalan = gelir
    vergi = 0
    a = 0

    if bordro:
        for i, dilim in enumerate(gelir1):
            if kalan <= 0:
                break
            tutar = min(kalan, dilim - a)
            vergi += oran1[i] * tutar
            kalan -= tutar
            a = dilim
    else:
        for i, dilim in enumerate(gelir2):
            if kalan <= 0:
                break
            tutar = min(kalan, dilim - a)
            vergi += oran2[i] * tutar
            kalan -= tutar
            a = dilim

    net = gelir - vergi
    ay_brut = gelir / 12
    ay_net = net / 12
    st.markdown(
        f"""
        <div style="
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 2px 10px #d0d0d0;">
            <h3 style="color:#007ACC;">Sonuç Özeti</h3>
            <p style="font-size:15px;">💼 Gelir Türü: <b>{gelir_turu}</b></p>
            <p style="font-size:15px;">📆 Yıllık Brüt Gelir: <b>{gelir:,.2f} TL</b></p>
            <p style="font-size:15px;">💰 Yıllık Net Gelir: <b style="color:#117A65;">{net:,.2f} TL</b></p>
            <p style="font-size:15px;">📉 Toplam Vergi: <b style="color:#C0392B;">{vergi:,.2f} TL</b></p>
            <hr style="border: 1px solid #ccc;">
            <p style="font-size:16px;">🗓️ Aylık Brüt: <b>{ay_brut:,.2f} TL</b> &nbsp; | &nbsp; 💵 Aylık Net: <b style="color:#117A65;">{ay_net:,.2f} TL</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

