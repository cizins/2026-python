import sys
import math

def solve_easy(input_data: str) -> str:
    """
    解題思路 (簡單、容易記憶版)：
    1. 這題主要是單位轉換的細節和 Python `math` 套件的運用。
    2. 先用一行 if-else 將角度統統轉換成 degree。
    3. 利用 % 360 和 min(deg, 360 - deg) 極度簡化「尋找最短夾角」的判斷邏輯。
    4. 用 f-string 直接回傳計算結果，減少變數的宣告，讓程式碼保持乾淨。
    """
    results = []
    # 逐行讀取處理
    for line in input_data.strip().split('\n'):
        if not line.strip(): 
            continue
            
        # unpack 解析出三筆參數
        s_str, a_str, unit = line.split()
        
        # 算出與地球中心的距離 (總半徑)
        r = 6440.0 + float(s_str)
        
        # 轉換單位為度數 (如果是 min 就除以 60)
        deg = float(a_str) / 60.0 if unit == 'min' else float(a_str)
        
        # 縮減到 360 度以內，並取兩衛星之間的「最短」夾角
        deg = deg % 360.0
        deg = min(deg, 360.0 - deg)
            
        # 轉換為弧度
        rad = math.radians(deg)
        
        # 弧長 = 半徑 * 弧度
        # 弦長 = 2 * 半徑 * sin(弧度/2)
        results.append(f"{r * rad:.6f} {2.0 * r * math.sin(rad / 2.0):.6f}")
        
    return '\n'.join(results)

if __name__ == "__main__":
    # 從標準輸入讀取測試資料
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_easy(input_text))
