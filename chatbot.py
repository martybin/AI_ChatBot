from langchain_ollama import ChatOllama
from langchain_core.messages import (SystemMessage, HumanMessage)

llm = ChatOllama(
    model='mimo-v2.6:9b',
    base_url='http://localhost:11434',
    temperature=0.3
)

messages = [
    SystemMessage(
        content='''
        You are a professional AI assistant in coding and programming.
        You should implement what the user asks you to do in a professional manner.
        '''
        ),
    HumanMessage(
        content=input('What do you like to codeing? ')
        )
]

while True:
    response = llm.invoke(messages)
    answer = response.content.replace('\n', ' ')
    if messages[-1].content.lower() == 'exit':
        break
    print(f'Answer: {answer}')