import streamlit as st
from google import genai

def tampilkan_ai_konsultan():
    st.header("🤖 AI Konsultan Hama & Penyakit Tanaman")
    st.caption("Tanyakan gejala tanamanmu (misal: daun keriting, bercak kuning, atau layu) untuk mendapat saran penanganan.")

    api_key = st.text_input("Masukkan Gemini API Key:", type="password", help="Dapatkan gratis di Google AI Studio")

    if "riwayat_chat" not in st.session_state:
        st.session_state.riwayat_chat = []

    for pesan in st.session_state.riwayat_chat:
        with st.chat_message(pesan["role"]):
            st.markdown(pesan["content"])

    if pertanyaan := st.chat_input("Ketik keluhan tanamanmu di sini..."):
        if not api_key:
            st.error("Masukkan Gemini API Key terlebih dahulu di kolom atas!")
            return

        st.session_state.riwayat_chat.append({"role": "user", "content": pertanyaan})
        with st.chat_message("user"):
            st.markdown(pertanyaan)

        with st.chat_message("assistant"):
            try:
                client = genai.Client(api_key=api_key)
                prompt_sistem = (
                    "Kamu adalah pakar agronomi dan pertanian ramah pemula. "
                    "Jawab keluhan pertanian berikut secara terstruktur, singkat, dan praktis "
                    "(meliputi: kemungkinan penyebab, langkah penanganan awal, dan pencegahan): "
                )
                respons = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt_sistem + pertanyaan
                )
                jawaban = respons.text
                st.markdown(jawaban)
                st.session_state.riwayat_chat.append({"role": "assistant", "content": jawaban})
            except Exception as e:
                st.error(f"Terjadi kesalahan koneksi API: {e}")