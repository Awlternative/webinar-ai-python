import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """Inisialisasi Google AI dengan cache"""
    try:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠️ Google API Key tidak ditemukan! Tambahkan ke file .env")
            st.stop()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat inisialisasi Google AI: {str(e)}")
        st.stop()

def generate_content(topic, model, style, word_count):
    """Generate konten menggunakan Google Gemini AI"""
    try:
        if style == "Santai (Gen Z & Milenial)":
            tone = """
            - Gunakan bahasa ringan, gaul, dan tetap sopan.
            - Hindari kata yang terlalu formal atau baku.
            - Gunakan emoji bila relevan (tidak berlebihan).
            - Tulis seperti sedang ngobrol santai dengan pembaca online.
            """
        else:
            tone = """
            - Gunakan bahasa formal dan profesional.
            - Hindari slang, emoji, atau bahasa gaul.
            - Gunakan struktur yang rapi dan jelas.
            - Cocok untuk konteks bisnis, pendidikan, atau profesional.
            """

        prompt = f"""
        Kamu adalah AI content writer bernama AIKU yang sangat ahli dalam menulis konten
        media sosial dan artikel pendek yang menarik, jelas, dan sesuai konteks audiens.

        Tugasmu:
        Buatkan konten tentang topik: "{topic}"

        Struktur konten:
        1. Judul (maks 10 kata, relevan dan menarik)
        2. Pendahuluan singkat (1 paragraf)
        3. 3–5 poin isi utama dengan penjelasan
        4. Kesimpulan (1 paragraf)
        5. Call to action (1 kalimat ajakan)

        Gaya penulisan:
        {tone}

        Ketentuan tambahan:
        - Panjang sekitar {word_count} kata.
        - Harus informatif, engaging, dan mudah dibaca.
        - Bahasa Indonesia yang baik dan benar.

        Tujuan:
        Membuat pembaca merasa terhubung dan tertarik untuk membagikan atau menindaklanjuti konten ini.
        """

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def run():
    """Menjalankan aplikasi utama"""
    st.set_page_config(page_title="AIKU", page_icon="🚀")

    # Sidebar info
    with st.sidebar:
        st.header("💡 Tentang AIKU")
        st.markdown("""
        **AIKU** adalah aplikasi berbasis **Google Gemini AI**  
        yang membantu kamu membuat konten media sosial dengan cepat dan sesuai gaya yang kamu pilih.

        ### Langkah Penggunaan:
        1. Masukkan topik konten  
        2. Pilih gaya bahasa  
        3. Tentukan panjang kata  
        4. Klik **🔥 Generate Konten**

        ### Mode Gaya:
        - 😎 Santai (Gen Z & Milenial)  
        - 💼 Formal (Profesional)

        """)
        st.divider()
        st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size:14px;'><strong>Developed with ❤️ + GPT🤣</strong></p>
            <p style='font-size:15px;'>Supported by Aruta Mentor</p>
            <p style='font-size:11px;'>Wahyu Maulana & Haris Al-Rasyid</p>
            <p style='font-size:10px;'>Powered by Google Gemini AI & Streamlit</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([4, 5])  
    with col1:
        st.write("🚀 AIKU")
        st.write("Selamat datang di **AIKU**, bantu kamu bikin konten keren, cepat, dan sesuai gaya pilihanmu!")

    with col2:
        style = st.radio(
            "🎭 Pilih gaya bahasa:",
            ["Santai (Gen Z & Milenial)", "Formal (Profesional)"],
            horizontal=True
        )
        word_count = st.slider(
            "📏 Tentukan panjang konten (kata):",
            min_value=100,
            max_value=500,
            value=250,
            step=50
        )

    st.divider()
    model = init_google_ai()

    # --- Input di bagian bawah (chat style) ---
    user_topic = st.chat_input("📝 Masukkan topik konten (misal: Tips Belajar Python, Manfaat AI, dll)")

    # --- Logika pemrosesan ---
    if user_topic:
        st.write(f"**Topik:** {user_topic}")
        st.write(f"**Gaya Bahasa:** {style}")
        st.write(f"**Panjang:** ~{word_count} kata")

        with st.spinner("🤖 AIKU sedang menulis konten..."):
            hasil_konten = generate_content(user_topic, model, style, word_count)

        st.success("✅ Konten berhasil dibuat!")
        st.subheader("📄 Hasil dari AIKU:")
        st.info(hasil_konten)

    

if __name__ == "__main__":
    run()
