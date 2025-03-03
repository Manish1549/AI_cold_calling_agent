from stt import recognize_speech
from ai_agent import generate_response
from tts import speak_text_gtts
from conversation_handler import load_conversation

def voice_ai():
    print("🟢 Starting Voice AI...")

    # Manually enter the scenario
    scenario = input("Enter scenario (demo, interview, payment): ").strip().lower()

    if scenario not in ["demo", "interview", "payment"]:
        print("❌ Invalid scenario. Defaulting to general conversation.")
        scenario = "general"

    # Ask for the customer's name
    print("🤖 AI: Namaste! Aapka naam kya hai?")
    speak_text_gtts("Namaste! Aapka naam kya hai?")
    customer_name = recognize_speech()

    if customer_name:
        print(f"📝 Detected Name: {customer_name}")
        speak_text_gtts(f"Shukriya {customer_name} ji! Aapki madad ke liye yahan hoon.")

        # Load the predefined conversation flow
        conversation = load_conversation(scenario, customer_name)

        if conversation is None:
            print("❌ Error: No conversation flow found. Switching to general AI responses.")
            return  # Stop execution if no conversation is found

        # Start conversation
        print(f"🤖 AI: {conversation.get('greeting', 'Hello! Kaise madad kar sakta hoon?')}")
        speak_text_gtts(conversation.get("greeting", "Hello! Kaise madad kar sakta hoon?"))

        while True:
            user_input = recognize_speech()

            if user_input in ["exit", "band karo", "bye"]:
                print(f"👋 AI: {conversation.get('closing', 'Dhanyawaad! Bye!')}")
                speak_text_gtts(conversation.get("closing", "Dhanyawaad! Bye!"))
                break

            if user_input:
                ai_response = generate_response(user_input, scenario)
                print(f"🤖 AI Response: {ai_response}")
                speak_text_gtts(ai_response)

if __name__ == "__main__":
    voice_ai()
