import openai
from config import api_key
client = openai.OpenAI(api_key=api_key)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # <-- use gpt-3.5-turbo
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)
