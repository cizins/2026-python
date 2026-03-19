import unittest
from uva_118 import solve
from uva_118_easy import solve_easy

class TestUVA118(unittest.TestCase):
    """
    UVA 118 的單元測試 (Unit Test)
    使用 Python 內建的 unittest 模組來驗證解答是否正確。
    """
    
    def setUp(self):
        """
        setUp 是在每一個 test_* 方法執行前都會自動呼叫的初始化函式。
        我們在這裡準備題目提供的測資 (Sample Input) 與預期輸出 (Sample Output)。
        """
        # 這是題目提供的測資
        self.sample_input = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL"""
        
        # 這是測資預期應該要有的正確輸出
        self.sample_output = """1 1 E
3 3 N LOST
2 3 S"""
        
        # 額外新增一筆邊界測資
        self.edge_case_input = """2 2
0 0 S
F
0 0 W
F
0 0 S
F"""
        # 第一個掉在 (0,0) 面向南，第二個掉在 (0,0) 面向西，第三個有氣味保護所以留在原點面向南
        self.edge_case_output = """0 0 S LOST
0 0 W
0 0 S"""

    def test_solve_normal(self):
        """測試標準版解法 (uva_118.py) 能否通過 UVA 的範例測資"""
        print("\n--- 執行測試: 標準版 (uva_118.py) ---")
        result = solve(self.sample_input)
        self.assertEqual(result, self.sample_output, "標準版解答無法通過範例測資！")
        print("標準版 (uva_118.py) 測試成功通過！")
        
    def test_solve_easy(self):
        """測試簡單版解法 (uva_118_easy.py) 能否通過 UVA 的範例測資"""
        print("\n--- 執行測試: 簡單版 (uva_118_easy.py) ---")
        result = solve_easy(self.sample_input)
        self.assertEqual(result, self.sample_output, "簡單版解答無法通過範例測資！")
        print("簡單版 (uva_118_easy.py) 測試成功通過！")

    def test_edge_cases(self):
        """測試邊界氣味是否正常運作"""
        print("\n--- 執行測試: 邊界氣味測試 (uva_118_easy.py) ---")
        result = solve_easy(self.edge_case_input)
        self.assertEqual(result, self.edge_case_output, "邊界氣味測試失敗！")
        print("邊界氣味測試 (uva_118_easy.py) 成功通過！")

if __name__ == '__main__':
    # 執行所有以 test_ 開頭的測試方法
    unittest.main()