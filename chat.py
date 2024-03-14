import os
import openai # pip install openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hi ChatGPT. Say hi back!"}
    ]
)
answer = response.choices[0].message.content
print(answer)
