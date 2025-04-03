import google.generativeai as genai
# Step 1: Configure API Key (Replace with your actual API key)
genai.configure(api_key="AIzaSyCGGuCvdXyRsE4YCjtSuEd9uDFDH7Nqqz0")
# Step 2: Set Up AI Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Fastest model
    generation_config={
        "temperature": 0.7,         # Controls randomness (Higher = More Creative)
        "top_p": 0.9,               # Nucleus Sampling (Controls diversity of response)
        "max_output_tokens": 300     # Limits response length
    }
)
# Step 3: Create Chat Function
def chat_with_ai():
    print("🤖 Chatbot: Hello! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")  # Take input from user
        
        if user_input.lower() == "exit":
            print("🤖 Chatbot: Goodbye!")
            break
        
        response = model.generate_content(user_input)  # Get AI response
        print("🤖 Chatbot:", response.text)  # Print response
# Step 4: Run the Chatbot
chat_with_ai()
