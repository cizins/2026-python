import sys

def solve(input_text):
    """
    UVA 299: Train Swapping (火車車廂調換) - 標準版
    
    核心概念：
    這題要求「相鄰車廂交換的最小次數」，這在數學/演算法上就是求「逆序數對 (Inversions)」的數量。
    逆序數對的意思是：在一個數列中，如果有兩個數字的相對順序是錯的 (前面的數字 > 後面的數字)，
    那它們就是一個逆序數對，必須交換 1 次才能排正。
    """
    # 由於題目測資的換行與空白可能不規律，使用 split() 可以自動忽略所有空白與換行，把所有「字(Token)」切成一個一維陣列
    tokens = input_text.split()
    if not tokens: 
        return ""
    
    # 讀取測試資料的總筆數 (N)
    n = int(tokens[0])
    idx = 1 # 紀錄目前讀到哪一個 token
    
    result = []
    
    # 處理每一筆測試資料
    for _ in range(n):
        if idx >= len(tokens):
            break
            
        # 讀取火車長度 L
        l = int(tokens[idx])
        idx += 1
        
        # 讀取 L 個車廂編號
        trains = []
        for _ in range(l):
            trains.append(int(tokens[idx]))
            idx += 1
            
        # 計算逆序數對的數量 (即最小交換次數)
        swaps = 0
        for i in range(l):
            for j in range(i + 1, l):
                # 如果前面的車廂號碼「大於」後面的車廂號碼，代表順序顛倒了
                if trains[i] > trains[j]:
                    swaps += 1
                    
        # 將結果加入結果陣列
        result.append(f"Optimal train swapping takes {swaps} swaps.")
        
    return "\n".join(result)

def main():
    # 讀取標準輸入，交給 solve 處理
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve(input_text))

if __name__ == "__main__":
    main()