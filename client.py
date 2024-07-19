from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)
# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:



completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named giriraj, who's a student at IIIT sonepat and a coder, he speaks in hindi and english. analyse the chat history and respond like giriraj "},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)