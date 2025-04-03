import google.generativeai as genai
# Configure API key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
# Initialize model
model = genai.GenerativeModel("gemini-pro")
# Few-shot prompting example for interview preparation
prompt = """
You are an AI interview assistant. Answer technical questions concisely.

Example 1:
Q: What is a linked list?
A: A linked list is a linear data structure where elements are stored in nodes, with each node pointing to the next.

Example 2:
Q: What is recursion?
A: Recursion is a programming technique where a function calls itself to solve smaller instances of a problem.

Now answer this:
Q: What are Python decorators?
"""
# Generate response
response = model.generate_content(prompt)
# Print the AI's response
print(response.text)
