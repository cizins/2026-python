"""UVA 10008 Cryptanalysis - 簡單好記版 (-easy)。

解題口訣與核心技巧：
1. `sys.stdin.read().upper()`: 把所有輸入一次讀進來，全部轉成大寫。不用管第一行那個無聊的 N，反正數字不影響字母統計！
2. `[c for c in text if c.isupper()]`: 直接濾出所有是大寫字母的字元。
3. 靠 `.count(c)` 或者字典統計次數。
4. 排序神技：`sorted(資料, key=lambda x: (-x[1], x[0]))`。-x[1] 代表數量遞減，x[0] 代表字母遞增。
"""

import sys


def solve_from_text(text: str) -> str:
    """處理全部輸入，回傳答案。"""
    
    # 步驟 1 & 2：全部轉大寫，並挑出所有的 A-Z 字母
    # 注意：這裡刻意忽略第一行的 N，因為不管有沒有 N，都不會影響字母 A-Z 的統計。
    all_letters = [c for c in text.upper() if 'A' <= c <= 'Z']
    
    # 步驟 3：用一個字典(或直接用 set)來統計每個字母的出現次數
    counts = {}
    for letter in all_letters:
        counts[letter] = counts.get(letter, 0) + 1
        
    # 步驟 4：排序
    # counts.items() 會變成類似 [('A', 3), ('B', 1)] 的列表
    # key=lambda x: (-x[1], x[0]) 讓它先照數量遞減，再照字母遞增排
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 組合出最後要印出的格式
    answers = [f"{char} {count}" for char, count in sorted_items]
    return "\n".join(answers)


def main() -> None:
    """主程式進入點。"""
    print(solve_from_text(sys.stdin.read()))


if __name__ == "__main__":
    main()
