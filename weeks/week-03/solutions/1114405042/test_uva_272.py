import unittest
from uva_272 import solve
from uva_272_easy import solve_easy

class TestUVA272(unittest.TestCase):
    """
    UVA 272 的單元測試 (Unit Test)
    使用 Python 內建的 unittest 模組來驗證解答是否正確。
    """
    
    def setUp(self):
        """
        準備題目提供的測資 (Sample Input) 與預期輸出 (Sample Output)。
        """
        # 這是題目提供的測資，包含多行與多個雙引號
        self.sample_input = """"To be or not to be," quoth the Bard, "that
is the question".
The programming contestant replied: "I must disagree.
To `C' or not to `C', that is The Question!"
"""
        
        # 這是測資預期應該要有的正確輸出
        # 應該要將所有的成對 " 替換成 `` 和 ''
        self.sample_output = """``To be or not to be,'' quoth the Bard, ``that
is the question''.
The programming contestant replied: ``I must disagree.
To `C' or not to `C', that is The Question!''
"""
        
        # 邊界測資：單行內有多層次或連續的引號
        self.edge_case_input = 'He said "What?" and then "" followed by "Nothing".'
        self.edge_case_output = "He said ``What?'' and then ``'' followed by ``Nothing''."

    def test_solve_normal(self):
        """測試標準版解法 (uva_272.py) 能否通過範例測資"""
        print("\n--- 執行測試: 標準版 (uva_272.py) ---")
        result = solve(self.sample_input)
        self.assertEqual(result, self.sample_output, "標準版解答無法通過範例測資！")
        print("標準版 (uva_272.py) 測試成功通過！")
        
    def test_solve_easy(self):
        """測試簡單版解法 (uva_272_easy.py) 能否通過範例測資"""
        print("\n--- 執行測試: 簡單版 (uva_272_easy.py) ---")
        result = solve_easy(self.sample_input)
        self.assertEqual(result, self.sample_output, "簡單版解答無法通過範例測資！")
        print("簡單版 (uva_272_easy.py) 測試成功通過！")

    def test_edge_cases(self):
        """測試邊界測資，例如連續引號與同行多個引號"""
        print("\n--- 執行測試: 邊界測資測試 (uva_272_easy.py) ---")
        result = solve_easy(self.edge_case_input)
        self.assertEqual(result, self.edge_case_output, "邊界測資測試失敗！")
        print("邊界測資測試成功通過！")

if __name__ == '__main__':
    # 執行所有以 test_ 開頭的測試方法
    unittest.main()