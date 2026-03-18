"""UVA 10035 Primary Arithmetic - 簡單好記版 (-easy)。

解題口訣與核心技巧：
遇到直式加法問題，最不容易出錯的寫法就是「當成數字處理」。

口訣只有兩句：
1. `n % 10`：抓出最後一個數字（個位數）。
2. `n //= 10`：砍掉最後一個數字，把前面的數字往右退一位。

一直重複這個動作到數字變成 0 為止，
只要兩個個位數加上 `carry` 大於等於 10，就記 1 次進位。
這樣就完全不用管字串長度、補零跟倒轉了！
"""

import sys


def count_carries_easy(a: int, b: int) -> int:
    """計算兩個數字在直式加法時的進位次數。"""
    carries = 0  # 總計進位的次數
    carry = 0    # 目前有沒有進位 (只能是 0 或 1)
    
    # 只要 a 還有數字，或者 b 還有數字，或者手上還有進位沒加上去，就繼續算
    while a > 0 or b > 0 or carry > 0:
        
        # 抓出 a 跟 b 目前最後一個數字 (個位數)，加上上一回的進位
        current_sum = (a % 10) + (b % 10) + carry
        
        if current_sum >= 10:
            carries += 1
            carry = 1   # 下一次要加上進位的 1
        else:
            carry = 0   # 數字不夠大，沒有進位
            
        # 算完了這一位，把它砍掉，讓十位數變成新的個位數
        a //= 10
        b //= 10
        
    return carries


def solve_from_text(text: str) -> str:
    """處理輸入文字，轉換成輸出文字。"""
    lines = text.strip().splitlines()
    answers = []
    
    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
            
        # 把讀進來的字串轉換成整數
        a, b = int(parts[0]), int(parts[1])
        
        # 如果兩者都是 0，代表輸入結束
        if a == 0 and b == 0:
            break
            
        carries = count_carries_easy(a, b)
        
        # 判斷結果文字 (0 次、1 次、多次)
        if carries == 0:
            answers.append("No carry operation.")
        elif carries == 1:
            answers.append("1 carry operation.")
        else:
            answers.append(f"{carries} carry operations.")
            
    return "\n".join(answers)


def main() -> None:
    """主程式進入點，讀取標準輸入並印出答案。"""
    print(solve_from_text(sys.stdin.read()))


if __name__ == "__main__":
    main()
