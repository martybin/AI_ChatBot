from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.tools import tool

llm = ChatOllama(
    model='mimo-v2.6:9b',
    base_url='http://localhost:11434',
    temperature=0.3
)

@tool
def get_current_time() -> str:
    """Get the current date and time in Tehran."""
    now = datetime.now(ZoneInfo('Asia/Tehran'))
    return now.strftime('%Y-%m-%d %H:%M:%S')

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

agent = create_agent(
    model=llm,
    tools=[get_current_time, multiply],
    system_prompt="""
    تو یک دستیار هوشمند فارسی زبان هستی.
    برای دریافت تاریخ و ساعت فعلی از ابزار زمان استفاده کن.
    برای محاسبه ضرب از ابزار multiply استفاده کن.
    اطلاعات را از خودت اختراع نکن.
    پاسخ نهایی را به زبان فارسی ارائه بده.
    """
)

result = agent.invoke(
    {
        'messages': [
            {
                'role': 'user',
                'content': 'سلام! لطفاً تاریخ و ساعت فعلی را به من بده و سپس حاصل ضرب ۱۲ در ۳ را محاسبه کن.'
            }
        ]
    }
)


print(result['messages'][-1].content.replace('\n', ' '))
