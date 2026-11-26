from langchain.agents import create_agent
from langgraph.checkpoint import InMemorySaver
from .llm import get_llm
from .prompt import SYSTEM_PROMPT
from .tools import TOOLS

class AI_Agent():
    def __init__(self):
        self.llm = get_llm()
        self.memory = InMemorySaver()
        self.agent = create_agent(model=self.llm, tools=TOOLS, checkpointer=self.memory, system_prompt=SYSTEM_PROMPT)

    def chat(self, message: str, user_id: str) -> str:
        config = {
            'configurable': {'thread_id': str(user_id)},
            'recursion_limit': 20
        }

        result = self.agent.invoke({
            'messages': {
                'role': 'user',
                'content': message
            }
        }, config=config
        )

        return result['messages'][-1].text
