# TEST_LOG

## Run 1 - Red (預期失敗)

- 執行時間：2026-03-12
- 指令：python -m unittest discover -s tests -p "test_*.py" -v
- 結果摘要：
  - 測試總數：2
  - 通過：0
  - 失敗：0
  - 錯誤：2
- 關鍵訊息：ModuleNotFoundError: No module named 'robot_core'
- 從失敗到通過做了哪些修改：
  - 新增 robot_core.py，完成 L/R/F、越界 LOST、scent 規則。
  - 新增 robot_game.py 並保持畫面與核心解耦。

## Run 2 - Green (全通過)

- 執行時間：2026-03-12
- 指令：python -m unittest discover -s tests -p "test_*.py" -v
- 結果摘要：
  - 測試總數：11
  - 通過：11
  - 失敗：0
  - 錯誤：0
- 從失敗到通過做了哪些修改：
  - 補齊 scent 的方向維度 (x, y, dir) 與 LOST 後停止執行。
  - 補上非法指令 ValueError，讓行為可預期且可測試。
