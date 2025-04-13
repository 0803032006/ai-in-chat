
import os
import google.generativeai as genai

# Configure API Key securely
api_key = ("AIzaSyBW9hcMr_y0ddhJ3bTvF8ukN7CPOVTc0UU")
if not api_key:
    raise ValueError("API Key not found. Set it as an environment variable.")

genai.configure(api_key=api_key)

# Model Configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

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

while True:
    user_input = input("Enter your prompt : ").strip()
    if user_input.lower() == "exit":
        break
    print("Bot:", GenerateResponse(user_input))
