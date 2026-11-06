# 採用 Python 官方輕量級環境
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 安裝系統基本元件與 git
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# 下載並安裝 OpenClaw 套件
RUN pip install --no-cache-dir openclaw

# 將當前目錄的 SOUL.md, AGENTS.md 等設定檔複製進容器
COPY . /app

# 啟動 OpenClaw 服務
CMD ["openclaw", "run"]
