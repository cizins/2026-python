# UVA 299: Train Swapping
# 標準解法 - 模組化與型別提示

def solve_train_swapping(input_text: str) -> str:
    """
    處理 UVA 299 Train Swapping (火車車廂置換) 的核心函式。
    
    題目要求計算將一個序列透過「相鄰交換」排序成遞增序列所需的最少交換次數。
    這個次數在數學上等價於計算序列中的「逆序對 (Inversion)」數量。
    
    參數:
        input_text (str): 包含所有輸入測資的完整字串。
        
    回傳:
        str: 每組測資的答案，格式為 "Optimal train swapping takes S swaps."
    """
    # 透過空白字元 (空格、換行等) 將字串分割成 token 列表
    # 這樣可以忽略輸入中多餘的空白或換行
    tokens = input_text.split()
    if not tokens:
        return ""
        
    # 第一個數字代表總測資數量
    n = int(tokens[0])
    idx = 1
    results = []
    
    # 處理每一組測資
    for _ in range(n):
        if idx >= len(tokens):
            break
            
        # 取得這組測資的火車車廂數量 L
        l = int(tokens[idx])
        idx += 1
        
        # 讀取這 L 個車廂的當前順序
        trains = []
        for _ in range(l):
            trains.append(int(tokens[idx]))
            idx += 1
            
        # 計算最少交換次數 (也就是逆序對數量)
        # 對於陣列中的每一對 (i, j) 且 i < j，如果 trains[i] > trains[j]
        # 代表這兩個數字順序不對，需要透過一次相鄰交換來處理
        swaps = 0
        for i in range(l):
            for j in range(i + 1, l):
                if trains[i] > trains[j]:
                    swaps += 1
                    
        # 格式化輸出並加入結果列表中
        results.append(f"Optimal train swapping takes {swaps} swaps.")
        
    return "\n".join(results)

if __name__ == '__main__':
    import sys
    # 從標準輸入讀取全部資料
    input_data = sys.stdin.read()
    if input_data.strip():
        print(solve_train_swapping(input_data))
