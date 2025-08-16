from groq import Groq
import os

API_KEY = os.getenv('API_KEY')

client = Groq(api_key=API_KEY)

conversation_history = []


def groq(prompt):

    if not conversation_history:
        conversation_history.append({"role": "system", "content": "Responda qualquer pergunta em termos de League of Legends"})

    conversation_history.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=conversation_history,
        temperature=0.6,
        max_tokens=500
    )

    conversation_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return chat_completion.choices[0].message.content
