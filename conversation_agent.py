from transformers import AutoModelForSequenceClassification, AutoTokenizer
from langchain.memory import ConversationBufferMemory
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.prompts import PromptTemplate
import torch

class MuRILWrapper:
    def __init__(self, model_path="final_fine_tuned_muril"):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.label_map = {0: "scheduling", 1: "interview", 2: "follow-up"}

    def predict_category(self, text: str):
        text = str(text)  # ✅ Ensure input is always a string
        inputs = self.tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_label = torch.argmax(logits, dim=1).item()
        
        return self.label_map[predicted_label]

# ✅ Define conversation memory (fixes the warning)
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# ✅ Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["history", "user_input"],
    template="""
    This is a Hinglish AI conversation agent.
    Maintain context and assist in cold calling tasks.
    Keep responses short and professional.

    Conversation history:
    {history}

    User: {user_input}
    AI Response:"""
)

# ✅ Define LangChain conversation logic
class MuRILChatBot:
    def __init__(self):
        self.model = MuRILWrapper()
        self.chain = (
            RunnablePassthrough.assign(
                history=lambda _: {"history": memory.load_memory_variables({}).get("history", "")},  
                user_input=lambda x: {"user_input": str(x) if isinstance(x, str) else x}  # ✅ Always wrap in dict
            )
            | prompt_template
            | RunnableLambda(lambda x: self.model.predict_category(x))  # ✅ Directly pass the text
        )

    def chat(self, user_input):
        if not isinstance(user_input, dict):
            user_input = {"user_input": str(user_input)}  # ✅ Ensure correct input format
        return self.chain.invoke(user_input)  # ✅ Always pass a dictionary

# ✅ Run the chatbot
if __name__ == "__main__":
    chatbot = MuRILChatBot()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        response = chatbot.chat(user_input)
        print(f"Bot: {response}")