import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_document(message, history, document_text_state):
    history = history or []
    history.append({"role": "user", "content": message})

    context = f"Document: {document_text_state}\n\nUser: {message}"

    response = openai.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "system", "content": context}] + history
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return history, history
