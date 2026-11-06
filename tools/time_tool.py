import datetime

def get_current_time() -> str:
    """取得當前的系統日期與時間。"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"目前的系統時間為：{now}"