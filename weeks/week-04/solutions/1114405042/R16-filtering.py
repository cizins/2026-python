# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 原始數列：同時包含正數與負數。
mylist = [1, 4, -5, 10]

# 串列推導式（list comprehension）：
# 立即建立新 list，將 mylist 中大於 0 的元素收集起來。
# 適合資料量不大，且你希望立刻拿到完整結果的情境。
[n for n in mylist if n > 0]

# 生成器表達式（generator expression）：
# 不會立刻產生完整清單，而是「需要時才逐個產生」元素，
# 記憶體使用通常更省，適合大量資料串流處理。
pos = (n for n in mylist if n > 0)

# 混合了可轉整數與不可轉整數的字串資料。
values = ['1', '2', '-3', '-', 'N/A']

# 自訂判斷函式：用於檢查字串是否可安全轉成 int。
def is_int(val):
    try:
        # 能成功轉換就代表 val 是合法整數字串。
        int(val); return True
    except ValueError:
        # 轉換失敗（例如 '-'、'N/A'）就回傳 False。
        return False

# filter(function, iterable)：保留 function 回傳 True 的元素。
# 這裡會留下可轉 int 的字串，回傳的是迭代器，
# 透過 list(...) 可把結果一次展開成清單。
list(filter(is_int, values))

# compress(data, selectors)：依照 selectors 的布林值遮罩過濾 data。
from itertools import compress

# data：要被篩選的資料。
addresses = ['a1', 'a2', 'a3']
# selectors 的來源數值。
counts = [0, 3, 10]

# 先把條件（是否 > 5）轉成布林清單，作為遮罩。
more5 = [n > 5 for n in counts]

# 只保留對應遮罩為 True 的地址。
list(compress(addresses, more5))
