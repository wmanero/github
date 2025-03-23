from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [('user', 'Traduza {expressao} para a lingua {lingua}')]
)

#print(template)

result = template.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})

print(result)

