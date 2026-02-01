from google import genai
from utils.helpers import extract_dict
from utils.config import GOOGLE_API_KEY_1, GOOGLE_API_KEY_2

client_1 = genai.Client(api_key=GOOGLE_API_KEY_1)
client_2 = genai.Client(api_key=GOOGLE_API_KEY_2)


def ask_gemini_for_url(command: str):
    """
    Asks Gemini to return ONLY a Python dict with a URL
    """
    try:
        response = client_1.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
            You are a backend API.

            Return ONLY a valid Python dictionary.
            No explanation. No extra text.

            Rules:
            - Key must be: url
            - Value must be a valid website URL or null

            Examples:
            open youtube -> {{ "url": "https://www.youtube.com" }}
            open google -> {{ "url": "https://www.google.com" }}
            hello -> {{ "url": null }}

            User input: {command}
            """
            )

        text = response.text.strip()
        data = extract_dict(text)

        if isinstance(data, dict):
            return data.get("url")

    except Exception as e:
        print("Gemini URL error:", e)

    return None


def ask_gemini_chat(command: str) -> str:
    """
    Normal Gemini fallback chat (short + clean)
    """
    try:
        response = client_2.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
            Reply in 1 or 2 short sentences only.
            Do not use symbols, markdown, bullets, or asterisks.
            Use simple hindi but English words only.

            Question: {command}
            """
            )
        return response.text.strip()

    except Exception as e:
        print("Gemini chat error:", e)
        return "Sorry, I am having trouble right now"
