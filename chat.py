import os
import openai # pip install openai

openai.api_key = ""
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hi ChatGPT. Say hi back!"}
    ]
)
answer = response.choices[0].message.content
print(answer)
