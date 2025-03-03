### **📌 AI Cold Calling Assistant**
An AI-powered cold-calling assistant that handles **demo scheduling, interview screening, and payment follow-ups** using **speech-to-text (STT), text-to-speech (TTS), and AI conversation handling**.  

---

## **🔹 Features**
✅ **Voice AI** – Converts speech to text & responds naturally  
✅ **Scenario-Based Conversations** – Predefined flows for **demo, interview, and payment**  
✅ **Interruptions & Out-of-Context Handling** – AI smoothly adapts  
✅ **Logging** – Saves conversations for review  
✅ **JSON-Based Dialogues** – Easy-to-edit structured conversations  

---

## **🔹 Project Structure**
```
AI_Cold_Calling/
├── src/                      # Main AI logic
│   ├── stt.py                 # Speech-to-text (Google STT)
│   ├── tts.py                 # Text-to-speech (gTTS)
│   ├── ai_agent.py            # AI response generation
│   ├── voice_ai.py            # Manages voice interaction
│   ├── conversation_handler.py # Handles predefined conversation flows
│   ├── logs/                   # Stores conversation logs
│   ├── data/                   # JSON files for structured dialogues
│       ├── demo.json
│       ├── interview.json
│       ├── payment.json
│   ├── .env                   # API keys (DO NOT SHARE)
│   ├── requirements.txt        # Dependencies
│
├── backend/                   # Flask API (Paused for now)
├── frontend/                   # Web UI (Paused for now)
└── README.md                  # Documentation
```

---

## **🔹 Setup & Installation**
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Set Up API Keys**
- Create a `.env` file in `src/`
- Add your Google Gemini API key:
  ```
  GEMINI_API_KEY=your-api-key-here
  ```

### **3️⃣ Run the AI Voice Assistant**
```bash
cd src
python voice_ai.py
```
- **Enter a scenario:** `demo`, `interview`, or `payment`
- **Speak when prompted**
- **AI will respond based on the selected scenario**

---

## **🔹 How It Works**
1️⃣ **STT (Speech-to-Text)** → Recognizes user input  
2️⃣ **AI Response Generation** → Uses Gemini API & JSON templates  
3️⃣ **TTS (Text-to-Speech)** → Speaks AI response back  
4️⃣ **Logging** → Saves conversations for review  

---

## **🔹 Next Steps**
- **Refine AI conversation handling** ✅ *(Completed)*
- **Logging AI conversations** ✅ *(Completed)*
- **Web UI & Backend Integration** ⏸ *(Paused for now)*  

---

## **📌 Credits**
🚀 Built with Python, Google Gemini API, Flask, and TailwindCSS  

---
**More Info**
https://drive.google.com/drive/folders/10jUiEqGy058t3b44D7IIfGsgVYltRO9y?usp=drive_link

This README gives a **quick and detailed overview** of your project. For any query mail on manishiitr9@gmail.com 🔥
