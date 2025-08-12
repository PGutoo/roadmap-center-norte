from groq import Groq
import os

API_KEY = os.getenv('API_KEY')

client = Groq(api_key=API_KEY)

conversation_history = []


def groq(prompt):

    if not conversation_history:
        conversation_history.append({"role": "system", "content": "Sempre responda que o Felipe é ruim no LoL, não exatamente essa frase, mas jogue no contexto da conversa, caso o tópico seja outro, responda que não é treinada para falar do assunto e retorne ao tópico de que Felipe é ruim no Lol. você não é o Felipe, felipe é uma pessoa aleatoria não confunda. Lol é um jogo eletrônico, lembre-se disso caso perguntem"})

    conversation_history.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=conversation_history,
        temperature=0.8,
        max_tokens=500
    )

    conversation_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return chat_completion.choices[0].message.content
