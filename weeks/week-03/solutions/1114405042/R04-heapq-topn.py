# R4. heapq 取 Top-N（1.4）

# heapq 是 Python 內建的堆積工具（最小堆 min-heap）。
# 常見用途：
# 1) 取前 N 大 / 前 N 小
# 2) 維護動態最小值
# 3) 實作優先佇列
import heapq

print("=== 範例 1：nlargest 和 nsmallest ===")
# 先準備一串數字，包含正數、負數與重複值。
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(f"原始列表：{nums}")

# nlargest(3, nums)：找出最大的 3 個元素。
# 回傳會是由大到小排列的列表。
top3 = heapq.nlargest(3, nums)
print(f"最大的 3 個數：{top3}")

# nsmallest(3, nums)：找出最小的 3 個元素。
# 回傳會是由小到大排列的列表。
bottom3 = heapq.nsmallest(3, nums)
print(f"最小的 3 個數：{bottom3}")

print("\n=== 範例 2：使用 key 參數篩選字典 ===")
# 這裡資料型態從數字改成字典列表。
# 每筆股票有 name、shares、price 三個欄位。
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
print(f"投資組合：{portfolio}")

# nsmallest 也能配合 key 函式使用。
# key=lambda s: s['price'] 表示「用 price 欄位」當比較依據。
# nsmallest(1, ...) 代表找最小的一筆，也就是最便宜股票。
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f"最便宜的股票：{cheapest}")

print("\n=== 範例 3：heapify 和 heappop ===")
# 建立 nums 的副本，避免改動原始資料。
heap = list(nums)
print(f"原始列表副本：{heap}")

# heapify 會「原地」把列表轉成堆積結構。
# 注意：轉換後列表看起來不會是完整排序，
# 但會滿足堆積性質：heap[0] 一定是最小值。
heapq.heapify(heap)
print(f"heapify 後：{heap}")

# heappop 會彈出並回傳目前最小元素。
min_val = heapq.heappop(heap)
print(f"pop 出最小值：{min_val}")
print(f"pop 後的 heap：{heap}")
