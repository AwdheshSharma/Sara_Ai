from core.listener import Listener
from core.processor import Processor
from core.speaker import speak
from utils.config import ASSISTANT_NAME


def main():
    listener = Listener()
    processor = Processor()

    speak(f"Initializing {ASSISTANT_NAME}")

    while True:
        try:
            print("Listening..... ")
            text = listener.listen()

            if listener.wake_word(text):
                speak("Yes, I am here")

                print("Listening for command...")
                command = listener.listen_command()

                if command:
                    processor.process(command)
                else:
                    speak("I did not hear any command")

        except KeyboardInterrupt:
            speak("Shutting down")
            break

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong")


if __name__ == "__main__":
    main()
