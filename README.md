# 🌍 Language Translator App

A beautiful and interactive language translation application built with Streamlit and Google Translate API.

## ✨ Features

- 🌐 Translate between 25+ languages
- 🔍 Auto-detect source language
- 📋 Copy translated text to clipboard
- 🔊 Text-to-speech for translations
- 💫 Clean and attractive user interface
- ⚡ Real-time translation

## 📦 Installation

1. **Clone or download the project files**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run

Run the application using:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 🎯 How to Use

1. **Select Source Language**: Choose the language you're translating from (or use Auto-detect)
2. **Select Target Language**: Choose the language you want to translate to
3. **Enter Text**: Type or paste the text you want to translate
4. **Click Translate**: Press the translate button to get your translation
5. **Use Features**:
   - 📋 Copy: Copy the translation to your clipboard
   - 🔊 Listen: Hear the translation pronounced
   - 🗑️ Clear: Reset the form

## 🌍 Supported Languages

- English, Spanish, French, German, Italian
- Portuguese, Russian, Japanese, Korean
- Chinese (Simplified & Traditional)
- Arabic, Hindi, Bengali, Turkish
- Dutch, Polish, Swedish, Greek
- Hebrew, Thai, Vietnamese
- Indonesian, Malay, Filipino
- And more!

## 🛠️ Technology Stack

- **Streamlit**: Web framework for the UI
- **googletrans**: Google Translate API wrapper
- **gTTS**: Google Text-to-Speech
- **pyperclip**: Clipboard functionality

## 📝 Code Structure

The application is built in a single `app.py` file with:
- Custom CSS styling for attractive UI
- Two-column layout for language selection
- Session state management for translations
- Error handling for robust performance
- Sidebar with helpful information

## ⚠️ Notes

- Requires internet connection for translation and text-to-speech
- Clipboard functionality may require additional permissions on some systems
- Audio playback works best on modern browsers

## 🤝 Contributing

Feel free to fork, modify, and enhance this application!

## 📄 License

Open source - feel free to use for personal or commercial projects.

---

**Enjoy translating! 🌟**
