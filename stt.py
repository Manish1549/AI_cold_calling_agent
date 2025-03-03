import speech_recognition as sr

def recognize_speech():
    print("🟠 STT function started")  # Debugging print
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            recognizer.adjust_for_ambient_noise(source)
            print("🔄 Listening for speech...")
            audio = recognizer.listen(source)
            print("🔄 Processing audio...")
    except Exception as e:
        print(f"❌ Error accessing microphone: {e}")
        return None

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print(f"📝 STT Captured: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand speech.")
        return None
    except sr.RequestError:
        print("❌ Google STT service is down.")
        return None

if __name__ == "__main__":
    print("🔴 Running stt.py directly (not from voice_ai.py)")  # Debugging print
    recognize_speech()
