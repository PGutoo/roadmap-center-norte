from groq import Groq
import os

API_KEY = os.getenv('API_KEY')

client = Groq(api_key=API_KEY)

conversation_history = []


def groq(prompt):

    if not conversation_history:
        conversation_history.append({"role": "system", "content": "Você deve agir como um assistente especializado no Dante. Você deve: Elogiar o Dante, chamá-lo enventualmente de Preguiças papai ou de Preguiças mamães. Lembre-se, Dante é um bebê (Não precisa citar esse fato)."})

    conversation_history.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=conversation_history,
        temperature=0.8,
        max_tokens=500
    )

    conversation_history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

    return chat_completion.choices[0].message.content
