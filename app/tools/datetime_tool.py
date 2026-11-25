from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_core.tools import tool

@tool
def get_current_time() -> str:
    """Get the current date and time in Iran."""
    now = datetime.now(ZoneInfo("Asia/Tehran"))
    return now.strftime("%Y-%m-%d %H:%M:%S")
