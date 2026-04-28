# 🎤 AI Meeting Assistant

A basic AI project that converts meeting audio into useful insights using **Speech-to-Text (STT)** and LLMs.

---

## 🚀 Features

* 🎧 Audio → Text transcription (core feature)
* 🧠 Financial term normalization
* 📝 Meeting summary generation
* 📌 Task extraction

---

## 🔥 Core Focus: Speech-to-Text

This project uses **Whisper** to convert audio into text:

```python
pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en"
)
```

* Handles `.wav`, `.mp3`, etc.
* Uses **FFmpeg** for audio decoding
* Acts as the base for all further processing

---

## 📂 Project Structure

```
.
├── app/
│   └── main.py              # Gradio UI
│
├── services/
│   ├── getaudio.py          # Audio handling
│   ├── llm.py               # Groq + LangChain logic
│   ├── pipeline.py          # End-to-end flow (STT → LLM)
│
├── testing/
│   └── testinterface.py     # test UI
│
├── audio_sample.wav
├── requirements.txt
└── README.md
```

---

## ▶️ Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add API key

Create `.env`:

```
GROQ_API_KEY=your_api_key
```

### 3. Run the app

```bash
python app/main.py
```

---

## ⚠️ Requirements

* Python 3.10 / 3.11
* FFmpeg installed and added to PATH

---

## 📌 Note

This is a **base-level project** showing how **Speech-to-Text can be used as the foundation** for building AI-powered meeting assistants.

---
