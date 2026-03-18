"""UVA 10019 Funny Encryption Method - 簡單好記版 (-easy)。

解題口訣與核心技巧：
1. 數字字串 s 不管當作什麼進位，只要用 int(s, base) 就可以轉成真實的整數。
   - 當十進位：int(s, 10) 或是直接 int(s)
   - 當十六進位：int(s, 16)
2. 整數轉二進位用 bin()。
3. 算 '1' 的數量直接用字串方法 .count('1')。

所以：
b1 = bin(int(s)).count('1')
b2 = bin(int(s, 16)).count('1')
短短兩句就可以搞定！
"""
import sys

def solve_from_text(text: str) -> str:
    """處理包含多行測試資料的文字。"""
    
    # splitlines() 可以把文字拆成一行一行
    # 我們忽略第一行(測資數量)，只取後面的數字字串
    lines = [line.strip() for line in text.splitlines()[1:] if line.strip()]

    answers = []
    
    # 逐一處理每一個數字字串
    for s in lines:
        # 步驟 1：把字串 s 當成一般「十進位」，轉二進位後算 '1' 有幾個
        b1 = bin(int(s)).count('1')

        # 步驟 2：把字串 s 當成「十六進位」，轉二進位後算 '1' 有幾個
        b2 = bin(int(s, 16)).count('1')

        answers.append(f"{b1} {b2}")

    return "\n".join(answers)

def main() -> None:
    """主程式進入點，讀取終端機的輸入並印出答案。"""
    print(solve_from_text(sys.stdin.read()))

if __name__ == "__main__":
    main()
