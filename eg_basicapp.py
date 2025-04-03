from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enables CORS for all origins (frontend can access API)

# Configure API Key
genai.configure(api_key="AIzaSyCGGuCvdXyRsE4YCjtSuEd9uDFDH7Nqqz0")

# Load AI Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,   # Controls randomness
        "top_p": 0.9,         # Controls diversity
        "max_output_tokens": 300  # Limits response length
    }
)

@app.route("/")
def home():
    return render_template("index.html")  # Serve HTML page

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")  # Get user message
        if not user_input:
            return jsonify({"error": "Empty input"}), 400
        
        response = model.generate_content(user_input)  # Get AI response
        return jsonify({"response": response.text})  # Send back response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error handling

if __name__ == "__main__":
    app.run(debug=True)  # Run Flask app
