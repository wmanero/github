import os
from langchain_groq import ChatGroq

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

from langchain.prompts import ChatPromptTemplate

def resposta_bot(mensagens):
    mensagens_modelo = [('system', "Você é um assistente amigável chamado Asimo")]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print('Bem vindo ao Asimobot')

mensagens = []
while True:
    pergunta = input('usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append({'role': 'assistant', 'content': resposta})
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o Asimobot')
print(mensagens)