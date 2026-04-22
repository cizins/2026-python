import os

problems = {
    "10226": "DFS 排列組合問題 (UVA 10226/a219)",
    "10235": "插座與蛇的方格放置問題 (UVA 10235/a228)",
    "10242": "ATM搶劫路線最大化問題 (UVA 10242/a235)",
    "10252": "兩條線的距離最小化問題 (UVA 10252/a245)",
}

base_dir = "."

for pid, desc in problems.items():
    # 寫入正規解法
    with open(f"solution_{pid}.py", "w", encoding="utf-8") as f:
        f.write(f'''# 解決 {desc} 的 Python 程式
# 這是一般的解題思路，會著重在效能與完整性。

def solve_{pid}(data):
    """
    解題主要函式，傳入題目所需的資料。
    請根據題意將輸入轉換為所需格式後傳入。
    """
    # TODO: 實作 {desc} 邏輯
    return None

if __name__ == "__main__":
    pass
''')
    
    # 寫入簡單易記版本
    with open(f"solution_{pid}-easy.py", "w", encoding="utf-8") as f:
        f.write(f'''# 解決 {desc} 的 Python 程式 - 簡易版
# 這裡使用更直觀、容易記憶的結構，適合在考場上快速寫出。

def solve_easy(data):
    """
    簡易版的解題函式，邏輯直白易懂。
    專注於通過大多數基礎測資。
    """
    # 建立一個簡單的陣列或變數來記錄結果
    result = None
    # TODO: 實作直觀的 {desc} 邏輯
    return result

if __name__ == "__main__":
    pass
''')

    # 寫入單元測試
    with open(f"test_{pid}.py", "w", encoding="utf-8") as f:
        f.write(f'''import unittest
from solution_{pid} import solve_{pid}

class TestProblem{pid}(unittest.TestCase):
    """
    針對 {desc} 進行自動化單元測試。
    幫助確認邏輯與邊界條件。
    """
    
    def test_example(self):
        """
        測試題目給定的範例輸入。
        """
        # TODO: 填入範例資料與預期輸出
        self.assertEqual(solve_{pid}([]), None)

if __name__ == '__main__':
    unittest.main()
''')

