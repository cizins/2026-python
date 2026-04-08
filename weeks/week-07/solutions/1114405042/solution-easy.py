# 這是更簡單、更容易記憶的解法版本 (Easy version)
#
# 解題思路：
# 1. 知道每頭牛前面有幾頭編號比牠小。
# 2. 如果從最後一頭牛開始往前推，因為最後一頭牛後面沒有其他牛，
#    所以如果牠前面有 x 頭比牠小，代表牠的編號就是「目前剩下的數字中，第 x+1 小的」。
# 3. 於是我們建立一個清單 `candidates` 包含 1 到 n，表示所有可以選擇的數字。
# 4. 從最後一頭牛開始，根據牠的 `x` 值，直接使用 Python list 的 pop 操作取出對應的數字。
#    因為 Python 的 list 索引從 0 開始，所以「剩下的第 x+1 小數字」剛好就是 `candidates.pop(x)`！
# 5. 這個方法程式碼非常短，不需要學習複雜的樹狀結構 (如 BIT 或 Segment Tree)。
#    雖然 `pop` 內部是 O(N) 操作，讓整體時間複雜度變成 O(N^2)，但在 Python 中這種連續記憶體的移動非常快，實用且容易在面試或比賽中寫出來。

def solve_easy(n, smaller_counts):
    """
    計算每頭牛的原始編號 (簡易版)。
    利用 Python list 的 pop 方法快速移除並取得元素。
    
    參數:
    n (int): 牛的總數。
    smaller_counts (list): 長度為 n-1 的串列，代表第 2 頭到第 n 頭牛，前面有幾頭牛編號比牠小。
    
    回傳:
    list: 長度為 n，代表從隊伍最前面到最後面每頭牛的原始編號。
    """
    # 步驟 1: 建立 1 到 n 的候選名單。這些是所有還沒被排進隊伍的牛的編號。
    candidates = list(range(1, n + 1))
    
    # 步驟 2: 為了方便統一處理，將第一頭牛的條件 (0 頭牛在牠前面且比牠小) 補在最前面。
    full_counts = [0] + smaller_counts
    
    # 準備一個陣列存放結果
    ans = [0] * n
    
    # 步驟 3: 逆向處理，從隊伍的最後一頭牛往前推算。
    for i in range(n - 1, -1, -1):
        count = full_counts[i]
        # 直接從 candidates 裡面抽出第 count 個數字 (因為索引從 0 開始)。
        # 抽出來的同時，這個數字也會從 candidates 中移除，後面的數字會自動往前補齊。
        ans[i] = candidates.pop(count)
        
    return ans
