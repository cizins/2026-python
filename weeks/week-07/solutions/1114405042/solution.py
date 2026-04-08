# POJ 2182 / UVA 10062 變形 - 乳牛排隊 (Lost Cows)
# 
# 題意:
# 有 N 頭牛 (1 ~ N)，給定每個位置前面有幾頭牛編號比牠小。
# 求原來這 N 頭牛的編號。
#
# 解法:
# 從後面往前推。因為最後一頭牛前面就是所有的牛，所以如果牠前面有 x 頭牛比牠小，
# 代表牠的編號是「目前剩下的數字中，第 x+1 小的」。
# 由於 N 可達 80,000，使用 Python 內建 list 的 pop 操作雖然理論最糟是 O(N^2)，
# 但因其底層實作為連續記憶體區塊移動，常數極小，通常能通過。
# 若要嚴格 O(N log N) 可使用 Binary Indexed Tree (Fenwick Tree) 或 Segment Tree。
# 這裡展示使用 BIT (樹狀數組) 搭配二分搜尋的標準解法。

def solve(n, smaller_counts):
    """
    計算每頭牛的原始編號。
    n: 牛的總數
    smaller_counts: 長度為 n-1 的串列，表示第 2 到第 n 頭牛前面有幾頭牛編號比牠小。
    """
    # tree 陣列，大小為 n+1，用來維護 1~n 每個數字是否還存在 (1 表示存在，0 表示已被選走)
    tree = [0] * (n + 1)
    
    def add(idx, val):
        while idx <= n:
            tree[idx] += val
            idx += idx & (-idx)
            
    def query(idx):
        res = 0
        while idx > 0:
            res += tree[idx]
            idx -= idx & (-idx)
        return res
        
    # 初始化 BIT，所有數字 1~n 剛開始都存在 (頻率為 1)
    for i in range(1, n + 1):
        add(i, 1)
        
    # 建立完整的 smaller_counts 陣列 (第一頭牛前面沒有比牠小的，設為 0)
    full_counts = [0] + smaller_counts
    ans = [0] * n
    
    # 從最後一頭牛往前處理
    for i in range(n - 1, -1, -1):
        target = full_counts[i] + 1  # 我們要找目前剩下的數字中，第 target 小的
        
        # 二分搜尋找這個數字
        left, right = 1, n
        chosen_number = -1
        while left <= right:
            mid = (left + right) // 2
            # query(mid) 會回傳 <= mid 的數字中還有幾個未被選走
            if query(mid) >= target:
                chosen_number = mid
                right = mid - 1
            else:
                left = mid + 1
                
        ans[i] = chosen_number
        # 找到後，將這個數字從 BIT 中移除 (頻率減 1)
        add(chosen_number, -1)
        
    return ans
