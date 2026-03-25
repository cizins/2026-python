import sys

# 這是針對 UVA 10055 單調函數問題的簡易且好記的解法！
#
# 【解題核心概念】：
# 1. 函數的「增減性複合」就像是「正負號相乘」：
#    - 增函數(0) 代入 增函數(0) = 增函數(0)  --> 正 * 正 = 正
#    - 減函數(1) 代入 增函數(0) = 減函數(1)  --> 負 * 正 = 負
#    - 增函數(0) 代入 減函數(1) = 減函數(1)  --> 正 * 負 = 負
#    - 減函數(1) 代入 減函數(1) = 增函數(0)  --> 負 * 負 = 正
# 2. 我們發現，只要這個區間 [L, R] 裡面的「減函數」有奇數個，結果就是「減函數(1)」；
#    如果「減函數」有偶數個（包含 0 個），結果就是「增函數(0)」。
#
# 【資料結構的選擇】：
# 這個題目 N 和 Q 都高達 20 萬，如果用一個陣列慢慢從 L 加到 R 絕對會超時 (Time Limit Exceeded)。
# 因此我們必須用「樹狀陣列 (Binary Indexed Tree, BIT)」，這是一種簡單好寫、可以在 O(log N) 內完成單點修改與區間求和的資料結構。
# 如果不了解 BIT 原理，只要把它當作「能夠快速修改陣列並計算總和的黑盒子」即可。

# BIT (樹狀陣列) 的三部曲：
def add(bit, i, delta, n):
    """將位置 i 的值加上 delta"""
    while i <= n:
        bit[i] += delta
        i += i & (-i) # 這是固定寫法：加上最右邊的 1 (lowbit)，跳到父節點

def query(bit, i):
    """查詢從第 1 個到第 i 個的總和"""
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i) # 這是固定寫法：減去最右邊的 1 (lowbit)，跳回前一個區間
    return s

def main():
    # 快速讀取所有資料
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    q = int(data[1])
    
    # 初始化樹狀陣列，大小開 n+1 是因為 BIT 必須從索引 1 開始使用
    bit = [0] * (n + 1)
    
    # 初始化每個函數的狀態 (0 表示增，1 表示減)
    states = [0] * (n + 1)
    
    idx = 2 # 從讀取完 N, Q 之後的索引開始處理
    
    for _ in range(q):
        if idx >= len(data): break
        
        v = int(data[idx]) # 取得操作類型
        
        if v == 1: # 操作 1：反轉
            i = int(data[idx+1])
            idx += 2
            
            # 如果目前狀態是 0 (增)，反轉變成 1 (減)，變化量就是 +1
            # 如果目前狀態是 1 (減)，反轉變成 0 (增)，變化量就是 -1
            delta = 1 if states[i] == 0 else -1
            states[i] = 1 - states[i] # 更新狀態
            
            # 將變化量更新到樹狀陣列中
            add(bit, i, delta, n)
            
        elif v == 2: # 操作 2：查詢
            L = int(data[idx+1])
            R = int(data[idx+2])
            idx += 3
            
            # 利用前綴和的概念求區間 [L, R] 之間的總和
            # 總和就是 [1 到 R 的總和] 減去 [1 到 L-1 的總和]
            count = query(bit, R) - query(bit, L - 1)
            
            # 總數是奇數還是偶數？
            # 奇數(餘數1) -> 減函數(1)
            # 偶數(餘數0) -> 增函數(0)
            print(count % 2)

if __name__ == '__main__':
    main()
