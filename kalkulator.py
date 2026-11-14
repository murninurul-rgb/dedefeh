import streamlit as st
from datetime import datetime, timedelta

DATA_TANAMAN = {
    "Cabai Rawit": {
        "urea_per_m2": 0.02,
        "npk_per_m2": 0.03,
        "bibit_per_m2": 1500,
        "masa_panen_hari": 75,
        "musim_terbaik": "Awal Kemarau (April - Mei) atau Akhir Hujan (September)"
    },
    "Tomat": {
        "urea_per_m2": 0.015,
        "npk_per_m2": 0.025,
        "bibit_per_m2": 1200,
        "masa_panen_hari": 65,
        "musim_terbaik": "Musim Kemarau (Mei - Agustus) dengan penyiraman teratur"
    },
    "Jagung Manis": {
        "urea_per_m2": 0.03,
        "npk_per_m2": 0.02,
        "bibit_per_m2": 800,
        "masa_panen_hari": 70,
        "musim_terbaik": "Awal Musim Hujan (Oktober - November)"
    }
}

HARGA_UREA = 3000
HARGA_NPK = 3500

def tampilkan_kalkulator():
    st.header("🧮 Kalkulator Pupuk, Modal & Kalender Tanam")
    
    tanaman_pilihan = st.selectbox("Pilih Komoditas Tanaman:", list(DATA_TANAMAN.keys()))
    luas_lahan = st.number_input("Masukkan Luas Lahan (m²):", min_value=1.0, value=10.0, step=1.0)
    tanggal_tanam = st.date_input("Rencana Tanggal Mulai Tanam:", datetime.today())

    if st.button("Hitung Estimasi Tanam"):
        info = DATA_TANAMAN[tanaman_pilihan]
        
        kebutuhan_urea = info["urea_per_m2"] * luas_lahan
        kebutuhan_npk = info["npk_per_m2"] * luas_lahan
        total_modal = (kebutuhan_urea * HARGA_UREA) + (kebutuhan_npk * HARGA_NPK) + (info["bibit_per_m2"] * luas_lahan)
        estimasi_panen = tanggal_tanam + timedelta(days=info["masa_panen_hari"])

        st.success(f"Hasil Perhitungan untuk **{tanaman_pilihan}** seluas **{luas_lahan} m²**:")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Pupuk Urea", f"{kebutuhan_urea:.2f} kg")
        col2.metric("Pupuk NPK", f"{kebutuhan_npk:.2f} kg")
        col3.metric("Estimasi Modal", f"Rp {total_modal:,.0f}")

        st.info(f"📅 **Perkiraan Tanggal Panen:** {estimasi_panen.strftime('%d %B %Y')} ({info['masa_panen_hari']} hari setelah tanam)")
        st.warning(f"🌤️ **Rekomendasi Waktu Tanam Terbaik:** {info['musim_terbaik']}")

        