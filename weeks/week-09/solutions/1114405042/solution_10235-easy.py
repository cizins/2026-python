# 解決 10235 (插座與蛇的方格放置問題) - 手打簡易版
# 題意：在 N*M 的網格中放置多個迴圈(蛇)，不能經過插座，求方法數。
# 這題標準解法是輪廓線 DP (Plug DP/插頭 DP)，但在考場上手打簡易版
# 可以寫成帶有記憶化搜索 (Memoization) 的 DFS，雖然效能較差但容易記憶。

def solve_10235_easy():
    # 簡易版的 DFS 框架（考場背誦用）
    # 注意：這裡只提供邏輯框架，完整插頭 DP 狀態壓縮較長。
    import sys
    lines = sys.stdin.read().split()
    if not lines: return
    
    T = int(lines[0])
    idx = 1
    
    for case_num in range(1, T + 1):
        N = int(lines[idx])
        M = int(lines[idx+1])
        idx += 2
        
        grid = []
        for _ in range(N):
            grid.append([int(x) for x in lines[idx:idx+M]])
            idx += M
            
        # memo 用於記憶化搜索，記錄 (格子座標, 輪廓線狀態) 對應的放置方法數
        memo = {}
        MOD = 1000000007
        
        def dfs(r, c, state):
            # 走到底部，如果狀態是全空的表示這是一種合法的封閉迴圈擺法
            if r == N:
                return 1 if state == 0 else 0
                
            # 換行
            if c == M:
                # 換行時，最右邊的插頭不能延伸到下一行的最左邊
                if state & (1 << M): return 0
                return dfs(r + 1, 0, state << 1)
                
            state_key = (r, c, state)
            if state_key in memo:
                return memo[state_key]
                
            res = 0
            # 取出左邊跟上面的插頭狀態 (1表示有線連過來)
            left = (state >> c) & 1
            up = (state >> (c + 1)) & 1
            
            # grid[r][c] == 0 代表有插座（障礙物），不能放蛇
            if grid[r][c] == 0:
                if left == 0 and up == 0:
                    res = dfs(r, c + 1, state)
            else:
                # 簡單的情況分支 (不包含連通性檢查的簡化版)
                if left == 0 and up == 0:
                    # 放入一個右下拐角，產生兩個新插頭
                    res = dfs(r, c + 1, state | (1 << c) | (1 << (c + 1)))
                elif left == 1 and up == 1:
                    # 兩個插頭匯合，消除這兩個插頭
                    res = dfs(r, c + 1, state ^ (1 << c) ^ (1 << (c + 1)))
                else:
                    # 一個插頭延伸，可以往下或往右
                    # 往下
                    res = (res + dfs(r, c + 1, state | (1 << c) & ~(1 << (c + 1)))) % MOD
                    # 往右
                    res = (res + dfs(r, c + 1, state | (1 << (c + 1)) & ~(1 << c))) % MOD
                    
            memo[state_key] = res % MOD
            return memo[state_key]
            
        ans = dfs(0, 0, 0)
        print(f"Case {case_num}: {ans}")

if __name__ == '__main__':
    pass # 實際執行時可呼叫 solve_10235_easy()
