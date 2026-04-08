# 這是更簡單、更容易記憶的寫法 (Easy version)
#
# 解題思路 (Top-Down DP + 記憶化搜索):
# 1. 直接用 Python 內建的 `@lru_cache` (Least Recently Used Cache) 來實作記憶化搜索。
# 2. 我們定義一個函式 `dfs(r, st1, st2)`:
#    - `r`: 當前正在決定第 r 列 (row) 的炮兵擺法。
#    - `st1`: 第 r-1 列 (上一列) 的炮兵狀態。
#    - `st2`: 第 r-2 列 (上上列) 的炮兵狀態。
# 3. 在函式內，我們枚舉第 r 列所有「可能且合法的擺法」(不與地形衝突、且自身左右距離合理)。
# 4. 對於每一種合法的擺法 `curr_st`，我們檢查它是否與 `st1` 或 `st2` 衝突 (利用位元 AND 運算 `&`)。
# 5. 如果不衝突，我們就加上這列佈署的炮兵數量，然後遞迴呼叫 `dfs(r + 1, curr_st, st1)`，去算下一列。
# 6. 這樣的寫法把繁瑣的陣列索引管理，轉變為了直觀的函式呼叫，而且在效能上也完全不會輸給普通的 DP！

from functools import lru_cache

def solve_easy(n: int, m: int, grid: list[str]) -> int:
    """
    計算最多能部署的炮兵數量 (簡易版：使用 DFS + lru_cache)。
    """
    if n == 0 or m == 0:
        return 0
        
    # 步驟 1: 將地圖轉換為整數的位元遮罩，1 代表山地 (不能放置)，0 代表平原
    mountains = []
    for row in grid:
        mask = 0
        for i, char in enumerate(row):
            if char == 'H':
                mask |= (1 << i)
        mountains.append(mask)
        
    # 步驟 2: 預先找出單行所有「自身不會互相攻擊」的合法放置狀態
    valid_states = []
    for i in range(1 << m):
        if (i & (i << 1)) == 0 and (i & (i << 2)) == 0:
            valid_states.append(i)

    # 步驟 3: 定義遞迴函數
    # 參數 r: 當前列數 (0 到 n-1)
    # 參數 st1: 上一列的狀態
    # 參數 st2: 上上列的狀態
    @lru_cache(None)  # None 代表快取沒有上限
    def dfs(r, st1, st2):
        # 如果已經超過最後一列，沒辦法再放了，回傳 0
        if r == n:
            return 0
            
        max_artillery = 0
        
        # 嘗試在第 r 列放入各種預先算好的合法狀態
        for curr_st in valid_states:
            # 檢查 1: 是否與地形衝突 (不能放在山地)
            if curr_st & mountains[r]:
                continue
            # 檢查 2: 是否與上一列 (st1) 發生縱向衝突
            if curr_st & st1:
                continue
            # 檢查 3: 是否與上上列 (st2) 發生縱向衝突
            if curr_st & st2:
                continue
                
            # 計算當前這個狀態放了幾個炮兵 (二進位裡面 1 的個數)
            count = bin(curr_st).count('1')
            
            # 繼續往下決定下一列 (原本的 curr_st 變成了上一列，原本的 st1 變成了上上列)
            max_artillery = max(max_artillery, count + dfs(r + 1, curr_st, st1))
            
        return max_artillery
        
    # 一開始在第 0 列，且沒有上一列和上上列的狀態，所以初始狀態填 0
    return dfs(0, 0, 0)
