import unittest
from uva_299 import solve
from uva_299_easy import solve_easy

class TestUVA299(unittest.TestCase):
    """
    UVA 299 的單元測試 (Unit Test)
    用來驗證「逆序數對法」和「泡沫排序模擬法」是否都能正確算出最少交換次數。
    """
    
    def setUp(self):
        """
        準備題目提供的測資 (Sample Input) 與預期輸出 (Sample Output)。
        包含 3 筆測試資料。
        """
        self.sample_input = """3
3
1 3 2
4
4 3 2 1
2
2 1"""
        
        self.sample_output = """Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps."""
        
        # 邊界測資：車廂長度為 0 的情況，或是原本就排好的情況
        self.edge_case_input = """3
0

5
1 2 3 4 5
3
3 1 2"""
        
        self.edge_case_output = """Optimal train swapping takes 0 swaps.
Optimal train swapping takes 0 swaps.
Optimal train swapping takes 2 swaps."""

    def test_solve_normal(self):
        """測試標準版解法 (uva_299.py - 逆序數對法)"""
        print("\n--- 執行測試: 標準版 (uva_299.py) ---")
        result = solve(self.sample_input)
        self.assertEqual(result, self.sample_output, "標準版解答無法通過範例測資！")
        print("標準版 (uva_299.py) 測試成功通過！")
        
    def test_solve_easy(self):
        """測試簡單版解法 (uva_299_easy.py - 泡沫排序模擬法)"""
        print("\n--- 執行測試: 簡單版 (uva_299_easy.py) ---")
        result = solve_easy(self.sample_input)
        self.assertEqual(result, self.sample_output, "簡單版解答無法通過範例測資！")
        print("簡單版 (uva_299_easy.py) 測試成功通過！")

    def test_edge_cases(self):
        """測試邊界測資 (例如長度為 0 或已排序好)"""
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