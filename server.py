from flask import Flask, request, jsonify
from flask_cors import CORS
from voice_ai import voice_ai  # Import AI cold-calling function

app = Flask(__name__)
CORS(app)  # Enable frontend to talk to backend

@app.route("/start_ai_call", methods=["POST"])
def start_ai_call():
    data = request.json
    scenario = data.get("scenario", "general")

    # Call AI function and return its first response
    response = voice_ai(scenario)
    
    return jsonify({
        "ai_message": response,
        "user_message": "User's response will appear here..."
    })

if __name__ == "__main__":
    app.run(debug=True)
