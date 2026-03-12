# R9. 兩字典相同點：keys/items 集合運算（1.9）

# 準備兩個字典：
# a 與 b 的 key 有部分重疊（x、y），也有各自獨有的 key（z、w）。
# 這很適合示範「集合運算」在字典分析上的應用。
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print("=== 兩個字典 ===")
print(f"a = {a}")
print(f"b = {b}")

print("\n=== keys 的集合運算 ===")
# a.keys() 和 b.keys() 回傳的是 dict_keys 視圖。
# 這個視圖支援集合運算，例如：交集(&)、差集(-)、聯集(|)。
#
# 交集：找出兩個字典都存在的 key。
common_keys = a.keys() & b.keys()
print(f"a.keys() & b.keys()（交集）：{common_keys}")

# 差集：找出只在 a 出現、但不在 b 的 key。
# 這裡結果會是 {'z'}。
only_in_a = a.keys() - b.keys()
print(f"a.keys() - b.keys()（只在 a 中）：{only_in_a}")

print("\n=== items 的集合運算 ===")
# a.items() 與 b.items() 會得到 (key, value) 配對的視圖。
# 對 items 做交集時，必須 key 和 value 都完全相同才算相同。
#
# 在這組資料中：
# - ('y', 2) 兩邊都一樣，會被保留
# - ('x', 1) 與 ('x', 11) value 不同，因此不算相同項目
common_items = a.items() & b.items()
print(f"a.items() & b.items()（相同的鍵值對）：{common_items}")

print("\n=== 字典推導式：移除特定鍵 ===")
# 字典推導式搭配 key 的差集，建立過濾後的新字典：
# a.keys() - {'z', 'w'} 的意思是：
# - 從 a 的 key 集合中，排除 z 與 w
# - 注意：w 不在 a 裡，排除它不會報錯，結果不受影響
#
# 最後只保留剩下的 key 對應值，組成新字典 c。
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print(f"移除 'z' 和 'w' 後的字典：{c}")
print(f"說明：保留 a 中除了 'z' 和 'w' 之外的所有鍵值對。")
