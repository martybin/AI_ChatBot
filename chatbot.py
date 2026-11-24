from langchain_ollama import ChatOllama

llm = ChatOllama(
    model='mimo-v2.6:9b',
    base_url='http://localhost:11434',
    temperature=0.3
)

while True:
    _input = input('Enter your question: ')
    response = llm.invoke(_input)
    answer = response.content.replace('\n', ' ')
    if _input.lower() == 'exit':
        break
    print(f'Answer: {answer}')