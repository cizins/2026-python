import unittest
from uva_490 import solve
from uva_490_easy import solve_easy

class TestUVA490(unittest.TestCase):
    """
    UVA 490 的單元測試 (Unit Test)
    驗證句子順時針旋轉 90 度，且遇到短句時是否能正確補足空白。
    """
    
    def setUp(self):
        """
        準備題目提供的測資 (Sample Input) 與預期輸出 (Sample Output)。
        """
        self.sample_input = """Rene Dekart
Blaise Pascal"""
        
        self.sample_output = """BR
le
an
ie
s 
eD
 e
Pk
aa
sr
ct
a 
l """
        
        # 邊界測資：長短交錯，尤其是第一行跟最後一行長度差異極大的情況
        self.edge_case_input = """123
12345
12"""
        
        self.edge_case_output = """111
222
 33
 4 
 5 """

    def test_solve_normal(self):
        """測試標準版解法 (uva_490.py)"""
        print("\n--- 執行測試: 標準版 (uva_490.py) ---")
        result = solve(self.sample_input)
        self.assertEqual(result, self.sample_output, "標準版解答無法通過範例測資！")
        print("標準版 (uva_490.py) 測試成功通過！")
        
    def test_solve_easy(self):
        """測試簡單版解法 (uva_490_easy.py)"""
        print("\n--- 執行測試: 簡單版 (uva_490_easy.py) ---")
        result = solve_easy(self.sample_input)
        self.assertEqual(result, self.sample_output, "簡單版解答無法通過範例測資！")
        print("簡單版 (uva_490_easy.py) 測試成功通過！")

    def test_edge_cases(self):
        """測試邊界測資 (例如長度不一的情境)"""
        print("\n--- 執行測試: 邊界測資測試 ---")
        
        # 標準版邊界測試
        result_normal = solve(self.edge_case_input)
        self.assertEqual(result_normal, self.edge_case_output, "標準版無法通過邊界測資！")
        
        # 簡單版邊界測試
        result_easy = solve_easy(self.edge_case_input)
        self.assertEqual(result_easy, self.edge_case_output, "簡單版無法通過邊界測資！")
        
        print("邊界測資測試成功通過！")

if __name__ == '__main__':
    unittest.main()