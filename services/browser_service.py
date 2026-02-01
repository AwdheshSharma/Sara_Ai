import webbrowser


def open_url(url: str):
    if not url:
        return

    try:
        webbrowser.open(url)
    except Exception as e:
        print("Browser error:", e)
