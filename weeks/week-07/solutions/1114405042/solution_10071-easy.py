# 這是更簡單、更容易記憶的寫法 (Easy version)
#
# 解題思路：
# 1. 題目要求尋找 a + b + c + d + e = f 的數量。
# 2. 將方程式改寫成 a + b + c = f - d - e，左右兩邊都是 3 個變數。
# 3. 在 Python 裡面，我們可以使用強大的標準函式庫 (Standard Library)：
#    - itertools.product：用來產生所有可能的排列組合（笛卡兒積）。
#    - collections.Counter：用來計算某個數值出現的次數。
# 4. 這樣只需要幾行程式碼就能寫完，這才是真正 Pythonic 的簡潔風格，面試中也能展示你對內建模組的熟悉程度！

from itertools import product
from collections import Counter

def solve_easy(n: int, s: list) -> int:
    """
    計算 a + b + c + d + e = f 的六元組數量。
    利用 itertools 與 collections 模組，大幅簡化程式碼。
    
    參數:
    n (int): 集合 S 的元素個數
    s (list): 集合 S，元素可以重複挑選
    
    回傳:
    int: 符合條件的六元組數量
    """
    # 步驟 1: 使用 product 產生 a, b, c 的所有可能組合，並立刻計算它們的總和。
    # 然後用 Counter 統計每個總和 (a+b+c) 出現過幾次。
    left_sums = Counter(a + b + c for a, b, c in product(s, repeat=3))
    
    # 步驟 2: 計算所有 f, d, e 組合中，目標值 (f - d - e) 有沒有在左邊的統計中出現。
    # 用 sum() 函數將所有的次數累加起來。
    ans = sum(left_sums[f - d - e] for f, d, e in product(s, repeat=3))
    
    return ans
