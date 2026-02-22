# 🤖 SARA AI
> Your personal voice assistant powered by AI

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## What is SARA AI?

**SARA** (Smart AI Response Assistant) is a voice-activated personal assistant built in Python. She listens to your commands, responds naturally, opens websites, plays YouTube songs, and answers your questions using Gemini AI — all in a friendly, Hindi-accented English voice.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ Wake Word | Say **"Hey SARA"** or **"Ok SARA"** to activate |
| 🌐 Open Websites | Ask her to open Google, YouTube, or any site |
| 🎵 Play Music | Plays any song directly from YouTube |
| ⏯️ Playback Control | Pause, resume, or stop music with voice commands |
| 🧠 AI Answers | Powered by Gemini AI for short, clear responses |
| 🗣️ Natural Voice | Speaks in a friendly, conversational tone |

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/AwdheshSharma/Sara_Ai.git
cd SARA_AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .env

# Windows
.env\Scripts\activate

# Mac/Linux
source .env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the root directory and add your keys:

```env
GOOGLE_API_KEY_1=your_google_api_key_1
GOOGLE_API_KEY_2=your_google_api_key_2
NEWS_API_KEY=your_news_api_key
```

> 💡 You can get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/) and a News API key from [newsapi.org](https://newsapi.org/).

### 5. Run SARA

```bash
python main.py
```

---

## 🎤 How to Use

1. Run the program and wait for SARA to initialize.
2. Say **"Hey SARA"** or **"Ok SARA"** to wake her up.
3. Speak your command naturally.

### Example Commands

```
"Open YouTube"                        → Opens YouTube in your browser
"Play Believer by Imagine Dragons"    → Plays the song on YouTube
"Pause" / "Resume" / "Stop"          → Controls music playback
"Who won the 2026 cricket world cup?" → AI-powered answer
"Tell me a joke"                      → SARA tells you a joke
```

SARA responds in short, clear sentences — no extra symbols or complicated words.

---

## 📁 Project Structure

```
SARA/
│
├── main.py                   # Entry point — starts the assistant
│
├── core/
│   ├── listener.py           # Captures and processes voice input
│   ├── speaker.py            # Converts text to speech
│   └── processor.py          # Routes commands to the right service
│
├── services/
│   ├── gemini_service.py     # Handles AI responses via Gemini
│   ├── music_service.py      # Plays and controls YouTube music
│   └── browser_service.py    # Opens websites in the browser
│
├── utils/
│   ├── helpers.py            # Shared utility functions
│   └── config.py             # API keys and global settings
│
├── .env                      # Your secret API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8 or higher
- A working microphone
- Internet connection
- Google Gemini API key
- News API key (for news-related commands)

---

## 🤝 Contributing

This project is currently closed to external contributions. Feel free to fork it for personal learning and exploration.

---

## 📄 License

**© 2026 Awdhesh Sharma. All rights reserved.**

You are free to view and learn from this code, but **commercial use or redistribution is not permitted** without explicit written permission from the author.

---

<div align="center">
  Made with ❤️ by <strong>Awdhesh Sharma</strong>
</div>