import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# Gemini API Key (secure it in production)
api_key = "AIzaSyBW9hcMr_y0ddhJ3bTvF8ukN7CPOVTc0UU"
genai.configure(api_key=api_key)

# Model setup
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
            "You are a helpful and creative educational chatbot. Be friendly and positive in tone.",
            f"User: {input_text}",
        ])
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# --- GUI Functions ---
def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return
    chat_log.insert(tk.END, f"🧑 You: {user_input}\n", "user")
    entry.delete(0, tk.END)

    response = GenerateResponse(user_input)
    chat_log.insert(tk.END, f"🤖 Bot: {response}\n\n", "bot")
    chat_log.see(tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("🎨 Creative Educational Chatbot - Gemini 1.5")
root.geometry("700x540")
root.configure(bg="#fdf6f0")

# Chat log
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Comic Sans MS", 12), bg="#fffaf2", fg="#333")
chat_log.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
chat_log.tag_config("user", foreground="#1f78d1", font=("Comic Sans MS", 12, "bold"))
chat_log.tag_config("bot", foreground="#2ca245", font=("Comic Sans MS", 12, "italic"))

# Input + Send button frame
frame = tk.Frame(root, bg="#fdf6f0")
frame.pack(pady=10)

entry = tk.Entry(frame, width=60, font=("Segoe UI", 12), bg="#ffffff", fg="#000000",
                 relief=tk.FLAT, highlightthickness=1, highlightbackground="#1f78d1")
entry.pack(side=tk.LEFT, padx=5, ipady=6)
entry.bind("<Return>", lambda event: send_message())

send_btn = tk.Button(frame, text="✨ Send", command=send_message,
                     font=("Segoe UI Semibold", 11),
                     bg="#6c63ff", fg="white",
                     activebackground="#5548e0",
                     relief=tk.FLAT, padx=12, pady=6)
send_btn.pack(side=tk.LEFT)

# Exit button
exit_btn = tk.Button(root, text="❌ Exit", command=root.quit,
                     font=("Segoe UI", 11), bg="#ff6b6b", fg="white",
                     relief=tk.FLAT, padx=10, pady=5)
exit_btn.pack(pady=5)

root.mainloop()


