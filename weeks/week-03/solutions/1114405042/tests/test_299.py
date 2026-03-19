import unittest
import importlib.util
import os
import sys

# 將當前目錄加入 sys.path 以便載入模組
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# 透過 importlib 手動匯入模組，解決檔名包含特殊字元 '-' 的問題
spec_std = importlib.util.spec_from_file_location("std_299", os.path.join(current_dir, "..", "299.py"))
if spec_std and spec_std.loader:
    std_299 = importlib.util.module_from_spec(spec_std)
    spec_std.loader.exec_module(std_299)

spec_easy = importlib.util.spec_from_file_location("easy_299", os.path.join(current_dir, "..", "299-easy.py"))
if spec_easy and spec_easy.loader:
    easy_299 = importlib.util.module_from_spec(spec_easy)
    spec_easy.loader.exec_module(easy_299)

class TestUVA299(unittest.TestCase):
    """
    針對 UVA 299 (Train Swapping) 進行單元測試
    確保標準版 (299.py) 與簡單版 (299-easy.py) 都能正確計算最少交換次數
    """
    
    def setUp(self):
        # 官方提供的範例測資
        self.sample_input = (
            "3\n"
            "3\n"
            "1 3 2\n"
            "4\n"
            "4 3 2 1\n"
            "2\n"
            "2 1\n"
        )
        
        # 官方預期的正確輸出
        self.expected_output = (
            "Optimal train swapping takes 1 swaps.\n"
            "Optimal train swapping takes 6 swaps.\n"
            "Optimal train swapping takes 1 swaps."
        )
        
    def test_standard_solution(self):
        """測試標準版解法 (299.py)"""
        result = std_299.solve_train_swapping(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版解法輸出不符合預期")
        
    def test_easy_solution(self):
        """測試簡單版解法 (299-easy.py)"""
        result = easy_299.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版解法輸出不符合預期")
        
    def test_empty_input(self):
        """測試空輸入"""
        self.assertEqual(std_299.solve_train_swapping(""), "")
        self.assertEqual(easy_299.solve_easy(""), "")

    def test_already_sorted(self):
        """測試已經排好序的情況，交換次數應為 0"""
        input_data = "1\n5\n1 2 3 4 5\n"
        expected = "Optimal train swapping takes 0 swaps."
        self.assertEqual(std_299.solve_train_swapping(input_data), expected)
        self.assertEqual(easy_299.solve_easy(input_data), expected)

    def test_zero_trains(self):
        """測試 L=0 (沒有車廂) 的邊界情況"""
        input_data = "1\n0\n"
        expected = "Optimal train swapping takes 0 swaps."
        self.assertEqual(std_299.solve_train_swapping(input_data), expected)
        self.assertEqual(easy_299.solve_easy(input_data), expected)

if __name__ == '__main__':
    unittest.main()
