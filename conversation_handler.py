import json
import os

def load_conversation(scenario, customer_name=""):
    """Loads a predefined conversation template from a JSON file."""
    file_path = os.path.join(os.path.dirname(__file__), f"../data/{scenario}.json")

    if not os.path.exists(file_path):
        print(f"❌ Error: Conversation flow for {scenario} not found at {file_path}")
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        conversation = json.load(file)

    # Replace placeholders with customer name
    for key in conversation:
        conversation[key] = conversation[key].replace("{name}", customer_name)

    return conversation
