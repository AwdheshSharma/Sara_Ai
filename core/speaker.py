import asyncio
import os 
import re 
import edge_tts 
from playsound import playsound 
from utils.config import TTS_VOICE, TTS_OUTPUT_FILE

_is_speaking = False

def clean_text(text: str) -> str:
    # Cleans text to avoid asterisks, symbols, markdown issues in TTS
    if not text:
        return ""
    
    # remove markdown asterisks and bullets
    text = re.sub(r"[*_`#>-]+", " ", text)

    # remove extra symbols
    text = re.sub(r"[^\w\s.,!?]", " ", text)

    # normalize spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

async def speak_async(text: str):
    global _is_speaking 

    if _is_speaking:
        return
    
    _is_speaking = True
    text = clean_text(text)

    try:
        tts = edge_tts.Communicate(
            text=text,
            voice=TTS_VOICE
        )

        await tts.save(TTS_OUTPUT_FILE)
        playsound(TTS_OUTPUT_FILE)
    except Exception as e:
        print("TTS Error: ", e)

    finally:
        _is_speaking = False
        if os.path.exists(TTS_OUTPUT_FILE):
            try:
                os.remove(TTS_OUTPUT_FILE)
            except:
                pass

def speak(text: str):
    try:
        asyncio.run(speak_async(text))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(speak_async(text))
