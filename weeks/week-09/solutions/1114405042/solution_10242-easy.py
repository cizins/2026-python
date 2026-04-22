# 解決 10242 (ATM搶劫路線最大化) - 手打簡易版
# 題意：找一條從起點到有酒吧的終點的路線，使經過的 ATM 金額總和最大（可重複經過，但錢只能拿一次）。
# 簡易手打法：Kosaraju's Algorithm 求強連通分量 (SCC)，然後做 DAG 上的 DP。

def solve_10242_easy():
    import sys
    sys.setrecursionlimit(200000)
    lines = sys.stdin.read().split()
    if not lines: return
    
    n = int(lines[0])
    m = int(lines[1])
    idx = 2
    
    # 建立正向與反向圖
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = int(lines[idx]), int(lines[idx+1])
        adj[u].append(v)
        rev_adj[v].append(u)
        idx += 2
        
    cash = [0] * (n + 1)
    for i in range(1, n + 1):
        cash[i] = int(lines[idx])
        idx += 1
        
    start_node = int(lines[idx])
    p = int(lines[idx+1])
    idx += 2
    
    bars = set()
    for _ in range(p):
        bars.add(int(lines[idx]))
        idx += 1
        
    # 第一步：正向 DFS 記錄離開順序
    visited = [False] * (n + 1)
    order = []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
            
    # 第二步：反向 DFS 找出 SCC (強連通分量)
    scc_id = [0] * (n + 1)
    scc_cash = []
    scc_has_bar = []
    current_scc = 0
    visited = [False] * (n + 1)
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = current_scc
        scc_cash[-1] += cash[u]
        if u in bars:
            scc_has_bar[-1] = True
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
                
    for i in reversed(order):
        if not visited[i]:
            scc_cash.append(0)
            scc_has_bar.append(False)
            dfs2(i)
            current_scc += 1
            
    # 第三步：縮點後建圖並計算 DP
    scc_adj = [[] for _ in range(current_scc)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_adj[scc_id[u]].append(scc_id[v])
                
    # 尋找最大金額
    memo = [-1] * current_scc
    def dp(u):
        if memo[u] != -1: return memo[u]
        
        max_val = 0
        for v in scc_adj[u]:
            res = dp(v)
            if res != -1: # 若後續能到達酒吧，才計入
                max_val = max(max_val, res)
                
        # 如果自己有酒吧，或後面能到達酒吧，就加上自己的錢
        if max_val > 0 or scc_has_bar[u]:
            memo[u] = max_val + scc_cash[u]
        else:
            memo[u] = -1 # 代表此路不通
            
        return memo[u]
        
    ans = dp(scc_id[start_node])
    print(max(0, ans))

if __name__ == '__main__':
    pass
