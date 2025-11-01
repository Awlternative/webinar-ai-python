import streamlit as st

st.set_page_config(page_title="AIKU", page_icon="🚀")

# 1 st.title() - untuk menampilkan judul halaman
st.title("AIKU - Aplikasi AI Pertamaku")
st.markdown("**Ini adalah aplikasi AI pertamaku**")
st.divider()

# 2. st.text_input() - untuk menginputkan user
user_topic = st.text_input("Masukkan topik konten kalian: ")

# kode untuk menampilkan prompt user
if user_topic:
    st.write(f"Prompt yang dimasukkan oleh user: {user_topic}")

#st.button() - untuk belajar tampilan button
if st.button("Kirim"):
    #validasi input
    if not user_topic.strip():
        st.warning("⚠️Mohon masukkan topik konten terlebih dahulu!")
    else:
        #simulasi hasil ai untuk latihan
        hasil_dari_ai = f""" 
        # {user_topic}

        ## Pendahuluan
        Topik "{user_topic}" adalah topik yang akan kita bahas kali ini

        ## Poin Utama
        1. **ide pertama** - ini adalah penjelasan ide pertama
        2. **ide kedua** - ini adalah penjelasan ide kedua
        3. **ide ketiga** - Informasi tambahan yang berguna

        ## Kesimpulan
        demikian pembahasan singkat tentang {user_topic}. Semoga bermanfaat!

        ---
        "Konten ini dibuat oleh AIKU - Aplikasi AI Pertamaku"
        """
        #st.info() - ini berguna untuk menampilkan hasil dari button
        st.success("✅ Konten berhasil dibuat!")
        st.info(hasil_dari_ai)

#tambahan komponen streamlit
st.divider()
st.markdown("**Komponen Streamlit Tambahan**")

#contoh komponen/widget yang serng dipakai
col1, col2 = st.columns(2)

with col1:
    st.selectbox("Pilih Streamer Favoritmu:", ["Windah Basudara", "Windah Batubara", "Windah Bersaudara", "Windah Barusadar"])

with col2:
    st.slider("pilih panjang konten (dalam kata)", 100, 500, 250)


#footer
st.divider()
st.markdown("**Developed with ❤️ by AIKU**")