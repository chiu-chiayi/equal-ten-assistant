import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError, ServerError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from tools import ALL_TOOLS

# 設定 Telegram Bot 日誌
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 載入 SOUL.md + AGENT.md
def load_system_instructions() -> str:
    instructions = []
    for filename in ["SOUL.md", "AGENT.md"]:
        path = Path(filename)
        if path.exists():
            instructions.append(path.read_text(encoding="utf-8"))
    return "\n\n---\n\n".join(instructions)

# 載入 .env 檔案，取得 GEMINI_API_KEY 與 TELEGRAM_BOT_TOKEN
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 驗證 Key 是否順利讀取
if not GEMINI_API_KEY or not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ 錯誤：未在 .env 中找到必要的 GEMINI_API_KEY 或 TELEGRAM_BOT_TOKEN")

# 初始化 Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

# 呼叫 Gemini Agent 核心邏輯
def ask_gemini(user_prompt: str) -> str:

    try:
        chat = client.chats.create(
            model="gemini-3.6-flash",
            config=types.GenerateContentConfig(
                system_instruction=load_system_instructions(),
                tools=ALL_TOOLS,
                temperature=0.2,
            )
        )
        response = chat.send_message(user_prompt)
        return response.text
    except ServerError as e:
        if e.code == 503:
            return "⚠️ 伺服器忙碌中 (503)，請稍後再試。"
        return f"❌ 發生伺服器錯誤：{e}"
    except APIError as e:
        if e.code == 401:
            return "❌ API Key 驗證失敗 (401)，請檢查 GEMINI_API_KEY 是否正確。"
        elif e.code == 429:
            return "⚠️ 達到 API 使用限制 (429)，請稍後再試。"
        return f"❌ 發生 API 錯誤：{e}"
    except Exception as e:
        return f"❌ 發生未預期錯誤：{e}"

# Telegram Bot 指令與訊息處理
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 嗨！我是 Equal Ten 助理，今天過得如何？")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # 顯示 Telegram「正在輸入中...」狀態
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # 取得 Gemini 回應並傳回 Telegram
    reply_text = ask_gemini(user_text)
    await update.message.reply_text(reply_text)

# 主程式入口
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram Bot 已成功啟動並監聽中...")
    app.run_polling()

if __name__ == "__main__":
    main()