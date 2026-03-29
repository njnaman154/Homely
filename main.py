from loadModel import load_client, grok_client, get_response
import os

model="llama-3.1-8b-instant"
client = grok_client()

prompt = "aaj din kya hai. Answer in english only"
response = get_response(client, prompt, model)
print(response)

