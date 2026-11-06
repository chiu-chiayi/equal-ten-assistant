from .time_tool import get_current_time
from .calendar_tool import create_calendar_event
# 未來有新工具，只需在此加一行 import 即可：
# from .weather_tool import get_weather

# 將所有要給 Gemini 使用的工具集中起來
ALL_TOOLS = [
    get_current_time,
    create_calendar_event,
    # get_weather,
]