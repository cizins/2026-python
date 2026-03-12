# R5. 優先佇列 PriorityQueue（1.5）

# heapq 是 Python 內建的最小堆積（min-heap）工具。
# 最小堆積特性：每次 heappop 會先取出「最小值」。
#
# 但這題希望「優先度越大越先出來」，也就是最大優先先出。
# 所以會把 priority 轉成負值存入 heap：
# - 原本 priority=3 會存成 -3
# - 由於 -3 < -1，所以會先被彈出，等效於高優先度先出。
import heapq


# 這是一個簡化版的優先佇列類別。
# 支援兩個主要操作：
# 1) push(item, priority): 加入任務與優先度
# 2) pop(): 取出目前最高優先度的任務
class PriorityQueue:
    # 初始化：
    # _queue 用來存 heap 結構
    # _index 用來記錄插入順序（解決同優先度時的比較問題）
    def __init__(self):
        self._queue = []
        self._index = 0

    # push 時，實際放進 heap 的資料是三元組：
    # (-priority, _index, item)
    #
    # 比較順序會先比第一個欄位，再比第二個欄位：
    # 1) 先比 -priority -> 優先度高者（數值大）先出
    # 2) 若優先度相同，再比 _index -> 先加入的先出（FIFO）
    #
    # 為什麼要放 _index？
    # 如果只放 (-priority, item)，當 priority 一樣時，Python 會嘗試比較 item。
    # 若 item 是無法比較的物件，可能拋出 TypeError。
    # 放 _index 可避免直接比較 item，也讓行為更穩定。
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    # heappop 會回傳整個三元組，例如 (-3, 0, '任務A')。
    # 我們只需要原始任務內容 item，因此取 [-1] 回傳。
    def pop(self):
        return heapq.heappop(self._queue)[-1]


# ------------------------------
# 示範：加入與取出
# ------------------------------
print("=== 優先佇列使用範例 ===")
pq = PriorityQueue()

print("\n1. 加入任務（任務名稱, 優先度）：")
pq.push("任務A", 3)
print("  加入『任務A』，優先度 3")

pq.push("任務B", 1)
print("  加入『任務B』，優先度 1")

pq.push("任務C", 2)
print("  加入『任務C』，優先度 2")

print("\n2. 依優先度取出任務（高優先度先取出）：")
task1 = pq.pop()
print(f"  第 1 個取出：{task1}")

task2 = pq.pop()
print(f"  第 2 個取出：{task2}")

task3 = pq.pop()
print(f"  第 3 個取出：{task3}")
