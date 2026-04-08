# 題目 10093 (POJ 1185 炮兵陣地)：炮兵部署問題
# 
# 題意:
# 在 N x M 的地圖上部署炮兵。
# 'H' 代表山地，不能部署。'P' 代表平原，可以部署。
# 炮兵的攻擊範圍為上下各2格，左右各2格。任何兩個炮兵不能互相攻擊。
# 求最多能部署多少炮兵。
#
# 解法 (狀態壓縮 DP):
# 因為 M <= 10，每一行的狀態可以壓縮成一個整數 (Bitmask)。
# 例如：二進位 1010 代表第0格與第2格放置炮兵。
#
# 1. 預處理合法的單行狀態：同一行內不能有距離 <= 2 的炮兵。
#    因此合法的狀態 s 必須滿足: (s & (s << 1)) == 0 且 (s & (s << 2)) == 0。
# 2. 定義狀態：
#    dp[i][j][k] 表示第 i 行狀態為 j，第 i-1 行狀態為 k 時，前 i 行最多能放的炮兵數。
# 3. 狀態轉移：
#    dp[i][j][k] = max(dp[i][j][k], dp[i-1][k][l] + count_ones(j))
#    其中 j 不能與地形衝突，且 j, k, l 三個狀態之間不能有相同的位元為 1 (即不互相攻擊)。
#
# 複雜度：
# - 時間複雜度：O(N * V^3)，其中 V 是單行合法狀態的數量。當 M=10 時，V 最多 60。
# - 空間複雜度：O(N * V^2) 或更少。

def solve(n: int, m: int, grid: list[str]) -> int:
    """
    計算最多能部署的炮兵數量 (標準狀態壓縮 DP 解法)。
    """
    if n == 0 or m == 0:
        return 0
        
    # 預處理地形：把地形轉換為二進位遮罩。1 代表山地 (H)，0 代表平原 (P)
    # 這樣只要 (state & mountains[i]) != 0 就代表炮兵放在了山地上，這是不合法的。
    mountains = []
    for row in grid:
        mask = 0
        for i in range(m):
            if row[i] == 'H':
                mask |= (1 << i)
        mountains.append(mask)
        
    # 預處理所有單行合法的狀態 (左右不互相攻擊)
    valid_states = []
    state_counts = []
    for i in range(1 << m):
        if (i & (i << 1)) == 0 and (i & (i << 2)) == 0:
            valid_states.append(i)
            # 計算這個狀態放了幾個炮兵 (二進位中 1 的數量)
            state_counts.append(bin(i).count('1'))
            
    num_states = len(valid_states)
    
    # 建立 DP 陣列: dp[i][j][k]
    # i: 考慮到第 i 行 (0 ~ n-1)
    # j: 第 i 行的狀態索引 (0 ~ num_states-1)
    # k: 第 i-1 行的狀態索引 (0 ~ num_states-1)
    dp = [[[0] * num_states for _ in range(num_states)] for _ in range(n)]
    
    # Base Case: 第 0 行
    for j in range(num_states):
        if (valid_states[j] & mountains[0]) == 0:
            dp[0][j][0] = state_counts[j]
            
    # Base Case: 第 1 行 (如果有)
    if n > 1:
        for j in range(num_states):
            if (valid_states[j] & mountains[1]) != 0:
                continue
            for k in range(num_states):
                if (valid_states[k] & mountains[0]) != 0:
                    continue
                # 第 1 行與第 0 行不能互相攻擊
                if (valid_states[j] & valid_states[k]) == 0:
                    dp[1][j][k] = max(dp[1][j][k], dp[0][k][0] + state_counts[j])
                    
    # 狀態轉移: 第 2 行到第 n-1 行
    for i in range(2, n):
        for j in range(num_states):
            if (valid_states[j] & mountains[i]) != 0:
                continue
            for k in range(num_states):
                if (valid_states[k] & mountains[i-1]) != 0:
                    continue
                if (valid_states[j] & valid_states[k]) != 0:
                    continue
                for l in range(num_states):
                    if (valid_states[l] & mountains[i-2]) != 0:
                        continue
                    # 檢查這三行兩兩之間是否會互相攻擊
                    if (valid_states[j] & valid_states[l]) != 0:
                        continue
                    if (valid_states[k] & valid_states[l]) != 0:
                        continue
                        
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][k][l] + state_counts[j])
                    
    # 在最後一行中找出最大值
    ans = 0
    for j in range(num_states):
        for k in range(num_states):
            ans = max(ans, dp[n-1][j][k])
            
    return ans
