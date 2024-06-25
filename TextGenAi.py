import sys
import google.generativeai as genai
import time
from collections import deque
import json

genai.configure(api_key='PutYourApiKeyHere')

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

history_file = 'D:\programming\Python\chat_history.json'

def load_history():
    try:
        with open(history_file, 'r') as file:
            data = json.load(file)
            return deque(data['prompts'], maxlen = 5), deque(data['responses'], maxlen = 5)
            file.close()
    except FileNotFoundError:
        return deque(maxlen=5), deque(maxlen=5)
    
def save_history(prompt_history, response_history):
    with open(history_file, 'w') as file:
        json.dump({'prompts': list(prompt_history), 'responses': list(response_history)}, file)
        file.close()

prompt_history, response_history = load_history()

def add_to_history(user_prompt, ai_response):
    prompt_history.append(user_prompt)
    response_history.append(ai_response)
    save_history(prompt_history, response_history)

chat_session = model.start_chat(history=[
    {
      "role": "user",
      "parts": [
        "your name is Jynx, developed by me, Imon Chakraborty to be my personal CLI assistant!",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Greetings Imon! I am Jynx, a sophisticated AI assistant developed by you to be your personal CLI assistant. Ask away anything you want to know and I am here to assist you!",
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[0]),
      ],
    },
    {
        "role": "model",
      "parts": [
        str(response_history[0]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[1]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[1]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[2]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[2]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[3]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[3]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[4]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[4]),
      ],
    }])

try:
    prompt = sys.argv[1:]
    prompt = str(prompt)+", in short and point wise if possible"
    response = chat_session.send_message(prompt)

    add_to_history(prompt, response.text)
    prompt_history, response_history = load_history()
    
    for char in response.text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

except Exception:
    print("Enter your prompt after prefix jynx!!!")


