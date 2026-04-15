import sys
import math

def get_x(t: float, x0: int, l: int, v: int, W: int) -> float:
    """
    計算某把雨傘在時間 t 的左端點位置 x(t)。
    利用 Python 的 modulo (%) 特性，可以完美模擬往返運動 (三角波)。
    """
    D = W - l
    if D == 0:
        return 0.0  # 雨傘寬度等於馬路，不會移動
    if v == 0:
        return float(x0)
        
    S = abs(v)
    # 如果初始向左移動，相當於從 -x0 開始向右移動
    P0 = x0 if v > 0 else -x0
    
    P = P0 + S * t
    modP = P % (2 * D)
    
    # 判斷是處於向右還是向左的週期
    if modP <= D:
        return float(modP)
    else:
        return float(2 * D - modP)

def get_U(t: float, umbrellas: list, W: int) -> float:
    """
    計算在時間 t 時，所有雨傘覆蓋的馬路總長度。
    這是一個經典的「區間聯集長度」問題。
    """
    intervals = []
    for x0, l, v in umbrellas:
        x = get_x(t, x0, l, v, W)
        intervals.append((x, x + l))
        
    if not intervals:
        return 0.0
        
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

def solve(input_data: str) -> str:
    """
    解題思路 (標準精確版 - 事件掃描法 Event-Driven)
    1. 每一把傘在馬路上來回移動，其位置 x(t) 是一條折線 (Piecewise Linear)。
    2. 如果我們找出所有傘「撞到牆壁 (反彈)」的時間點，在這些時間點之間的區間，所有傘的軌跡都是直線。
    3. 在這些純直線區間內，任何兩把傘的相對位置交錯 (例如重疊、包含) 都只會發生在特定交點。
    4. 找出所有的關鍵時間點 (反彈點 + 軌跡交點)，將 [0, T] 切割成若干個小區間。
    5. 在每個小區間 [tk, tk+1] 內，傘的覆蓋長度 U(t) 會是完美的線性函數！
    6. 因此我們可以直接使用梯形公式 (Trapezoidal Rule) 精確算出積分，完全沒有誤差。
    """
    lines = input_data.strip().split('\n')
    if not lines or not lines[0]:
        return ""
        
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
            
        N = int(parts[0])
        W = int(parts[1])
        T = int(parts[2])
        V = float(parts[3])
        idx += 1
        
        umbrellas = []
        for _ in range(N):
            u_parts = lines[idx].strip().split()
            umbrellas.append((int(u_parts[0]), int(u_parts[1]), int(u_parts[2])))
            idx += 1
            
        # 1. 收集所有「反彈 (撞牆)」的時間點
        bounce_times = [0.0, float(T)]
        for x0, l, v in umbrellas:
            D = W - l
            if D == 0 or v == 0:
                continue
            S = abs(v)
            P0 = x0 if v > 0 else -x0
            # 尋找所有 k 使得 0 <= t = (k*D - P0) / S <= T
            k_min = math.ceil(P0 / D)
            k_max = math.floor((T * S + P0) / D)
            for k in range(k_min, k_max + 1):
                t = (k * D - P0) / S
                if 0 <= t <= T:
                    bounce_times.append(t)
                    
        # 去除重複的反彈時間
        bounce_times = sorted(list(set(round(t, 7) for t in bounce_times)))
        
        event_times = list(bounce_times)
        
        # 2. 在每個反彈區間內，尋找傘與傘之間的「交錯」時間點
        for m in range(len(bounce_times) - 1):
            t1, t2 = bounce_times[m], bounce_times[m+1]
            if t2 - t1 < 1e-9:
                continue
                
            # 取得每把傘在該區間的直線方程式 x(t) = a + b*t
            # 為了避免浮點數誤差，直接用頭尾兩點計算斜率與截距
            line_eqs = []
            for x0, l, v in umbrellas:
                x_start = get_x(t1, x0, l, v, W)
                x_end = get_x(t2, x0, l, v, W)
                slope = (x_end - x_start) / (t2 - t1)
                intercept = x_start - slope * t1
                line_eqs.append((slope, intercept, l))
                
            # 窮舉任意兩把傘的交錯點
            for i in range(N):
                for j in range(i + 1, N):
                    bi, ai, li = line_eqs[i]
                    bj, aj, lj = line_eqs[j]
                    
                    # 傘邊界的交錯只發生在 x_i(t) - x_j(t) 等於以下四種常數 C 時
                    for C in [0, lj - li, -li, lj]:
                        # (bi - bj) * t = C - ai + aj
                        if abs(bi - bj) > 1e-9:
                            t_cross = (C - ai + aj) / (bi - bj)
                            # 如果交錯點在區間內部，則加入事件列表
                            if t1 < t_cross < t2:
                                event_times.append(t_cross)
                                
        # 將所有事件點排序去重
        event_times = sorted(list(set(round(t, 7) for t in event_times)))
        
        # 3. 完美積分
        integral_U = 0.0
        for k in range(len(event_times) - 1):
            tk = event_times[k]
            tk1 = event_times[k+1]
            if tk1 - tk < 1e-9:
                continue
            u1 = get_U(tk, umbrellas, W)
            u2 = get_U(tk1, umbrellas, W)
            # 因為 U(t) 在區間內是完全線性的，梯形公式就是精確解
            integral_U += (u1 + u2) * 0.5 * (tk1 - tk)
            
        # 馬路總面積扣除傘遮蔽的面積，再乘上降雨量 V
        rain_vol = (W * T - integral_U) * V
        results.append(f"{rain_vol:.2f}")
        
    return "\n".join(results)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve(input_text))
