import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# 使用此工具前，請先執行 get_token.py 以生成 token.json、並確保 credentials.json 已放置於專案根目錄。
# # 於終端機中執行以下指令測試：
# python -c "from tools.calendar_tool import create_calendar_event; print(create_calendar_event('測試行程', '2026-11-10T14:00:00', '2026-11-10T15:00:00', color_id='9'))"


SCOPES = ['https://www.googleapis.com/auth/calendar']

def _get_calendar_service():
    """內部輔助函式：讀取 token.json 並建立 API 服務"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # 若 Token 已過期但有 refresh_token，自動在背景刷新
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    if not creds or not creds.valid:
        raise RuntimeError("❌ 無法載入有效的 token.json，請先執行 get_token.py 重新授權")

    return build('calendar', 'v3', credentials=creds)


def create_calendar_event(
    summary: str,
    start_time: str,
    end_time: str,
    color_id: str = None,
    is_all_day: bool = False
) -> str:
    """
    在 Google Calendar 建立新行程。

    Args:
        summary: 行程標題/內容
        start_time: 開始時間，格式為 'YYYY-MM-DDTHH:mm:ss' 或全天行程的 'YYYY-MM-DD'
        end_time: 結束時間，格式同上
        color_id: 行事曆顏色 ID。規則如下：
                  - "9": 朋友聚餐/聚會 (Blueberry)
                  - "10": 旅遊/出遊 (Basil)
                  - "5": 醫療/看診/回診 (Banana)
                  - "3": 運動/藝文活動 (Grape)
                  - "1": 家庭聚餐/聚會 (Lavender)
                  - None: 其他一般事項
        is_all_day: 是否為全天行程
    """
    try:
        service = _get_calendar_service()

        if is_all_day:
            event_body = {
                'summary': summary,
                'start': {'date': start_time},
                'end': {'date': end_time},
            }
        else:
            event_body = {
                'summary': summary,
                'start': {'dateTime': f"{start_time}+08:00", 'timeZone': 'Asia/Taipei'},
                'end': {'dateTime': f"{end_time}+08:00", 'timeZone': 'Asia/Taipei'},
            }

        if color_id:
            event_body['colorId'] = str(color_id)

        event = service.events().insert(calendarId='primary', body=event_body).execute()
        return f"SUCCESS: 行程已成功寫入 Google Calendar (Event ID: {event.get('id')})"

    except Exception as e:
        return f"ERROR: 寫入 Google Calendar 失敗 - {str(e)}"