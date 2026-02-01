from ytmusicapi import YTMusic
import webbrowser
import time
import pyautogui as gu

ytmusic = YTMusic()


def play_song(song_name: str):
    """
    Search and play song directly on YouTube
    """
    try:
        results = ytmusic.search(song_name, filter="songs")

        if not results:
            return False

        video_id = results[0]["videoId"]
        url = f"https://www.youtube.com/watch?v={video_id}&autoplay=1"

        webbrowser.open(url)
        return True

    except Exception as e:
        print("Music error:", e)
        return False


def pause_resume():
    """
    Pause or resume using keyboard (space)
    """
    time.sleep(0.5)
    gu.press("space")
