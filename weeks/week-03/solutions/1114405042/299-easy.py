# UVA 299: Train Swapping
# 簡單版 - 更容易記憶的寫法 (-easy)

def solve_easy(input_text):
    """
    用極簡短、更容易記憶的方式解決 UVA 299 火車車廂交換問題。
    """
    # 拆分所有數字
    tokens = input_text.split()
    if not tokens: return ""
    
    # 將所有輸入轉為整數，方便後續直接取值
    nums = [int(x) for x in tokens]
    
    n = nums[0]  # 測資數量
    idx = 1
    res = []
    
    for _ in range(n):
        l = nums[idx]  # 車廂數量
        idx += 1
        
        # 取得車廂陣列
        arr = nums[idx : idx + l]
        idx += l
        
        # 簡單暴力的雙層迴圈計算交換次數 (也就是找逆序對)
        swaps = 0
        for i in range(l):
            for j in range(i + 1, l):
                if arr[i] > arr[j]:
                    swaps += 1
                    
        # 直接使用 f-string 記錄結果
        res.append(f"Optimal train swapping takes {swaps} swaps.")
        
    return "\n".join(res)

if __name__ == '__main__':
    import sys
    data = sys.stdin.read()
    if data.strip():
        print(solve_easy(data))
