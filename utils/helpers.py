import ast


def extract_dict(text: str) -> dict:
    """
    Safely extract a Python dictionary from Gemini response text.
    Expected format:
    { "url": "https://example.com" } OR { "url": null }
    """

    try:
        data = ast.literal_eval(text)
        if isinstance(data, dict) and "url" in data:
            return data
    except Exception:
        pass

    return {"url": None}
