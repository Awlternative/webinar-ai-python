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

def run():
    """
    Stage 4: Add AI Integration
    Menambahkan integrasi penuh dengan Google Gemini AI
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="AI Content Generator",
        page_icon="🚀"
    )
    
    # Judul aplikasi
    st.title("AI Content Generator 🚀")
    
    # Teks pembuka
    st.write("Selamat datang di aplikasi AI Content Generator!")
    st.write("Aplikasi ini menggunakan Google Gemini AI untuk membuat konten berkualitas.")
    
    # Inisialisasi Google AI
    model = init_google_ai()
    
    st.divider()
    
    # Input teks dari user
    user_topic = st.text_input(
        "📝 Masukkan topik konten:",
        placeholder="Contoh: Tips Belajar Python, Manfaat AI dalam Bisnis, dll."
    )
    
    # Tampilkan topik yang dimasukkan user
    if user_topic:
        st.write(f"**Topik yang akan diproses:** {user_topic}")
    
    # Tombol untuk generate konten
    if st.button("🔥 Generate Konten", type="primary"):
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            # Generate konten menggunakan AI
            with st.spinner("🤖 AI sedang bekerja keras membuat konten untuk Anda..."):
                hasil_konten = generate_content(user_topic, model)
            
            st.success("✅ Konten berhasil dibuat!")
            st.subheader("📄 Hasil Konten:")
            st.info(hasil_konten)

if __name__ == "__main__":
    run()