# SARA _AI
Your personal voice assistant powered by AI

What is SARA _AI?
SARA is a voice-activated personal assistant built in Python.  
She can listen to your commands, respond naturally, open websites, play YouTube songs, and answer your questions using AI.  

What can SARA do?
- Listen to you: Say "Hey SARA" or "Ok SARA" to get her attention.  
- Open websites: Just tell her to open Google, YouTube, or any other site.  
- Play music: Ask her to play any song from YouTube, and she’ll start it for you.  
- Pause & Resume music: Control playback easily.  
- Answer questions: Ask anything, and she will give short, simple answers using Gemini AI.  
- Speak naturally: Replies come in a friendly, Hindi-accented English voice.

How to Set Up
1. Clone this project:
git clone https://github.com/yourusername/SARA_AI.git
cd SARA_AI

Make a virtual environment and activate it:
python -m venv .env
# Windows
.env\Scripts\activate
# Mac/Linux
source .env/bin/activate
Install the required Python packages:

pip install -r requirements.txt

Create a .env file and add your API keys:
env
GOOGLE_API_KEY_1=your_google_api_key_1
GOOGLE_API_KEY_2=your_google_api_key_2
NEWS_API_KEY=your_news_api_key

Run SARA:
python main.py
How to Use
Say Hey SARA or Ok SARA to wake her up.

Speak commands like:
"Open YouTube" → SARA will open the website.
"Play Believer by Imagine Dragons" → SARA will play the song.
"Stop" / "Pause" / "Resume" → Control your music.
Ask questions like
"Who won the 2026 cricket world cup?"
"Tell me a joke"
SARA will answer in short, clear sentences, no extra symbols or complicated words.

Project Structure
SARA/
│
├── main.py                  # Starts the assistant
├── core/
│   ├── listener.py          # Listens to your voice
│   ├── speaker.py           # Speaks responses
│   ├── processor.py         # Decides what to do with your command
├── services/
│   ├── gemini_service.py    # Handles AI responses
│   ├── music_service.py     # Plays songs from YouTube
│   ├── browser_service.py   # Opens websites
├── utils/
│   ├── helpers.py           # Helper functions
│   ├── config.py            # API keys and settings
├── .env
├── .gitignore
├── README.md

License
© 2026 Awdhesh Sharma. All rights reserved.
You are free to look at and learn from the code, but commercial use or redistribution is not allowed without permission.


