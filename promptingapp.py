import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Configure Gemini AI API Key (Replace with your actual API key)
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Define structured prompting for better responses
PROMPT_TEMPLATE = """
You are a friendly chatbot that provides clear and helpful responses. Keep your answers short and professional.
User's question:
---
{user_input}
---
"""

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests from the frontend."""
    try:
        data = request.json
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Format the structured prompt
        prompt = PROMPT_TEMPLATE.format(user_input=user_message)

        # Generate AI response
        response = model.generate_content(prompt)
        bot_response = response.text.strip()

        return jsonify({"response": bot_response})
    
    except Exception as e:
        return jsonify({"error": "Something went wrong. Try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
