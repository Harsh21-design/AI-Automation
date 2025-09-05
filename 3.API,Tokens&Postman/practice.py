import os
from groq import Groq
# from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

api_key = os.environ["GROQ_API_KEY"]

client = Groq(
    api_key = api_key
)

# send a request
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages = [
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Write a 4 line poem about space."}
    ]
)

print(response.choices[0].message.content)