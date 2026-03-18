"""UVA 10038 Jolly Jumpers - 標準版。

題目定義：
一個長度為 n 的整數序列，如果相鄰元素的「絕對差值」剛好涵蓋了 1 到 n-1 的所有整數，
我們就稱這個序列為 Jolly Jumper。
例如：4 1 4 2 3
相鄰差值的絕對值分別為 |1-4|=3, |4-2|=2, |2-3|=1。
包含了 1, 2, 3 (即 1 到 4-1)，所以是 Jolly。
"""

import sys


def is_jolly(nums: list[int]) -> bool:
    """判斷一串數字是否為 Jolly Jumper。"""
    if not nums:
        return False
        
    n = nums[0]  # 第一個數字代表序列長度
    
    # 防呆機制：確保後面給的數字數量符合 n
    if len(nums) - 1 < n:
        return False
        
    # 取出真正的序列部份
    sequence = nums[1:1+n]
    
    # 建立一個集合(Set)，用來存放所有算出來的「絕對差值」
    diffs = set()
    for i in range(1, n):
        # 計算相鄰兩項的絕對差值，並加入集合中
        diff = abs(sequence[i] - sequence[i-1])
        diffs.add(diff)
        
    # 建立一個包含 1 到 n-1 的標準集合
    expected = set(range(1, n))
    
    # 如果算出來的差值集合，跟標準集合一模一樣，就是 Jolly
    return diffs == expected


def solve_from_text(text: str) -> str:
    """處理多行輸入文字，轉換成輸出文字。"""
    lines = text.strip().splitlines()
    outputs = []
    
    for line in lines:
        parts = line.split()
        if not parts:
            continue
            
        try:
            # 把字串陣列轉換成整數陣列
            nums = [int(p) for p in parts]
            
            # 判斷並輸出結果
            if is_jolly(nums):
                outputs.append("Jolly")
            else:
                outputs.append("Not jolly")
        except ValueError:
            # 遇到無法轉成整數的無效行就跳過
            continue
            
    return "\n".join(outputs)


def main() -> None:
    """主程式進入點，讀取標準輸入並印出答案。"""
    data = sys.stdin.read()
    print(solve_from_text(data))


if __name__ == "__main__":
    main()
