# Remember（記憶）- enumerate() 和 zip()
# 這個腳本介紹了 Python 中兩個非常實用的內建函式：enumerate() 和 zip()

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate() 會將一個可迭代物件（如列表）組合成一個索引序列
# 每次迭代會回傳一個包含 (索引, 值) 的元組 (tuple)
# 預設索引從 0 開始
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 可以透過 start 參數來指定起始的索引值
# 這裡指定 start=1，所以索引會從 1 開始計算
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# enumerate() 非常適合用來處理需要行號的情況，例如讀取檔案內容
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip() 可以將多個可迭代物件（如列表）打包成一個個元組 (tuple)
# 它會將相同位置的元素組合在一起
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
# 同時迭代 names 和 scores，每次取出相同索引的元素
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# zip() 不限於兩個序列，可以接收任意數量的可迭代物件
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
# 將三個列表中的元素對應位置打包
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 當傳入 zip() 的序列長度不一致時，它會以「最短」的序列為準進行打包
# 超出最短長度的元素會被忽略
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")  # 結果只會有兩個元組

from itertools import zip_longest

# 如果希望保留所有元素（以最長序列為準），可以使用 itertools 模組中的 zip_longest
# 較短序列缺失的部分，預設會補上 None，也可以透過 fillvalue 參數指定預設值
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# zip() 非常適合用來將兩個列表組合成一個字典
# 一個列表作為鍵 (keys)，另一個列表作為值 (values)
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
# 先用 zip 打包成 (key, value) 的元組，再轉成 dict
d = dict(zip(keys, values))
print(f"dict: {d}")