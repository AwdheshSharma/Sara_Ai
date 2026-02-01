from dotenv import load_dotenv
import os

load_dotenv()

# ===== API KEYS =====
GOOGLE_API_KEY_1 = os.getenv("GOOGLE_API_KEY_1")
GOOGLE_API_KEY_2 = os.getenv("GOOGLE_API_KEY_2")

# ===== ASSISTANT SETTINGS =====
ASSISTANT_NAME = "SARA"
WAKE_WORDS = ["sara", "hey sara", "ok sara", "sarah", "hey sarah", "ok sarah", "sra", "sar"]

# ===== SPEECH RECOGNITION =====
LISTEN_TIMEOUT = 10
PHRASE_TIME_LIMIT = 9
ENERGY_THRESHOLD = 300
PAUSE_THRESHOLD = 0.8
DYNAMIC_ENERGY = True
LANGUAGE = "en-IN"

# ===== TEXT TO SPEECH =====
TTS_VOICE = "en-IN-NeerjaNeural"
TTS_OUTPUT_FILE = "output.mp3"

# ===== BROWSER / MUSIC =====
DEFAULT_BASE_URL = "https://www.youtube.com/watch?v="
