# R8. 字典運算：min/max/sorted + zip（1.8）

# 這是一個「股票代碼 -> 價格」的字典。
# key 是股票代碼，value 是股價。
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
print("=== 股票價格字典 ===")
print(f"原始資料：{prices}")

print("\n=== 使用 zip 配對 (價格, 股票代碼) ===")
# zip(prices.values(), prices.keys()) 會把兩個可迭代物件逐項配對：
# - 第 1 個 tuple: (45.23, 'ACME')
# - 第 2 個 tuple: (612.78, 'AAPL')
# - 第 3 個 tuple: (10.75, 'FB')
#
# 這裡刻意配成 (價格, 代碼)，因為等等 min/max 會先比較 tuple 第一個元素。
print(f"zip(prices.values(), prices.keys())：{list(zip(prices.values(), prices.keys()))}")

print("\n=== 找出最低價和最高價 ===")
# min 會在 tuple 間做比較，先比第一個元素（價格），
# 因此會得到「價格最小」的 (價格, 代碼) 組合。
min_price = min(zip(prices.values(), prices.keys()))
print(f"min()：{min_price}（最低價 $10.75 的 FB）")

# max 同理，會得到「價格最大」的 (價格, 代碼) 組合。
max_price = max(zip(prices.values(), prices.keys()))
print(f"max()：{max_price}（最高價 $612.78 的 AAPL）")

print("\n=== 排序所有股票（按價格升序）===")
# sorted 會把所有 (價格, 代碼) tuple 依價格由小到大排列。
sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(f"sorted()：{sorted_prices}")

print("\n=== 使用 key 參數直接找最低/最高股票代碼 ===")
# 另一種常見寫法：直接在「字典的 key」中找最小/最大。
# min(prices, key=...) 回傳的是 key（股票代碼），不是 value。
#
# key=lambda k: prices[k] 的意思：
# - 對每個 key（例如 'ACME'）
# - 取出對應價格 prices[k] 當比較依據
cheapest = min(prices, key=lambda k: prices[k])
print(f"min(prices, key=...)：'{cheapest}'（回傳 key，價格最低）")

# max 版本完全同理，只是找價格最大的 key。
most_expensive = max(prices, key=lambda k: prices[k])
print(f"max(prices, key=...)：'{most_expensive}'（回傳 key，價格最高）")
