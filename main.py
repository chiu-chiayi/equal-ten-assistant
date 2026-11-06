import os
import sys

try:
    import openclaw
except ImportError:
    print("錯誤：找不到 openclaw 套件", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    print("正在啟動 Equal Ten Assistant (OpenClaw)...")
    
    # 嘗試調用 openclaw 的進入點
    if hasattr(openclaw, "main"):
        openclaw.main()
    elif hasattr(openclaw, "cli"):
        openclaw.cli()
    elif hasattr(openclaw, "run"):
        openclaw.run()
    else:
        # 若無封裝進入點，輸出 openclaw 的模組內容協助偵錯
        print("OpenClaw 模組屬性:", dir(openclaw))
