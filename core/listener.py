import speech_recognition as sr
from utils.config import (
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    ENERGY_THRESHOLD,
    PAUSE_THRESHOLD,
    DYNAMIC_ENERGY,
    LANGUAGE,
    WAKE_WORDS
)

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        #tuning
        self.recognizer.energy_threshold = ENERGY_THRESHOLD
        self.recognizer.pause_threshold = PAUSE_THRESHOLD
        self.recognizer.dynamic_energy_threshold = DYNAMIC_ENERGY
        
        # Initial calibration
        try:
            with sr.Microphone() as source:
                print("Calibrating background noise... Please wait.")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Calibration complete.")
        except Exception as e:
            print(f"Error during calibration: {e}")

    def listen(self, source=None, timeout=LISTEN_TIMEOUT, phrase_limit=PHRASE_TIME_LIMIT):
        try:
            if source:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            else:
                with sr.Microphone() as source: 
                    audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            
            text = self.recognizer.recognize_google(audio, language = LANGUAGE)
            print(f"YOU SAID: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected")
            return None
        except sr.UnknownValueError:
            print("Unknown Value: Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Speech API error:", e)
            return None
        
    def wake_word(self, text: str) -> bool:
        if not text:
            return False
        return any(word in text for word in WAKE_WORDS)

    def listen_command(self, source=None):
        return self.listen(source=source, timeout=60, phrase_limit=30)
