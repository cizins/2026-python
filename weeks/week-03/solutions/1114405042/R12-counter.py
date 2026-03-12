# R12. Counter 統計 + most_common（1.12）

# Counter 是 collections 提供的「計數器」類別。
# 你可以把它想成「專門拿來統計元素出現次數的字典」：
# - key: 元素內容（例如單字）
# - value: 出現次數（整數）
from collections import Counter

# 準備要統計的資料：一個單字列表。
# 這裡 look 出現了 2 次，其他大多出現 1 次。
words = ['look', 'into', 'my', 'eyes', 'look']
print("=== Counter 統計範例 ===")
print(f"原始單字列表：{words}")

# 直接把列表丟進 Counter，會自動完成統計。
# 等價概念：逐一讀取 words，每看到一個元素就把計數 +1。
word_counts = Counter(words)
print(f"\nCounter 統計結果：{word_counts}")

# most_common(3) 會回傳「前 3 個最常出現元素」。
# 回傳型態是 list，內容是 (元素, 次數) 的 tuple。
# 例如 [('look', 2), ('into', 1), ('my', 1)]
top3 = word_counts.most_common(3)
print(f"出現次數最多的前 3 名：{top3}")

# update(...) 可以把新資料合併進既有計數。
# 這裡再加入兩個 'eyes'，等於把 eyes 的次數再加 2。
word_counts.update(['eyes', 'eyes'])
print("\n更新計數：加入 ['eyes', 'eyes']")
print(f"更新後統計結果：{word_counts}")
