import streamlit as st
from googletrans import Translator
import pyperclip
from gtts import gTTS
import os

# Page configuration - LIGHT MODE ONLY
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean light UI
st.markdown("""
    <style>
    /* Force light theme */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff;
    }
    
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Main container styling */
    .main {
        background-color: #ffffff;
        padding: 2rem;
    }
    
    /* Text areas with better visibility */
    .stTextArea textarea {
        font-size: 18px !important;
        color: #000000 !important;
        background-color: #f8f9fa !important;
        border: 2px solid #dee2e6 !important;
        border-radius: 10px !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        font-size: 16px !important;
        border: 2px solid #dee2e6 !important;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: #1a73e8;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #5f6368;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Language section headers */
    .lang-header {
        color: #202124;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Result box styling */
    .result-box {
        background-color: #e8f5e9;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #81c784;
        margin: 1rem 0;
        font-size: 18px;
        color: #1b5e20;
        min-height: 100px;
    }
    
    /* Info box */
    .info-box {
        background-color: #e3f2fd;
        padding: 0.75rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        color: #0d47a1;
        margin: 0.5rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 0.5rem 2rem !important;
        border-radius: 8px !important;
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">🌍 Language Translator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Translate text between languages instantly and easily</p>', unsafe_allow_html=True)

# Initialize translator
translator = Translator()

# Dictionary of supported languages
LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Japanese': 'ja',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Korean': 'ko',
    'Arabic': 'ar',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Turkish': 'tr',
    'Dutch': 'nl',
    'Polish': 'pl',
    'Swedish': 'sv',
    'Greek': 'el',
    'Hebrew': 'he',
    'Thai': 'th',
    'Vietnamese': 'vi',
    'Indonesian': 'id',
    'Malay': 'ms',
    'Filipino': 'fil'
}

# Language selection section
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="lang-header">📝 From</p>', unsafe_allow_html=True)
    source_lang = st.selectbox(
        "Source Language",
        options=['Auto-detect'] + list(LANGUAGES.keys()),
        key='source',
        label_visibility="collapsed"
    )

with col2:
    st.markdown('<p class="lang-header">🎯 To</p>', unsafe_allow_html=True)
    target_lang = st.selectbox(
        "Target Language",
        options=list(LANGUAGES.keys()),
        index=1,
        key='target',
        label_visibility="collapsed"
    )

st.markdown("<br>", unsafe_allow_html=True)

# Text input area
st.markdown('<p class="lang-header">💬 Enter Your Text</p>', unsafe_allow_html=True)
input_text = st.text_area(
    "Input text",
    height=150,
    placeholder="Type or paste your text here...",
    key='input',
    label_visibility="collapsed"
)

# Translate button (centered)
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    translate_btn = st.button("🔄 Translate Now", type="primary", use_container_width=True)

# Translation logic
if translate_btn and input_text:
    try:
        with st.spinner('Translating...'):
            # Get language codes
            src_code = 'auto' if source_lang == 'Auto-detect' else LANGUAGES[source_lang]
            dest_code = LANGUAGES[target_lang]
            
            # Perform translation
            translation = translator.translate(
                input_text,
                src=src_code,
                dest=dest_code
            )
            
            # Store translation in session state
            st.session_state['translated_text'] = translation.text
            st.session_state['detected_lang'] = translation.src
            
    except Exception as e:
        st.error(f"Translation error: {str(e)}")

# Display translated text
if 'translated_text' in st.session_state:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="lang-header">✨ Translation Result</p>', unsafe_allow_html=True)
    
    # Show detected language if auto-detect was used
    if source_lang == 'Auto-detect':
        detected = st.session_state.get('detected_lang', 'unknown')
        lang_name = [k for k, v in LANGUAGES.items() if v == detected]
        if lang_name:
            st.markdown(f'<div class="info-box">🔍 Detected language: <strong>{lang_name[0]}</strong></div>', 
                       unsafe_allow_html=True)
    
    # Display translation
    st.markdown(f'<div class="result-box">{st.session_state["translated_text"]}</div>', 
                unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Copy", use_container_width=True):
            try:
                pyperclip.copy(st.session_state['translated_text'])
                st.toast("✅ Copied to clipboard!", icon="✅")
            except:
                st.warning("Copy feature requires clipboard access")
    
    with col2:
        if st.button("🔊 Listen", use_container_width=True):
            try:
                with st.spinner('Generating audio...'):
                    tts = gTTS(
                        text=st.session_state['translated_text'],
                        lang=LANGUAGES[target_lang],
                        slow=False
                    )
                    
                    audio_file = "translation_audio.mp3"
                    tts.save(audio_file)
                    
                    with open(audio_file, "rb") as f:
                        audio_bytes = f.read()
                    
                    st.audio(audio_bytes, format='audio/mp3')
                    os.remove(audio_file)
                    
            except Exception as e:
                st.error(f"Audio error: {str(e)}")
    
    with col3:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #5f6368; padding: 1rem;'>
        <p style='margin: 0;'>🌟 Powered by Google Translate API</p>
        <p style='margin: 0; font-size: 14px;'>Supports 25+ languages</p>
    </div>
""", unsafe_allow_html=True)