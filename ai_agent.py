import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
from datetime import datetime

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

conversation_history = []

def load_conversation_template(scenario):
    """Loads the predefined conversation template from a JSON file."""
    file_path = os.path.join(os.path.dirname(__file__), f"../data/{scenario}.json")

    if not os.path.exists(file_path):
        print(f"❌ Error: Conversation template for {scenario} not found.")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def detect_interruption(user_input):
    """Detects if the user is changing the topic or saying something unrelated."""
    interruption_keywords = ["price", "features", "discount", "change", "naya topic"]
    off_topic_keywords = ["weather", "family", "news", "sports", "politics"]

    if any(word in user_input.lower() for word in interruption_keywords):
        return "interruption"
    elif any(word in user_input.lower() for word in off_topic_keywords):
        return "off-topic"
    return None

def log_conversation(user_input, ai_response, scenario, customer_name):
    """Logs the conversation to a file."""
    log_dir = os.path.join(os.path.dirname(__file__), "../logs")
    os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists

    log_file = os.path.join(log_dir, "conversations.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"\n[{timestamp}] Scenario: {scenario}, Customer: {customer_name}\n")
        file.write(f"User: {user_input}\n")
        file.write(f"AI: {ai_response}\n")
        file.write("-" * 50 + "\n")

def generate_response(user_input, scenario="general", customer_name=""):
    global conversation_history
    conversation_history = conversation_history[-3:]  # Keep recent context

    # Load structured conversation template
    conversation_template = load_conversation_template(scenario)

    if not conversation_template:
        prompt = "You are an AI handling conversations. Respond naturally."
    else:
        prompt = f"{conversation_template['greeting']}\n"
        prompt += f"{conversation_template['question']}\n"
        prompt += f"{conversation_template['follow_up']}\n"
        prompt += f"{conversation_template['closing']}\n"

    # Detect if user changed the topic or went off-topic
    topic_status = detect_interruption(user_input)

    if topic_status == "interruption":
        prompt += "\nUser has changed the topic. Acknowledge their question and then smoothly return to the original topic."
    elif topic_status == "off-topic":
        prompt += "\nUser has mentioned an unrelated topic. Respond briefly and guide them back to the main conversation."

    # Add conversation history
    for entry in conversation_history:
        prompt += f"\n{entry['role']}: {entry['content']}"

    prompt += f"\nUser: {user_input}\nAssistant:"

    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    response = model.generate_content(
        prompt, 
        generation_config={"temperature": 0.7, "max_output_tokens": 100}
    ).text

    # Save conversation to log
    log_conversation(user_input, response, scenario, customer_name)

    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": response})

    return response
