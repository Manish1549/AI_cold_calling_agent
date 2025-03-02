from transformers import AutoModelForSequenceClassification, AutoTokenizer
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

        print(f"🔹 Raw logits: {logits.tolist()}")  # ✅ Debugging logits
        predicted_label = torch.argmax(logits, dim=1).item()
        
        return self.label_map[predicted_label]

# ✅ Test the Model Predictions
if __name__ == "__main__":
    muril = MuRILWrapper()

    test_sentences = [
        "Mujhe demo book karna hai.",
        "Mera interview kab hai?",
        "Mujhe payment reminder dena hai.",
        "Kya aapke ERP system ka demo available hai?",
        "Interview ke timings kya hain?",
        "Kya aapka software cloud-based hai?",
        "Payment ka status update de sakte hain?"
    ]

    for sentence in test_sentences:
        prediction = muril.predict_category(sentence)
        print(f"📝 Input: {sentence} → 🔹 Predicted: {prediction}")
