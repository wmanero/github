import os
from langchain_groq import ChatGroq

api_key = "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"
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [('user', 'Traduza {expressao} para a lingua {lingua}')]
)

chain = template | chat

resposta = chain.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})

print(resposta.content)