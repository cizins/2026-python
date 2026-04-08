# 題目 10071：找出符合 a + b + c + d + e = f 的六元組數量
#
# 題意：
# 給定一個包含 N 個相異整數的集合 S (1 <= N <= 100)。
# 找出有多少組 (a, b, c, d, e, f) 滿足 a + b + c + d + e = f。
# 其中 a, b, c, d, e, f 必須來自集合 S，且可以重複挑選。
#
# 解法 (Meet in the middle / 中途相遇法)：
# 原式：a + b + c + d + e = f
# 可以改寫為：a + b + c = f - d - e
# 由於 N 最大為 100，如果我們直接窮舉 6 個變數，時間複雜度為 O(N^6) = 100^6，一定會超時。
# 如果我們將方程式分為左右兩邊，分別計算：
# 左邊：L = a + b + c ，有 N^3 種組合。
# 右邊：R = f - d - e ，也有 N^3 種組合。
# 這樣我們只需要 O(N^3) 的時間複雜度。N^3 = 1,000,000，可以在一秒內算完。
# 
# 我們可以使用一個雜湊表 (Hash Map / dict) 來記錄左邊 (a+b+c) 所有可能出現的數值以及其出現次數。
# 然後再窮舉右邊 (f-d-e) 的所有可能數值，如果這個數值有在雜湊表中出現過，
# 就將其出現次數加到總和中。

def solve(n: int, s: list) -> int:
    """
    計算 a + b + c + d + e = f 的六元組數量。
    使用中途相遇法 (Meet-in-the-Middle) 將複雜度降至 O(N^3)。
    
    :param n: 集合 S 的元素個數
    :param s: 包含集合 S 元素的串列
    :return: 符合條件的六元組數量
    """
    # 使用字典 (dict) 記錄左邊 a + b + c 所有可能總和的出現次數
    left_counts = {}
    
    # 窮舉 a, b, c (時間複雜度 O(N^3))
    for a in s:
        for b in s:
            for c in s:
                val = a + b + c
                if val in left_counts:
                    left_counts[val] += 1
                else:
                    left_counts[val] = 1
                    
    ans = 0
    # 窮舉 f, d, e (時間複雜度 O(N^3))
    # 若 f - d - e 的值存在於 left_counts 中，代表找到符合的組合
    for f in s:
        for d in s:
            for e in s:
                target = f - d - e
                if target in left_counts:
                    ans += left_counts[target]
                    
    return ans
