# Understand（理解）- itertools 工具函數

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

# 這份範例示範 itertools 中常見且實用的工具函數。
# 重點不是背 API，而是理解「它們如何處理可迭代物件（iterable）」。
# 你可以把這份檔案當成一個小型實驗室，逐段執行並觀察輸出差異。

print("--- islice() 切片 ---")


def count(n):
    # 從 n 開始產生無限遞增整數。
    # 這是一個生成器（generator）：
    # 每次迭代只產生一個值，不會一次把所有值存進記憶體。
    i = n
    while True:
        # yield 會「暫停函式」並回傳目前值，
        # 下一次迭代再從這裡繼續。
        yield i
        i += 1


# 建立一個從 0 開始的無限序列。
c = count(0)
# islice(c, 5, 10) 的意思：
# 跳過前 5 個元素（0~4），取索引 5~9，共 5 個值。
# 注意：islice 不會回傳 list，而是迭代器，所以用 list(...) 轉成可視化結果。
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile 會從開頭開始「持續丟棄」元素，直到條件第一次不成立為止。
# 一旦遇到不符合條件的元素，後面元素就全部保留（不再繼續檢查丟棄）。
# 這裡流程為：
# 1(<5) 丟、3(<5) 丟、5(不<5) 停止丟棄，之後 [5,2,4,6] 全保留。
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile 則是從開頭開始「持續取用」元素，直到條件第一次不成立就停止。
# 和 dropwhile 剛好互補：
# 這裡會取到 [1,3]，遇到 5 時停止（5 不小於 5）。
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
# chain 會把多個可迭代物件「視為一條連續序列」依序走訪。
# 它不會建立巢狀清單，而是平順串接成單一迭代流程。
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
print(f"permutations(items):")
# permutations(items) 預設長度 r = len(items)。
# 因為是「排列」，順序不同算不同結果，且不重複使用同一元素。
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
# 指定 r=2，代表從 3 個元素中挑 2 個來排，
# 例如 ('a','b') 與 ('b','a') 會視為兩種不同排列。
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
print(f"combinations(items, 2):")
# combinations 是「組合」：順序不同視為同一組，
# 所以 ('a','b') 與 ('b','a') 只會出現一次。
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 用 permutations(chars, 2) 模擬「字元不可重複」的 2 位密碼。
# 例如 AA 不會出現，AB 與 BA 會分別出現。
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement 允許重複取值，
# 但仍屬於組合概念（不看順序），因此 AB 與 BA 不會同時出現。
# 若你要「可重複且看順序」的情境，通常可考慮 product(chars, repeat=2)。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
