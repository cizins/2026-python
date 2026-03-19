# UVA 100: The 3n + 1 problem
# 標準版 - 模組化與記憶化設計 (Memoization)

def solve_3n_plus_1(input_text: str) -> str:
    """
    處理 UVA 100 The 3n + 1 problem 的核心函式。
    
    使用字典 (memo) 來快取已經計算過的 cycle_length，
    這樣遇到重複數字時可以直接回傳，大幅加快運算速度。
    
    參數:
        input_text (str): 包含所有輸入測資的字串。
        
    回傳:
        str: 依照題目要求格式輸出的結果。
    """
    tokens = input_text.split()
    if not tokens:
        return ""
        
    # 初始化一個全域字典用來做記憶化 (Memoization)
    # 將已知的基礎狀態 1 加入字典中，長度為 1
    memo = {1: 1}
    
    def get_cycle_length(n: int) -> int:
        """計算給定數字 n 的 cycle_length"""
        # 如果曾經計算過這個數字，直接從字典中回傳
        if n in memo:
            return memo[n]
            
        # 依照規則計算下一個數字
        if n % 2 != 0:
            next_n = 3 * n + 1
        else:
            next_n = n // 2
            
        # 遞迴計算後續長度，加上當前數字這一步 (+1)
        length = 1 + get_cycle_length(next_n)
        
        # 記錄結果到字典中，以供未來使用
        memo[n] = length
        return length

    results = []
    # 每兩個數字一組進行處理
    for i in range(0, len(tokens) - 1, 2):
        orig_i = int(tokens[i])
        orig_j = int(tokens[i+1])
        
        # 題目陷阱：輸入的 i 和 j 可能不是由小到大排序的
        # 所以必須先找出真正的起點和終點
        start = min(orig_i, orig_j)
        end = max(orig_i, orig_j)
        
        max_len = 0
        # 走訪區間內所有的數字 [start, end]
        for num in range(start, end + 1):
            curr_len = get_cycle_length(num)
            if curr_len > max_len:
                max_len = curr_len
                
        # 依照題目要求，輸出順序必須和原本輸入的 i, j 一致
        results.append(f"{orig_i} {orig_j} {max_len}")
        
    return "\n".join(results)

if __name__ == '__main__':
    import sys
    # 從標準輸入讀取資料
    input_data = sys.stdin.read()
    if input_data.strip():
        print(solve_3n_plus_1(input_data))
