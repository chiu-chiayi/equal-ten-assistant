#!/bin/bash
set -e  # 遇到錯誤立刻停止執行

echo "🚀 開始自動建置 Python 虛擬環境..."

# 1. 移除舊的 .venv（若存在）
if [ -d ".venv" ]; then
    echo "🧹 清除舊的 .venv..."
    rm -rf .venv
fi

# 2. 尋找系統中較新的 Python 版本 (優先使用 python3.11 或 python3.10)
PYTHON_BIN=$(which python3)

echo "🐍 使用的 Python 執行檔: $PYTHON_BIN"
$PYTHON_BIN --version

# 3. 建立虛擬環境
echo "📦 建立全新的 .venv..."
$PYTHON_BIN -m venv .venv

# 4. 啟動虛擬環境並升級核心套件
echo "⬆️ 升級 pip 與 setuptools..."
source .venv/bin/activate
pip install --upgrade pip setuptools

# 5. 安裝專案相依套件
echo "📥 安裝專案所需套件 (google-genai, python-telegram-bot)..."
pip install python-dotenv google-genai python-telegram-bot google-api-python-client google-auth-httplib2 google-auth-oauthlib

echo "✅ 虛擬環境建置完成！"