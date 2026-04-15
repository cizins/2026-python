import sys

def solve_easy(input_data: str) -> str:
    """
    解題思路 (簡單、容易記憶版)：
    1. 推導出 (b-a)(c-a) = a^2 + 1 之後，這題其實就是找 (a^2 + 1) 最接近的一對因數 (x, y)。
    2. 因為 (a^2 + 1) 的平方根大約就是 a，所以我們直接從 a 開始往下找第一個能整除的數 x。
    3. 我們利用 Python 的 Generator 搭配內建的 next() 函數，能用一行程式碼優雅地找到這個最大的因數 x。
    4. 找到 x 後，另一個因數就是 y = (a^2 + 1) // x。
    5. 最終答案為 b+c = x + y + 2a。這種寫法非常精簡且極具 Python 風格。
    """
    results = []
    # 使用 map 直接將輸入的所有數字轉換為整數 a
    for a in map(int, input_data.split()):
        # next() 會回傳 generator 中第一個符合條件的值，也就是最大的因數 x
        x = next(i for i in range(a, 0, -1) if (1 + a * a) % i == 0)
        y = (1 + a * a) // x
        ans = x + y + 2 * a
        results.append(str(ans))
        
    return "\n".join(results)

if __name__ == "__main__":
    # 支援 OJ 平台的標準輸入
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve_easy(input_text))
