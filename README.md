# Equal Ten Assistant

這是一個以 Telegram 作為互動入口、以 Google Gemini 作為 AI 核心的個人助理型專案。它目前能夠接收訊息、產生自然語言回應，並透過工具擴充實際能力，例如查詢時間與建立 Google Calendar 行程。

## 專案定位

Equal Ten Assistant 的核心目標不是只做聊天機器人，而是打造一個可持續擴充的 AI 助理基礎架構。它適合用於：

- 個人助理型對話
- Telegram 即時互動
- AI 工具呼叫與任務執行
- 日常工作流程自動化

## 目前功能

- Telegram Bot 訊息互動
- Gemini AI 回應生成
- 繁體中文人設與語氣設定
- 工具擴充能力：
  - 取得當前時間
  - 建立 Google Calendar 行程

## 專案結構

```text
.
├── .env
├── .venv
├── AGENTS.md
├── README.md
├── SOUL.md
├── bot.py
├── get_token.py
├── setup_env.sh
├── tools/
│   ├── __init__.py
│   ├── calendar_tool.py
│   └── time_tool.py
```

## 應用場景

這個專案適合做為以下類型的基礎：

- 個人生活助理
- 簡單的行程管理助手
- AI 輔助的消息處理工具
- 之後延伸為任務管理、提醒、知識查詢或數據處理的入口

## 未來發展方向

這個專案的最大優勢在於「可擴充」。未來可持續發展方向包括：

- 新增更多工具能力（天氣、新聞、待辦、資料查詢）
- 加入指令系統（如 `/help`、`/todo`、`/status`）
- 整合資料庫，保存使用者資料與歷史互動
- 支援更完整的自動化流程與提醒機制
- 擴大成多功能 AI 助理平台

## 安裝與啟動

1. 建立環境

```bash
bash setup_env.sh
```

2. 設定 `.env`，加入：

```env
GEMINI_API_KEY="your_gemini_api_key"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
```

3. 啟動 Bot

```bash
python bot.py
```

## 設計理念

這個專案的核心精神是：

- 以對話為入口
- 以工具為執行能力
- 以 AI 為核心決策
- 以模組化架構支撐持續成長

也就是說，現在它已經能夠做一個小型助手；未來只要新增更多工具與流程，就能逐步演進成更完整的個人工作助理。

## 總結

Equal Ten Assistant 是一個以 Telegram + Gemini 為基礎的 AI 助理原型，現在已具備聊天與工具呼叫能力，未來有很大的擴充空間。它適合作為個人化助理、日程管理助手，並可逐步發展成更強大的自動化工作平台。
