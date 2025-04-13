import streamlit as st
import google.generativeai as genai

# Gemini API Key
api_key = "AIzaSyBW9hcMr_y0ddhJ3bTvF8ukN7CPOVTc0UU"
genai.configure(api_key=api_key)

# Model setup
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def GenerateResponse(input_text):
    try:
        response = model.generate_content([
            "You are a helpful and creative educational chatbot. Be friendly and positive in tone.",
            f"User: {input_text}",
        ])
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🎨 Creative Educational Chatbot")

user_input = st.text_input("Enter your message:")

if st.button("✨ Send"):
    if user_input.strip() != "":
        response = GenerateResponse(user_input)
        st.markdown(f"**🧑 You:** {user_input}")
        st.markdown(f"**🤖 Bot:** {response}")



