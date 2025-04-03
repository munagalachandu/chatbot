# chatbot
This is for explanation of chatbot, and quick integration for ur projects.
1. we install using pip install google-generativeai
2. get api key from https://aistudio.google.com/prompts/new_chat
    replace this actual key in api_key from actual code.
3. You can fine tune ur ai model using these props
   temperature : creative(1.0-less accurate), focused(0.2- less diverse), balamced(0.4-0.7)
   top_p(nucleus sampling) : high diversity words(1.0), more focused(0.5)
   max_output_tokens: long response(500), short & precise(50)
   top_k: diverse(40), accurate(5)

   Use Case	Best Settings
Coding assistant	temperature=0.2, top_p=0.8, top_k=10, max_output_tokens=300
Factual Q&A	temperature=0.1, top_p=0.9, top_k=5, max_output_tokens=200
Casual Chatbot	temperature=0.7, top_p=0.9, top_k=40, max_output_tokens=150
Story Writing	temperature=1.0, top_p=1.0, top_k=50, max_output_tokens=500
4. Gemini Models & Best Use Cases (with Example)  
   1. Gemini 1.5 Pro – Best for complex reasoning, coding, and long-context understanding. 
   Example: An AI assistant that summarizes long research papers.  
   2. Gemini 1.5 Flash – Optimized for speed, ideal for chatbots and real-time applications. 
   Example: A customer support chatbot responding instantly.  
   3. Gemini 2.0 Flash – Faster than 1.5 Flash, supports multimodal inputs (text, images, 
   audio). Example: A chatbot that processes images and provides instant feedback.  
   4. Gemini 2.5 Pro (Experimental) – Most advanced, excels in coding, reasoning, and largescale 
   AI tasks. Example: An AI that debugs and optimizes entire codebases automatically.  
FOR HACKATHONS ( Gemini 1.5 Flash, Gemini 2.0 Flash)
For speed → Flash models (e.g., quick chatbot).  
For deep understanding → Pro models (e.g., research summarization).

5. Different Types of Prompting  

1. Zero-Shot Prompting – No examples given, the model generates a response based on its training. Example: "Explain machine learning."  
2. One-Shot Prompting – One example is given to guide the model’s response. Example: "A cat is a small, furry animal. Now, describe a dog."  
3. Few-Shot Prompting – Multiple examples are given to set the response pattern. Example: "A cat is a small, furry pet. A parrot is a colorful bird. Now, describe a dolphin."  
4. Chain-of-Thought (CoT) Prompting – The model is guided to reason step-by-step. Example: "Solve: 23 × 7. First, multiply 20 × 7, then 3 × 7, and add both results."  
5. Instruction-Based Prompting – Clear instructions improve output quality. Example: "Summarize this paragraph in 3 bullet points."  
6. Role-Based Prompting – Assigning the model a role for better responses. Example: "You are a history professor. Explain World War II in simple terms."  
For hackathons, Few-Shot and Chain-of-Thought Prompting work best for accuracy and reasoning.

   FOR HISTORY SAVING :
   import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Configure API Key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Dictionary to store chat history
chat_history = {}

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests and stores history."""
    try:
        data = request.json
        user_id = data.get("user_id", "default_user")  # Unique user ID
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        # Initialize history if user is new
        if user_id not in chat_history:
            chat_history[user_id] = []
        # Add user message to history
        chat_history[user_id].append({"role": "user", "message": user_message})
        # Generate AI response
        response = model.generate_content(user_message)
        bot_response = response.text.strip()
        # Add bot response to history
        chat_history[user_id].append({"role": "bot", "message": bot_response})
        return jsonify({"response": bot_response, "history": chat_history[user_id]})
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

