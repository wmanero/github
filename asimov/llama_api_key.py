import os

api_key = "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"

os.environ['GROQ_API_KEY'] = api_key

from langchain_groq import ChatGroq

chat = ChatGroq(model='llama-3.3-70b-versatile')

pergunta = chat.invoke('Olá! com quem estou falando?')

print(pergunta.content)


