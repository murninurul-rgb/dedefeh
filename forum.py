import streamlit as st
import json
import os

FILE_DATA = "data_forum.json"

DATA_AWAL = [
    {"id": 1, "penulis": "Pak Budi (Tani Cabai)", "pupuk": "NPK Mutiara 16-16-16", "isi": "Pakai NPK Mutiara pas fase vegetatif bikin tunas cabai cepat rimbun!", "likes": 12},
    {"id": 2, "penulis": "Sari UrbanFarm", "pupuk": "Pupuk Organik Cair (POC)", "isi": "Buat yang nanam tomat di polybag balkon, POC air cucian beras + EM4 ampuh banget dan nggak bau.", "likes": 19},
    {"id": 3, "penulis": "Mas Dimas", "pupuk": "KNO3 Putih", "isi": "Pas mulai berbunga semprot KNO3 Putih, bunga cabai nggak gampang rontok meski hujan.", "likes": 8}
]

def muat_data():
    if not os.path.exists(FILE_DATA):
        simpan_data(DATA_AWAL)
    with open(FILE_DATA, "r", encoding="utf-8") as f:
        return json.load(f)

def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def tampilkan_forum():
    st.header("💬 TaniFeed — Forum Pengalaman & Top Pupuk")
    posts = muat_data()

    tab1, tab2 = st.tabs(["📰 Timeline Diskusi", "🏆 Top Pupuk Terpopuler"])

    with tab1:
        with st.expander("✍️ Bagikan Pengalaman Bertanimu", expanded=False):
            nama = st.text_input("Nama / Username:")
            pupuk = st.text_input("Merek / Jenis Pupuk yang Dipakai:")
            isi = st.text_area("Ceritakan pengalaman atau tipsmu:")
            if st.button("Posting ke TaniFeed"):
                if nama and pupuk and isi:
                    post_baru = {
                        "id": len(posts) + 1,
                        "penulis": nama,
                        "pupuk": pupuk,
                        "isi": isi,
                        "likes": 0
                    }
                    posts.insert(0, post_baru)
                    simpan_data(posts)
                    st.rerun()
                else:
                    st.error("Semua kolom wajib diisi!")

        st.divider()
        for idx, post in enumerate(posts):
            with st.container(border=True):
                st.subheader(f"@{post['penulis']} • 🌿 Rekomendasi: {post['pupuk']}")
                st.write(post["isi"])
                if st.button(f"❤️ Like ({post['likes']})", key=f"like_{post['id']}_{idx}"):
                    post["likes"] += 1
                    simpan_data(posts)
                    st.rerun()

    with tab2:
        st.subheader("Peringkat Pupuk & Tips Berdasarkan Like Terbanyak")
        top_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)
        for peringkat, post in enumerate(top_posts, start=1):
            st.markdown(f"**#{peringkat} — {post['pupuk']}** (❤️ {post['likes']} Likes)")
            st.caption(f"Direkomendasikan oleh @{post['penulis']}: \"{post['isi']}\"")
            st.divider()