# 🎤 AI Meeting Assistant

A simple AI-based tool that converts meeting audio into structured insights using **Speech-to-Text** and LLMs.

---

## 🚀 What it does

* 🎧 Converts audio → text (Speech-to-Text)
* 🧠 Cleans financial/product terms
* 📝 Generates meeting summary
* 📌 Extracts tasks

---

## 🔥 Core Feature: Speech-to-Text

This project uses **Whisper** to transcribe audio files:

```python
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en"
)
```

* Supports `.wav`, `.mp3`, etc.
* Uses **FFmpeg** for audio processing

---

## 📂 Project Structure

```
.
├── main.py              # Run main app
├── llm.py               # LLM logic (Groq + LangChain)
├── trialSST.py          # Speech-to-text pipeline
├── getaudio.py          # Audio handling
├── testinterface.py     # Gradio UI
├── audio_sample.wav     # Sample input
├── requirements.txt
└── README.md
```

---

## ▶️ Setup & Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add API key

Create `.env`:

```
GROQ_API_KEY=your_api_key
```

### 3. Run

```
python main.py
```

---

## ⚠️ Requirements

* Python 3.10/3.11
* FFmpeg installed (required for audio)

---

## 📌 Note

This is a **base project** demonstrating how speech-to-text can be used as the foundation for building AI-powered meeting tools.

---
