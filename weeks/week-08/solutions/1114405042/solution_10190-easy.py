import sys

def get_x(t: float, x0: int, l: int, v: int, W: int) -> float:
    """
    計算某把雨傘在時間 t 的左端點位置 x(t)。
    利用 Python 強大的 modulo (%) 處理負數的功能，可以極度簡潔地模擬往返運動。
    1. D 代表可以移動的最大距離 (W - l)。
    2. 把來回的反彈拉成直線 P (包含負數起點)。
    3. 取 2*D 的餘數，若大於 D 則反向計算。
    """
    D = W - l
    if D == 0: return 0.0  # 傘跟馬路一樣寬
    if v == 0: return float(x0) # 傘靜止不動
        
    S = abs(v)
    P0 = x0 if v > 0 else -x0 # 往左走相當於從對稱的負點出發
    
    P = P0 + S * t
    modP = P % (2 * D)
    
    if modP <= D:
        return float(modP)
    else:
        return float(2 * D - modP)

def get_U(t: float, umbrellas: list, W: int) -> float:
    """
    計算在時間 t 時，所有雨傘覆蓋的馬路總長度。
    """
    intervals = []
    for x0, l, v in umbrellas:
        x = get_x(t, x0, l, v, W)
        intervals.append((x, x + l))
        
    if not intervals: return 0.0
        
    intervals.sort()
    merged_len = 0.0
    curr_start, curr_end = intervals[0]
    
    for st, en in intervals[1:]:
        if st <= curr_end + 1e-9:
            curr_end = max(curr_end, en)
        else:
            merged_len += (curr_end - curr_start)
            curr_start, curr_end = st, en
            
    merged_len += (curr_end - curr_start)
    return merged_len

def solve_easy(input_data: str) -> str:
    """
    解題思路 (簡單容易記憶版 - 數值積分法 Numerical Integration)：
    1. 計算這題精確解(Event-Driven)需要複雜的線段交錯與碰撞推導，容易寫錯。
    2. 觀察題目只要求精確到小數點後第二位，而且 T, v 等物理量是連續變化的。
    3. 我們可以直接把時間 [0, T] 切成非常多份 (例如 10,000 份以上)。
    4. 使用梯形公式 (Trapezoidal Rule) 計算面積。只要切得夠細，誤差會遠小於 0.01。
    5. 這種解法極度容易記憶，且適用於絕大多數連續函數的物理競程題目。
    """
    lines = input_data.strip().split('\n')
    if not lines or not lines[0]: return ""
        
    idx = 0
    results = []
    
    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
            
        parts = line.split()
        if len(parts) < 4:
            idx += 1
            continue
            
        N, W, T, V = int(parts[0]), int(parts[1]), int(parts[2]), float(parts[3])
        idx += 1
        
        umbrellas = []
        for _ in range(N):
            u_parts = lines[idx].strip().split()
            umbrellas.append((int(u_parts[0]), int(u_parts[1]), int(u_parts[2])))
            idx += 1
            
        # 切割成 10000 個微小時間段，確保數值積分的誤差趨近於 0
        # 如果 T 非常大可以動態調整 steps，這裡固定最少 1 萬步
        steps = max(10000, int(T * 100))
        if T == 0:
            integral = 0.0
        else:
            dt = T / steps
            integral = 0.0
            
            # 使用梯形公式近似積分
            u_prev = get_U(0, umbrellas, W)
            for i in range(1, steps + 1):
                t = i * dt
                u_curr = get_U(t, umbrellas, W)
                # 梯形面積 = (上底 + 下底) * 高 / 2
                integral += (u_prev + u_curr) * 0.5 * dt
                u_prev = u_curr
                
        rain_vol = (W * T - integral) * V
        results.append(f"{rain_vol:.2f}")
        
    return "\n".join(results)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_easy(input_text))
