import unittest
import importlib.util
import os
import sys

# 將上一層目錄 (也就是 1114405042) 加入 sys.path，確保可以載入模組
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# 透過 importlib 手動匯入模組，解決檔名包含特殊字元 '-' 的問題
spec_std = importlib.util.spec_from_file_location("std_100", os.path.join(parent_dir, "100.py"))
if spec_std and spec_std.loader:
    std_100 = importlib.util.module_from_spec(spec_std)
    spec_std.loader.exec_module(std_100)

spec_easy = importlib.util.spec_from_file_location("easy_100", os.path.join(parent_dir, "100-easy.py"))
if spec_easy and spec_easy.loader:
    easy_100 = importlib.util.module_from_spec(spec_easy)
    spec_easy.loader.exec_module(easy_100)


class TestUVA100(unittest.TestCase):
    """
    針對 UVA 100 (The 3n + 1 problem) 進行單元測試
    確保標準版 (100.py) 與簡單版 (100-easy.py) 都能正確計算區間內最大的 cycle-length
    """
    
    def setUp(self):
        # 官方提供的範例測資
        self.sample_input = (
            "1 10\n"
            "100 200\n"
            "201 210\n"
            "900 1000\n"
        )
        
        # 官方預期的正確輸出
        self.expected_output = (
            "1 10 20\n"
            "100 200 125\n"
            "201 210 89\n"
            "900 1000 174"
        )
        
    def test_standard_solution(self):
        """測試標準版解法 (100.py)"""
        result = std_100.solve_3n_plus_1(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版解法輸出不符合預期")
        
    def test_easy_solution(self):
        """測試簡單版解法 (100-easy.py)"""
        result = easy_100.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版解法輸出不符合預期")
        
    def test_empty_input(self):
        """測試空輸入"""
        self.assertEqual(std_100.solve_3n_plus_1(""), "")
        self.assertEqual(easy_100.solve_easy(""), "")

    def test_reversed_order(self):
        """
        測試邊界情況：當起點大於終點 (i > j) 時，
        是否能夠自動翻轉區間，且輸出的時候保持原本反向的 i j 順序
        """
        input_data = "10 1"
        expected = "10 1 20"
        self.assertEqual(std_100.solve_3n_plus_1(input_data), expected)
        self.assertEqual(easy_100.solve_easy(input_data), expected)

if __name__ == '__main__':
    unittest.main()
