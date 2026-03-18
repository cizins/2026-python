"""UVA 10038 Jolly Jumpers - 簡單好記版 (-easy)。

解題口訣與核心技巧：
1. `zip(seq, seq[1:])`：這是 Python 的神招，可以一次抓出「前後相鄰」的兩個數字。
2. 用 `{abs(a - b) for a, b in ...}` (集合推導式) 一口氣算完所有差值並去除重複。
3. 最後直接比較 `算出的集合 == set(range(1, n))`。

不到五行，邏輯清晰、不會有 index out of bounds 的問題！
"""

import sys


def solve_from_text(text: str) -> str:
    """處理輸入字串，回傳對應的解答。"""
    answers = []
    
    # 逐行讀取
    for line in text.strip().splitlines():
        # 把這一行用空白切開，全部轉成整數
        nums = [int(x) for x in line.split()]
        if not nums:
            continue
            
        n = nums[0]        # 第一個是數量 n
        seq = nums[1:n+1]  # 後面是真正的數列
        
        # 核心：用 zip(seq, seq[1:]) 兩兩抓出來相減取絕對值，放進集合(set)
        diffs = {abs(a - b) for a, b in zip(seq, seq[1:])}
        
        # 判斷是否剛好等於 {1, 2, ..., n-1}
        if diffs == set(range(1, n)):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")
            
    return "\n".join(answers)


def main() -> None:
    """主程式進入點，讀取標準輸入並輸出結果。"""
    print(solve_from_text(sys.stdin.read()))


if __name__ == "__main__":
    main()
