"""UVA 10008 Cryptanalysis - 標準版。

題目要求：
1. 讀取一個數字 n，代表接下來有 n 行文字。
2. 統計這 n 行文字中所有英文字母出現的次數（不分大小寫，統一視為大寫）。
3. 按照「出現次數由大到小」排序。
4. 如果次數相同，則按照「字母順序由小到大 (A 到 Z)」排序。
"""

import sys
from collections import Counter


def solve_from_text(text: str) -> str:
    """處理多行輸入文字，回傳格式化後的答案字串。"""
    lines = text.splitlines()
    if not lines:
        return ""
        
    try:
        # 第一行是句子數量 n
        n = int(lines[0].strip())
    except ValueError:
        return ""
        
    # 把接下來的 n 行文字全部接在一起，並轉成大寫
    content = "".join(lines[1:1+n]).upper()
    
    # 使用 Counter 來計算所有是英文字母 (isalpha) 的字元出現次數
    counter = Counter(c for c in content if c.isalpha())
    if not counter:
        return ""
        
    # Python 的 sorted 函數非常強大，我們可以傳入一個 tuple 作為排序依據(key)：
    # key=lambda x: (-x[1], x[0]) 
    # x 是一個 tuple，例如 ('A', 5) 代表字母 'A' 出現 5 次。x[0] 是字母，x[1] 是次數。
    # 1. -x[1]：次數取負數，原本次數越多(如 5)，負數就越小(-5)，因此會排在越前面（達到由大到小排序的效果）。
    # 2. x[0]：當次數相同時，比較字母本身，'A' 小於 'B'，所以 A 排在前面（達到字典序由小到大排序的效果）。
    sorted_counts = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    # 把結果格式化成 "字母 次數" 的形式，並用換行符號連接
    return "\n".join(f"{char} {count}" for char, count in sorted_counts)


def main() -> None:
    """主程式進入點，讀取標準輸入並印出答案。"""
    data = sys.stdin.read()
    print(solve_from_text(data))


if __name__ == "__main__":
    main()
