# 解決 UVA 10268 (丟水球問題) 的 Python 程式
# 題意：給定 k 個水球與 n 層樓，求最少需要丟幾次才能測出水球破掉的樓層。
# 若超過 63 次，則輸出 "More than 63 trials needed."

def solve_water_balloons(k, n):
    """
    計算最少需要的測試次數。
    使用組合數學的概念，t 次測試、k 個水球最多可以測出的樓層數為：
    Sum_{i=1}^{k} C(t, i)
    """
    if n == 0:
        return 0
        
    for t in range(1, 64):
        max_floors = 0
        comb = 1
        # 計算組合數總和
        for i in range(1, min(k, t) + 1):
            comb = comb * (t - i + 1) // i
            max_floors += comb
            # 如果可測出的樓層數已經大於等於 n，代表 t 次就足夠了
            if max_floors >= n:
                return t
                
    return "More than 63 trials needed."

if __name__ == "__main__":
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
        print(solve_water_balloons(k, n))
