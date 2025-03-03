import os
import time
import threading
from gtts import gTTS
from playsound import playsound

def speak_text_gtts(text):
    temp_filename = "temp_response.mp3"

    # Ensure old file is deleted before creating a new one
    if os.path.exists(temp_filename):
        try:
            os.remove(temp_filename)
        except PermissionError:
            print("❌ File in use. Retrying...")
            time.sleep(1)
            os.remove(temp_filename)

    # Function to generate speech
    def generate_speech():
        tts = gTTS(text=text, lang="hi")
        tts.save(temp_filename)  # Save with a temporary name

    # Start speech generation in a separate thread
    speech_thread = threading.Thread(target=generate_speech)
    speech_thread.start()
    speech_thread.join()  # Wait until speech is generated

    # Play the file and wait until playback is finished
    print(f"🔊 AI Speaking: {text}")
    playsound(temp_filename)

    # Delay before deleting to prevent permission errors
    time.sleep(1)
    if os.path.exists(temp_filename):
        os.remove(temp_filename)  # Safely delete the temp file
