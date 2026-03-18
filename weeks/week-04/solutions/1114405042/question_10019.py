"""UVA 10019 Funny Encryption Method - 標準版。

這題要求我們計算一個數字在兩種不同解讀方式下，其二進位表示法中 '1' 的數量：
1. 把它當作十進位數字 (Decimal)，轉成二進位後算 '1' 的個數 (b1)。
2. 把它當作十六進位數字 (Hexadecimal)，轉成二進位後算 '1' 的個數 (b2)。
"""
import sys

def count_ones_in_binary(n: int) -> int:
    """將整數 n 視為十進位，回傳其二進位中 1 的個數。"""
    return bin(n).count('1')

def count_ones_in_hex(n_str: str) -> int:
    """將字串 n_str 視為十六進位，回傳其二進位中 1 的個數。"""
    # int(n_str, 16) 會把字串當作十六進位來解析成整數
    return bin(int(n_str, 16)).count('1')

def solve_from_text(text: str) -> str:
    """解析完整輸入並回傳解答字串。"""
    lines = text.strip().splitlines()
    if not lines:
        return ""

    try:
        # 第一行是測資的數量
        cases = int(lines[0].strip())
    except ValueError:
        return ""

    outputs = []
    # 逐一處理每一筆測資
    for i in range(1, cases + 1):
        if i >= len(lines):
            break
        line = lines[i].strip()
        if not line:
            continue

        # 計算 b1: 當作十進位
        b1 = count_ones_in_binary(int(line))
        # 計算 b2: 當作十六進位 (傳入字串讓 int() 處理 16 進位轉換)
        b2 = count_ones_in_hex(line)
        
        outputs.append(f"{b1} {b2}")

    return "\n".join(outputs)

def main() -> None:
    """主程式進入點，讀取標準輸入並輸出結果。"""
    print(solve_from_text(sys.stdin.read()))

if __name__ == "__main__":
    main()
