import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """
    Inisialisasi Google AI dengan cache
    """
    try:
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠️ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
            st.stop()
        
        # Configure Google AI
        genai.configure(api_key=api_key)
        
        # Initialize model
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat menginisialisasi Google AI: {str(e)}")
        st.stop()

def generate_content(topic, model):
    """
    Generate konten menggunakan Google Gemini AI
    """
    try:
        # Prompt template untuk AI
        prompt = f"""
        Buatkan konten yang menarik dan informatif tentang topik: "{topic}"
        
        Format konten:
        1. Judul yang catchy
        2. Pendahuluan singkat
        3. 3-5 poin utama dengan penjelasan
        4. Kesimpulan
        5. Call to action
        
        Konten harus:
        - Mudah dipahami
        - Informatif dan berguna
        - Engaging untuk pembaca
        - Panjang sekitar 200-300 kata
        
        Gunakan bahasa Indonesia yang baik dan benar.
        """
        
        # Generate menggunakan Google AI
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def sidebar_info():
    """
    Sidebar dengan informasi tambahan
    """
    st.sidebar.header("ℹ️ Informasi")
    st.sidebar.markdown("""
    **Cara Penggunaan:**
    1. Masukkan topik di kotak input
    2. Klik tombol "Generate Konten"  
    3. Tunggu AI memproses
    4. Copy atau download hasil konten
    
    **Contoh Topik:**
    - Tips Produktivitas
    - Manfaat Olahraga
    - Teknologi AI
    - Resep Masakan
    - Travel Tips
    """)
    
    st.sidebar.divider()
    
    st.sidebar.markdown("""
    **Teknologi yang Digunakan:**
    - 🎯 Streamlit (UI Framework)
    - 🧠 Google Gemini AI
    - 🐍 Python
    """)

def run():
    """
    Stage 5: Add Styling and UI Improvements
    Menambahkan perbaikan UI, styling, dan user experience
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="AI Content Generator",
        page_icon="🚀",
        layout="wide"
    )
    
    # Sidebar info
    sidebar_info()
    
    # Judul aplikasi
    st.title("Aplikasi AI Content Generator 🚀")
    
    # Deskripsi dengan markdown
    st.markdown("""
    **Selamat datang di AI Content Generator!** 
    
    Aplikasi ini menggunakan Google Gemini AI untuk membantu Anda membuat konten berkualitas tinggi 
    berdasarkan topik yang Anda berikan. Cukup masukkan topik, klik tombol generate, dan voila! ✨
    """)
    
    # Divider untuk estetika
    st.divider()
    
    # Inisialisasi Google AI
    model = init_google_ai()
    
    # Input teks dari user dengan help text
    user_topic = st.text_input(
        "📝 Masukkan topik konten:",
        placeholder="Contoh: Tips Belajar Python, Manfaat AI dalam Bisnis, dll.",
        help="Masukkan topik apapun yang ingin Anda buatkan kontennya"
    )
    
    # Tampilkan preview topik jika ada input
    if user_topic:
        st.write(f"**Topik yang akan diproses:** {user_topic}")
    
    # Tombol untuk generate konten dengan styling
    if st.button("🔥 Generate Konten", type="primary", use_container_width=True):
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            # Loading indicator
            with st.spinner("🤖 AI sedang bekerja keras membuat konten untuk Anda..."):
                hasil_konten = generate_content(user_topic, model)
            
            st.success("✅ Konten berhasil dibuat!")
            
            # Tampilkan hasil dalam container yang rapi
            st.subheader("📄 Hasil Konten:")
            st.info(hasil_konten)
            
            # Tombol download konten
            st.download_button(
                label="📥 Download Konten",
                data=hasil_konten,
                file_name=f"konten_{user_topic.replace(' ', '_').lower()}.txt",
                mime="text/plain",
                help="Download konten sebagai file teks"
            )
    
    # Footer dengan styling HTML
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 14px;'>
        💡 <strong>Tips:</strong> Semakin spesifik topik Anda, semakin baik hasil kontennya!<br>
        Dibuat dengan ❤️ menggunakan Streamlit & Google Gemini AI
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()