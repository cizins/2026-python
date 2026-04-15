import sys
import math

def solve(input_data: str) -> str:
    """
    解題思路 (標準版)：
    1. 讀取輸入資料，解析出高度 s、角度 a、以及單位 (min 或 deg)。
    2. 地球半徑為固定的 6440 公里，所以衛星到地心的距離 r = 6440 + s。
    3. 將角度統一轉換為「度 (degree)」。如果是 'min'，則除以 60。
    4. 【關鍵陷阱】：若給定的角度超過 180 度，我們必須取較小的夾角來計算最短距離，
       即 angle = 360 - angle (需先將 angle 取 360 的餘數，防止超過 360 度的怪異輸入)。
    5. 將角度轉換為弧度 (radians) 以便呼叫 math 函式庫。
    6. 代入公式計算弧長 (Arc) = r * rad，以及弦長 (Chord) = 2 * r * sin(rad / 2)。
    7. 輸出結果並保留小數點後 6 位。
    """
    lines = input_data.strip().split('\n')
    results = []
    for line in lines:
        if not line.strip():
            continue
            
        parts = line.split()
        if len(parts) < 3:
            continue
            
        s = float(parts[0])
        a = float(parts[1])
        unit = parts[2]
        
        # 衛星到地心的總半徑
        r = 6440.0 + s
        
        # 單位轉換 (60分 = 1度)
        if unit == 'min':
            a = a / 60.0
            
        # 將角度限制在 0 ~ 360 之間
        a = a % 360.0
        
        # 取較小的夾角計算最短路徑
        if a > 180.0:
            a = 360.0 - a
            
        # 轉換為弧度
        rad = math.radians(a)
        
        # 弧長公式：半徑 * 弧度
        arc_len = r * rad
        # 弦長公式：利用等腰三角形與半角公式推導 (2 * r * sin(theta/2))
        chord_len = 2.0 * r * math.sin(rad / 2.0)
        
        # 格式化輸出小數點後 6 位
        results.append(f"{arc_len:.6f} {chord_len:.6f}")
        
    return "\n".join(results)

if __name__ == "__main__":
    # 若直接執行此檔案，從標準輸入讀取資料並輸出結果 (支援 OJ)
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve(input_text))
