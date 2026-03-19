# UVA 100: The 3n + 1 problem
# 簡單版 - 更容易記憶的寫法 (-easy)

# 先在全域建立一個字典做快取，避免重複計算
memo = {1: 1}

def cycle_len(n):
    """計算並回傳單一數字的 cycle_length"""
    if n in memo:
        return memo[n]
    
    # 根據奇偶數決定下一個數字
    # 並用遞迴計算長度
    if n % 2 == 1:
        length = 1 + cycle_len(3 * n + 1)
    else:
        length = 1 + cycle_len(n // 2)
        
    memo[n] = length
    return length

def solve_easy(input_text):
    """用極簡短的方式解決 UVA 100 問題"""
    tokens = input_text.split()
    if not tokens: return ""
    
    res = []
    # 每次取兩個數字
    for i in range(0, len(tokens)-1, 2):
        u, v = int(tokens[i]), int(tokens[i+1])
        
        # 找出區間的最大最小值
        start, end = min(u, v), max(u, v)
        
        # 使用生成式與 max 快速找出區間內的最大 cycle length
        max_c = max(cycle_len(x) for x in range(start, end + 1))
        
        # 記得輸出時要使用原始順序的 u, v
        res.append(f"{u} {v} {max_c}")
        
    return "\n".join(res)

if __name__ == '__main__':
    import sys
    data = sys.stdin.read()
    if data.strip():
        print(solve_easy(data))
