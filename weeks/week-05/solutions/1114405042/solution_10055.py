class FenwickTree:
    """
    樹狀陣列 (Binary Indexed Tree, BIT)
    這是一個可以用來在 O(log N) 的時間內完成「單點修改」與「區間求和」的資料結構。
    """
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
        # 用一個陣列紀錄目前每個函數的狀態，0 為增函數，1 為減函數
        self.states = [0] * (size + 1)

    def toggle(self, i):
        """
        反轉第 i 個函數的狀態 (增函數變減函數，減函數變增函數)
        """
        # 如果原本是 0 (增)，反轉後變成 1，變化量為 +1
        # 如果原本是 1 (減)，反轉後變成 0，變化量為 -1
        delta = 1 if self.states[i] == 0 else -1
        self.states[i] = 1 - self.states[i]
        
        # 更新樹狀陣列
        idx = i
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx) # 加上最低位的 1 (lowbit)

    def query_prefix(self, i):
        """
        查詢前 i 個函數中，有多少個是減函數 (狀態為 1)
        """
        total = 0
        idx = i
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx) # 減去最低位的 1 (lowbit)
        return total

    def query_range(self, l, r):
        """
        查詢區間 [l, r] 中，減函數的數量
        """
        return self.query_prefix(r) - self.query_prefix(l - 1)

def solve(n, queries):
    """
    處理所有查詢操作並回傳結果
    
    參數:
    n (int): 函數的總數
    queries (list): 查詢與更新操作的列表，例如 [(1, i), (2, l, r)]
    
    回傳:
    list: 對應所有 v=2 查詢的結果 (0 或 1)
    """
    bit = FenwickTree(n)
    results = []
    
    for q in queries:
        if q[0] == 1:
            # v = 1：反轉函數 f_i 的增減性
            i = q[1]
            bit.toggle(i)
        elif q[0] == 2:
            # v = 2：查詢區間 [L, R] 內複合函數的增減性
            l, r = q[1], q[2]
            # 根據數學原理：
            # 增函數代入增函數 -> 增
            # 減函數代入增函數 -> 減
            # 增函數代入減函數 -> 減
            # 減函數代入減函數 -> 增
            # 也就是說，只要這區間內的「減函數」有奇數個，最後結果就是減函數(1)；偶數個就是增函數(0)
            count = bit.query_range(l, r)
            results.append(count % 2)
            
    return results

import sys

def main():
    # 讀取標準輸入
    # 由於測資可能很大，使用 sys.stdin.read 比較有效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    q = int(input_data[1])
    
    queries = []
    idx = 2
    for _ in range(q):
        if idx >= len(input_data):
            break
        v = int(input_data[idx])
        if v == 1:
            queries.append((1, int(input_data[idx+1])))
            idx += 2
        elif v == 2:
            queries.append((2, int(input_data[idx+1]), int(input_data[idx+2])))
            idx += 3
            
    # 執行並輸出
    results = solve(n, queries)
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
