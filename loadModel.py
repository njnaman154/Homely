from openai import OpenAI
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
api_key = os.getenv("apiKey")
grokapi=os.getenv("grokapi")

def load_client():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    return client

def grok_client():
    client = Groq(api_key=os.getenv("grokapi"))
    return client

def get_response(client, prompt, model):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content