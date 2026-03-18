"""UVA 10035 Primary Arithmetic - 標準版。

此程式模擬我們在小學計算直式加法時的「進位」動作。
作法是將兩個數字轉為字串，透過補零 (zfill) 讓兩個字串一樣長，
然後由右至左（由低位到高位）逐位相加，並將進位狀態（0 或 1）記錄下來，帶入下一位的計算。
"""

import sys


def count_carries(a_str: str, b_str: str) -> int:
    """計算兩個字串數字相加時的總進位次數。"""
    
    # 取兩個字串的最大長度
    max_len = max(len(a_str), len(b_str))
    
    # zfill 會在字串左邊補 0，讓兩個數字位數對齊
    # 例如："123" 和 "55" 會變成 "123" 和 "055"
    a = list(a_str.zfill(max_len))
    b = list(b_str.zfill(max_len))
    
    carries = 0  # 總共進位幾次
    carry = 0    # 目前這一位有沒有進位過來 (0 或 1)
    
    # zip() 可以把兩個陣列配對，reversed() 代表從後面(個位數)開始往前算
    for x, y in zip(reversed(a), reversed(b)):
        # x, y 原本是字串，轉成整數後加上前一位傳過來的 carry
        if int(x) + int(y) + carry >= 10:
            carries += 1
            carry = 1  # 產生進位，帶給下一位
        else:
            carry = 0  # 沒有進位，重置為 0
            
    return carries


def solve_from_text(text: str) -> str:
    """解析輸入的文字，回傳格式化後的答案字串。"""
    lines = text.strip().splitlines()
    outputs = []
    
    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
            
        a, b = parts[0], parts[1]
        
        # 遇到 "0 0" 就要停止程式
        if a == "0" and b == "0":
            break
            
        carries = count_carries(a, b)
        
        # 根據進位次數輸出對應的句子 (注意單複數與句號)
        if carries == 0:
            outputs.append("No carry operation.")
        elif carries == 1:
            outputs.append("1 carry operation.")
        else:
            outputs.append(f"{carries} carry operations.")
            
    return "\n".join(outputs)


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    print(solve_from_text(data))


if __name__ == "__main__":
    main()
