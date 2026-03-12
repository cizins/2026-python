# R7. OrderedDict（1.7）

# OrderedDict 是 collections 提供的有序字典。
# 與一般 dict 的差異重點（學習情境）：
# - OrderedDict 明確表達「我要保留插入順序」的意圖
# - 在教學與可讀性上，看到 OrderedDict 就知道順序是重點
from collections import OrderedDict
import json

print("=== OrderedDict 保留插入順序 ===")

# 建立一個空的 OrderedDict。
# 後續插入的鍵值會依加入順序被記錄下來。
d = OrderedDict()

# 先加入 foo，再加入 bar。
# 你可以觀察輸出順序：foo 會排在 bar 前面。
d['foo'] = 1
print(f"加入 'foo': 1 後：{d}")

d['bar'] = 2
print(f"加入 'bar': 2 後：{d}")

print("\n=== json.dumps 序列化 OrderedDict ===")

# 把 OrderedDict 轉成 JSON 字串。
# 序列化後，鍵的順序會依原本插入順序呈現。
# 這在需要穩定輸出格式（例如 API 範例、教學展示）時很有用。
json_str = json.dumps(d)
print(f"JSON 字串：{json_str}")
print(f"說明：OrderedDict 確保 JSON 序列化時保持插入順序。")
