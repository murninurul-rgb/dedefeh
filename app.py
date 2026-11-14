import streamlit as st
from kalkulator import tampilkan_kalkulator
from forum import tampilkan_forum
from ai_konsultan import tampilkan_ai_konsultan

st.set_page_config(
    page_title="AgroMate - Asisten Pertanian Modern",
    page_icon="🌱",
    layout="wide"
)

# CSS ringan untuk memperhalus kartu & tombol
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
    .banner-box {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        padding: 20px 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=70)
    st.title("AgroMate")
    st.caption("Platform Cerdas Petani Pemula & Urban Farming")
    st.divider()
    
    menu = st.radio(
        "Navigasi Utama:",
        [
            "🧮 Kalkulator & Kalender Tanam",
            "💬 Forum TaniFeed & Top Pupuk",
            "🤖 AI Konsultan Tani"
        ]
    )
    st.divider()
    st.info("💡 **Tips:** Gunakan kalkulator sebelum membeli bibit agar modal lebih terukur.")

# Header Banner Utama
st.markdown("""
    <div class="banner-box">
        <h2 style="margin:0; color:white;">🌱 AgroMate — Smart Farming Assistant</h2>
        <p style="margin:5px 0 0 0; opacity:0.95;">Hitung kebutuhan tanam, temukan rekomendasi pupuk terbaik, dan konsultasi hama secara instan.</p>
    </div>
""", unsafe_allow_html=True)

# Routing Halaman
if menu == "🧮 Kalkulator & Kalender Tanam":
    tampilkan_kalkulator()
elif menu == "💬 Forum TaniFeed & Top Pupuk":
    tampilkan_forum()
elif menu == "🤖 AI Konsultan Tani":
    tampilkan_ai_konsultan()