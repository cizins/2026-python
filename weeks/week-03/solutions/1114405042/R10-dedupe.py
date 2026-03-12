# R10. 去重且保序（1.10）

# dedupe(items) 的目標：
# 1) 去除重複元素
# 2) 保留原本出現順序（第一次出現會被保留）
#
# 核心做法：
# - seen: 用 set 記錄「已經看過」的值
# - 走訪 items 時，只有「第一次出現」才輸出
#
# 注意：這裡使用 yield，代表這是一個「生成器函式」：
# - 不會一次建立完整列表
# - 會逐個產生結果（節省記憶體）
def dedupe(items):
    seen = set()
    for item in items:
        # 如果這個值還沒看過，才輸出並記錄
        if item not in seen:
            yield item
            seen.add(item)


# dedupe2(items, key=None) 是進階版：
# 可以指定「比較規則」來決定是否重複。
#
# 為什麼需要 key？
# - 有些資料本身不可直接放進 set 比較（例如 dict）
# - 或者你只想用某個欄位判斷重複（例如只看 x，不看 y）
#
# key(item) 會產生「比較用的值」，
# 例如 key=lambda r: r['x'] 表示只用 x 欄位去重。
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        # 若沒提供 key，就直接用 item 本身比較；否則用 key(item) 比較
        val = item if key is None else key(item)
        # 只要比較值 val 第一次出現，就保留原始 item
        if val not in seen:
            yield item
            seen.add(val)


# ------------------------------
# 範例 1：基本去重（數字列表）
# ------------------------------
print("=== 範例 1：dedupe 基本去重（保序） ===")
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(f"原始列表：{a}")

# dedupe(a) 回傳生成器，轉成 list 才會看到完整結果
result = list(dedupe(a))
print(f"去重後：{result}")
print("說明：保留第一次出現的元素，移除後續重複。")


# -----------------------------------------
# 範例 2：使用 key 參數做「字典資料」去重
# -----------------------------------------
print("\n=== 範例 2：dedupe2 使用 key 參數（字典去重）===")
records = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 5}]
print(f"原始記錄：{records}")

# 這裡只用 x 欄位判斷重複：
# - 第一筆 x=2 保留
# - 第二筆 x=1 保留
# - 第三筆 x=2 視為重複，移除
deduped = list(dedupe2(records, key=lambda r: r['x']))
print(f"按 'x' 值去重後：{deduped}")
print("說明：根據 key 函數判斷 'x' 值，保留第一個，移除後續重複的 'x'。")
