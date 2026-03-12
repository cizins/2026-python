# R3. deque 保留最後 N 筆（1.3）

# deque（double-ended queue）是「雙端佇列」：
# - 可以在左端與右端都做新增/刪除
# - 比一般 list 更適合做佇列操作
#
# 常見用途：
# 1) 保留最近 N 筆資料（rolling window）
# 2) 需要在頭尾都高效率插入/刪除的場景
from collections import deque

print("=== 範例 1：固定長度 deque（maxlen=3）===")

# 設定 maxlen=3，代表最多只保留 3 筆。
# 超過時會自動丟掉「最舊」的元素（預設從左端淘汰）。
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(f"加入 1、2、3 後：{list(q)}")

# 此時再 append(4) 會超出容量，
# deque 會自動移除最左邊（最早進來）的 1。
q.append(4)  # 自動丟掉最舊的 1
print(f"再加入 4（超出長度）後：{list(q)}")
print("說明：最舊的元素 1 已被自動移除。")

print("\n=== 範例 2：appendleft / pop / popleft ===")

# 這裡建立不限制長度的 deque（未設定 maxlen）。
q = deque()

# append(x)：從右端加入元素
q.append(1)
print(f"append(1) 後：{list(q)}")

# appendleft(x)：從左端加入元素
q.appendleft(2)
print(f"appendleft(2) 後：{list(q)}")

# pop()：從右端移除並回傳元素
right = q.pop()
print(f"pop() 取出右端元素：{right}，目前 deque：{list(q)}")

# popleft()：從左端移除並回傳元素
left = q.popleft()
print(f"popleft() 取出左端元素：{left}，目前 deque：{list(q)}")
