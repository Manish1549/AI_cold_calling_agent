from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load fine-tuned model
model_path = "final_fine_tuned_muril"  # Update this if the model is in a different directory
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("✅ Fine-tuned MuRIL model loaded successfully!")

# Function to classify text
def classify_text(text):
    inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1).item()
    
    label_map = {0: "scheduling", 1: "interview", 2: "follow-up"}
    return label_map[predicted_label]

# Test with a Hinglish sentence
text = "Mujhe ek demo book karna hai ERP software ka."
prediction = classify_text(text)

print(f"🔹 Predicted Category: {prediction}")
