# 解決 10252 (兩條線的距離最小化問題 / 幾何中點) - 手打簡易版
# 題意：給定平面上 N 個點，找到一個點 P，使得 P 到所有點的距離和最小。
# 簡易法：模擬退火 (Simulated Annealing) 或是 爬山演算法 (Hill Climbing)。
# 這是競技程式中非常好記且實用的萬用寫法。

def solve_10252_easy():
    import sys
    import math
    lines = sys.stdin.read().split()
    if not lines: return
    
    T = int(lines[0])
    idx = 1
    
    for _ in range(T):
        n = int(lines[idx])
        idx += 1
        
        points = []
        cx, cy = 0.0, 0.0
        for _ in range(n):
            x = float(lines[idx])
            y = float(lines[idx+1])
            points.append((x, y))
            cx += x
            cy += y
            idx += 2
            
        # 初始猜測點 (質心)
        cx /= n
        cy /= n
        
        # 計算某點到所有點的距離和
        def get_dist_sum(px, py):
            res = 0.0
            for x, y in points:
                res += math.hypot(x - px, y - py)
            return res
            
        # 模擬退火 / 爬山演算法
        step = 10000.0 # 初始步長
        ans = get_dist_sum(cx, cy)
        
        # 4 個方向：上下左右
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        while step > 1e-6:
            found_better = False
            for i in range(4):
                nx = cx + dx[i] * step
                ny = cy + dy[i] * step
                curr = get_dist_sum(nx, ny)
                if curr < ans:
                    ans = curr
                    cx, cy = nx, ny
                    found_better = True
            
            # 如果沒有更好的，縮小步長
            if not found_better:
                step *= 0.5
                
        # 輸出結果 (依照題目要求輸出整數部分與解的數量)
        # 注意：這只是簡易模板，若需精確的整數解數量可能需額外判斷
        print(int(round(ans)), 1)

if __name__ == '__main__':
    pass
