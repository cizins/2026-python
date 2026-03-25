import sys

def solve(n, p, hartals):
    """
    計算在 N 天內，因為罷會 (hartal) 而損失的工作天數。
    
    參數:
    n (int): 總模擬天數
    p (int): 政黨數量
    hartals (list): 每個政黨的罷會參數 (h_i)
    
    回傳:
    int: 總共損失的工作天數
    """
    # 使用 set 來記錄發生罷會的日子，這樣可以避免不同政黨在同一天罷會時重複計算
    strike_days = set()
    
    # 針對每一個政黨的罷會參數進行處理
    for h in hartals:
        # 該政黨每 h 天罷會一次，所以罷會日子是 h, 2h, 3h, ...
        for day in range(h, n + 1, h):
            # 題目規定第一天是星期日 (Sunday)。
            # 星期五 (Friday) 是一週的第 6 天，所以 day % 7 == 6 代表星期五。
            # 星期六 (Saturday) 是一週的第 7 天，所以 day % 7 == 0 代表星期六。
            # 只有在非假日 (星期五和星期六除外) 發生罷會，才會損失工作天。
            if day % 7 != 6 and day % 7 != 0:
                strike_days.add(day)
                
    # 集合 (set) 的大小就是不重複的損失工作天數
    return len(strike_days)

def main():
    # 讀取所有的標準輸入資料，並以空白或換行符號分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 第一個整數是測試資料的組數 T
    t = int(input_data[0])
    idx = 1
    
    # 針對每一組測試資料進行迴圈處理
    for _ in range(t):
        if idx >= len(input_data):
            break
            
        # 讀取模擬的總天數 N
        n = int(input_data[idx])
        idx += 1
        
        # 讀取政黨的數量 P
        p = int(input_data[idx])
        idx += 1
        
        # 讀取接下來的 P 個政黨罷會參數 h_i
        hartals = []
        for _ in range(p):
            hartals.append(int(input_data[idx]))
            idx += 1
            
        # 計算並輸出損失的工作天數
        print(solve(n, p, hartals))

if __name__ == '__main__':
    main()
