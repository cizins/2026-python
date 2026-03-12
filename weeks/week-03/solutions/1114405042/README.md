# Week 03 - Robot Lost (pygame)

![gameplay](assets/gameplay.png)

## 功能清單

- 2D 格子地圖顯示（座標 0,0 到 W,H）
- 機器人位置與朝向顯示（三角形）
- scent 顯示（綠色圓點）
- 鍵盤一步一步操作：L / R / F
- N 建立新機器人（保留 scent）
- C 清除所有 scent
- P 進行歷史回放（內建 replay 機制）
- G 匯出 replay.gif（若有安裝 imageio）
- HUD 顯示目前狀態、scent 內容與操作提示
- 額外提供 10x10 字串矩陣工具：robot_core.py 的 get_10x10_matrix

## 執行方式

- Python: 3.9+（本機使用 3.9.6）
- 安裝 pygame：
  - pip install pygame
- 可選安裝（GIF 輸出）：
  - pip install imageio
- 啟動遊戲：
  - python robot_game.py

## 測試方式

- 指令：
  - python -m unittest discover -s tests -p "test_*.py" -v
- 本次結果摘要：
  - 測試總數：11
  - 全數通過：11
  - 失敗：0

## 資料結構選擇理由

1. scent 使用 set[tuple[int, int, str]]
   - O(1) 查詢是否為危險邊界，符合規則「同位置同方向才生效」。
2. 機器人狀態用 dataclass
   - x/y/direction/lost 集中管理，測試可直接比對狀態。
3. 方向與位移使用固定對照表
   - DIRECTIONS 做旋轉，MOVE_VECTOR 做前進，避免多層 if-else。

## 我踩到的 bug 與修正

- 問題：一開始把 scent 只記錄 (x, y)，導致同格不同方向也被錯誤保護。
- 修正：改為 (x, y, direction) 三元組，並在測試加入「同格不同方向不共用 scent」。

## 重播方式

- 即時回放：按 P，會按歷史快照重播操作。
- 匯出 GIF：按 G。
  - 若有安裝 imageio，會輸出 assets/replay.gif。
  - 若未安裝，會顯示提示，仍可使用 P 鍵回放。

## 交付提醒

- 請自行補上 assets/gameplay.png（實際遊玩截圖，必交）。
- 如需 GIF 檔，也請在遊玩後按 G 產生 assets/replay.gif。
