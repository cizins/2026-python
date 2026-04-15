import sys

def solve(input_data: str) -> str:
    """
    解題思路 (標準版)：
    1. 題目要求我們解出 arctan(1/a) = arctan(1/b) + arctan(1/c) 中，b+c 的最小值。
    2. 根據反正切函數的相加公式：arctan(1/b) + arctan(1/c) = arctan((b+c)/(bc-1))。
    3. 因此得到方程式：1/a = (b+c)/(bc-1) => bc - 1 = ab + ac。
    4. 經過移項與因式分解：bc - ab - ac = 1 => (b - a)(c - a) = 1 + a^2。
    5. 令 x = b - a, y = c - a，則方程式轉化為 x * y = 1 + a^2。
    6. 我們要求 b + c 的最小值，也就是求 (x + a) + (y + a) = x + y + 2a 的最小值。
    7. 由於 2a 是固定值，問題轉換為求滿足 x * y = 1 + a^2 的整數對 (x, y) 中，x + y 的最小值。
    8. 根據數學性質，當 x 和 y 越接近時，x + y 的值越小。因此我們從 x = a (即 sqrt(1+a^2) 的整數部分) 開始往下尋找因數，找到的第一個因數即能產生最小的 x + y。
    """
    results = []
    # 讀取所有測資 (雖然題目說只有一個，但多筆測資防禦性寫法更為保險，方便 OJ 平台測試)
    tokens = input_data.split()
    for token in tokens:
        a = int(token)
        target = 1 + a * a
        # 從 a 開始往下找，找到的第一個因數即可保證 x 與 y 最接近 (因為 sqrt(1+a^2) 的整數部分就是 a)
        for x in range(a, 0, -1):
            if target % x == 0:
                y = target // x
                ans = x + y + 2 * a
                results.append(str(ans))
                break
                
    return "\n".join(results)

if __name__ == "__main__":
    # 若直接執行此檔案，從標準輸入讀取資料並輸出結果
    input_text = sys.stdin.read()
    if input_text.strip():
        print(solve(input_text))
