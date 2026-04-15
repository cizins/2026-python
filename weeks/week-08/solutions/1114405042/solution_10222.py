import sys

def solve(input_data: str) -> str:
    """
    解題思路 (標準版)：
    1. 這是經典的 UVA 10222 (Decode the Mad man) 鍵盤解碼問題。
    2. 題目描述雖然稍微有些筆誤（標準 UVA 10222 實際上是向左偏移 2 個鍵，例如 'k' 變成 'h'，']' 變成 'p'）。
    3. 我們將鍵盤由左至右的字元定義成一個長字串。
    4. 遍歷輸入的每一個字元：
       - 若為大寫字母則先轉為小寫。
       - 若該字元存在於鍵盤字串中，就將索引值減 2（向左移 2 位）。
       - 若為空白、換行或是找不到的字元，則原封不動保留。
    5. 最後將轉換後的字元組合成字串並回傳。
    """
    # 建立鍵盤標準對應表（依照標準 QWERTY 鍵盤）
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    results = []
    # 逐字元讀取處理
    for char in input_data:
        # 將大寫轉小寫
        lower_char = char.lower()
        
        # 尋找該字元在鍵盤中的位置
        idx = keyboard.find(lower_char)
        
        # 如果有找到且可以向左移 2 格
        if idx >= 2:
            results.append(keyboard[idx - 2])
        else:
            # 空白、換行或原本就在最左邊兩個位置的字元原樣輸出
            results.append(lower_char)
            
    return "".join(results)

if __name__ == "__main__":
    # 支援 OJ 平台的標準輸入
    input_text = sys.stdin.read()
    if input_text:
        print(solve(input_text), end="")
