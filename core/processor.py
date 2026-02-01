import pyautogui as gui
import time
import webbrowser
from core.speaker import speak
from services.gemini_service import ask_gemini_for_url, ask_gemini_chat
from services.music_service import play_song, pause_resume
from services.browser_service import open_url
from services.gemini_service import ask_gemini_for_url

class Processor:
    def process(self, command: str):
        if not command:
            return

        command = command.lower()

        # ---------- OPEN WEBSITE ----------
        if command.startswith("open"):
            url = ask_gemini_for_url(command)

            if url:
                speak("Opening website")
                open_url(url)
            else:
                speak("I could not find a website")

        # ---------- PLAY MUSIC ----------
        elif "play" in command.lower():
            song = command.replace("play", "").strip()

            if not song:
                speak("Please tell me the song name")
            else:
                pause_resume()  # stop previous if playing
                speak(f"Playing {song}")
                play_song(song)

        # ---------- PAUSE / RESUME ----------
        elif "pause" in command or "resume" in command or "stop" in command or "continue" in command:
            speak("Okay")
            pause_resume()

        # ---------- FALLBACK (GEMINI CHAT) ----------
        else:
            reply = ask_gemini_chat(command)
            speak(reply)
    

 

def process_command(command: str):

    if "open" in command.lower():
        url = ask_gemini_for_url(command)

        if url:
            speak("Opening website")
            webbrowser.open(url)
        else:
            speak("No website found")

def pause_resume():
    time.sleep(0.3)
    gui.press("space")
