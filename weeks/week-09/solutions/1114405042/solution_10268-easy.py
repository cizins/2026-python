# 解決 10268 (丟水球問題) - 手打簡易版
# 題意：有 k 個水球、n 層樓，求最少需丟幾次測出水球破的最低樓層。

def solve_10268_easy():
    import sys
    
    # 讀取標準輸入
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
            
        k = int(parts[0])
        if k == 0:
            break
        n = int(parts[1])
        
        if n == 0:
            print(0)
            continue
            
        # 簡易版的丟水球數學組合算法
        ans = "More than 63 trials needed."
        for t in range(1, 64):
            floors = 0
            c = 1
            # 計算組合數總和 Sum(C(t, i))，i 從 1 到 k
            for i in range(1, min(k, t) + 1):
                # 利用前一項快速計算組合數：C(t, i) = C(t, i-1) * (t - i + 1) / i
                c = c * (t - i + 1) // i
                floors += c
                
            # 若能測出的最高樓層大於等於 n，則 t 即為最小次數
            if floors >= n:
                ans = t
                break
                
        print(ans)

if __name__ == "__main__":
    solve_10268_easy()
