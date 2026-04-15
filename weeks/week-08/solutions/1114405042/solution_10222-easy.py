import sys

def solve_easy(input_data: str) -> str:
    """
    解題思路 (簡單、容易記憶版)：
    1. 這是一道典型的「一對一字元映射轉換 (Character Mapping)」問題。
    2. 在 Python 中，處理字元映射最優雅、最快的方式是使用字串內建的 `str.translate()` 與 `str.maketrans()`。
    3. 我們只需要先把鍵盤字串定義好，再把「原字串的後段」對應到「前段」，就能建立出偏移 2 個位置的轉換表。
    4. 透過 `.lower()` 將全部轉小寫後，一行 `.translate()` 就能完美完成所有轉換。
    """
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    # 建立映射表：原字串的第 [2:] 個字元，對應到第 [:-2] 個字元。
    # 也就是說，如果原本輸入為 'e' (index 2)，會被對應成 'q' (index 0)
    mapping = str.maketrans(keyboard[2:], keyboard[:-2])
    
    # 全部轉小寫後直接套用映射表，空白和未設定映射的字元會保持原樣
    return input_data.lower().translate(mapping)

if __name__ == "__main__":
    # 從標準輸入讀取測試資料
    input_text = sys.stdin.read()
    if input_text:
        print(solve_easy(input_text), end="")
