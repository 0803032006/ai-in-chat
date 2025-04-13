import os
pip install streamlit google-generativeai

import google.generativeai as genai

# Set your API key
api_key = "AIzaSyBW9hcMr_y0ddhJ3bTvF8ukN7CPOVTc0UU"

if not api_key:
    raise ValueError("API Key not found. Set it as an environment variable or in the code.")

# Configure the API key
genai.configure(api_key=api_key)

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Response generation function
def GenerateResponse(input_text):
    try:
        response = model.generate_content([
            "You are an education chatbot, so reply accordingly.",
            f"Input: {input_text}",
            "Output:",
        ])
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Chat loop
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = GenerateResponse(user_input)
        print("Chatbot:", response)

