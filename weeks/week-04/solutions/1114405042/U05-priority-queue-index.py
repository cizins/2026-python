# U5. 優先佇列為何要加 index（1.5）
# 
# 這個範例展示了在實作「優先權佇列 (Priority Queue)」時，
# 為什麼我們通常會放入 `(priority, index, item)` 這樣三個元素的 Tuple，
# 而不是只放 `(priority, item)` 兩個元素。
#
# 問題的核心在於：當兩個項目的「優先權」相同時，
# Python 的 heapq 會怎麼決定誰比較小、誰該先出來？

import heapq

# 假設我們有一個自訂的類別 Item，它只包含一個 name 屬性。
# 注意：這個類別「沒有」實作魔法方法（如 __lt__，即小於 < 的比較邏輯），
# 所以 Python 不知道如何比較兩個 Item 物件的大小。
class Item:
    def __init__(self, name):
        self.name = name
    
    # 為了方便印出結果，我們加上 __repr__
    def __repr__(self):
        return f"Item({self.name!r})"

pq = []

# ---------------------------------------------------------
# 錯誤示範：只放 (priority, item)
# ---------------------------------------------------------
# 當我們使用 heapq.heappush 把 Tuple 放入 heap 時，
# heapq 會從 Tuple 的第一個元素 (priority) 開始比較大小。
# 如果 priority 不同，那就沒事；
# 但如果 priority 相同 (例如下面都是 -1)，
# heapq 就會「繼續比較 Tuple 的第二個元素 (也就是 item 物件本身)」。
#
# 因為我們的 Item 類別並不支援比較大小 (<)，
# 所以當第二個 Item 試圖與第一個 Item 比較時，程式就會直接崩潰（拋出 TypeError）。

# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # 執行到這行會引發 TypeError: '<' not supported between instances of 'Item' and 'Item'


# ---------------------------------------------------------
# 正確解法：加入 index (索引值) 作為「打破僵局 (Tie-breaker)」的機制
# ---------------------------------------------------------
#為了解決上述「同優先權無法比較物件」的問題，
# 我們會在 Tuple 的中間插入一個不斷遞增的數字 `index`。
# 這樣一來，Tuple 就變成了 `(priority, index, item)`。

idx = 0

# 當壓入第一個元素時，Tuple 是 (-1, 0, Item('a'))
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1  # 每次加入後，索引值遞增

# 當壓入第二個元素時，Tuple 是 (-1, 1, Item('b'))
# 此時 heapq 的比較過程如下：
# 1. 比較 priority：都是 -1，平手！繼續比下一個。
# 2. 比較 index：0 和 1 比較，因為 0 < 1，所以有了明確的勝負結果！
# 3. 由於在第二關 (index) 就分出勝負了，heapq 「永遠不會」去比較第三個元素 (item 物件)。
#
# 這樣不僅成功避免了 TypeError，
# 還帶來了額外的好處：它保證了相同優先權的項目會遵守 FIFO (先進先出) 的原則！
# 因為先加入的項目，其 index 一定比較小，所以會先被 pop 出來。
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1

print("目前 Queue 內容:", pq)

# 取出元素時，我們拿到的會是 (priority, index, item)
# 如果只要 item，可以透過索引 [2] 取得：
popped = heapq.heappop(pq)
print("取出的元素:", popped[2])