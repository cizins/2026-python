import unittest
import importlib.util
import os
import sys

# 將當前目錄加入 sys.path 以便載入模組
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# 由於 118-easy.py 含有特殊字元 '-'，無法直接使用 import 載入
# 需要透過 importlib 手動匯入模組
spec_std = importlib.util.spec_from_file_location("std_118", os.path.join(current_dir, "..", "118.py"))
if spec_std and spec_std.loader:
    std_118 = importlib.util.module_from_spec(spec_std)
    spec_std.loader.exec_module(std_118)

spec_easy = importlib.util.spec_from_file_location("easy_118", os.path.join(current_dir, "..", "118-easy.py"))
if spec_easy and spec_easy.loader:
    easy_118 = importlib.util.module_from_spec(spec_easy)
    spec_easy.loader.exec_module(easy_118)

class TestUVA118(unittest.TestCase):
    """
    針對 UVA 118 (Mutant Flathead Groteque) 進行單元測試
    確保標準版 (118.py) 與簡單版 (118-easy.py) 都能得到正確結果
    """
    
    def setUp(self):
        # 設定 UVA 118 官方提供的範例測資
        self.sample_input = (
            "5 3\n"
            "1 1 E\n"
            "RFRFRFRF\n"
            "3 2 N\n"
            "FRRFLLFFRRFLL\n"
            "0 3 W\n"
            "LLFFFLFLFL\n"
        )
        # 官方預期的正確輸出結果
        self.expected_output = (
            "1 1 E\n"
            "3 3 N LOST\n"
            "2 3 S"
        )
        
    def test_standard_solution(self):
        """測試標準版解法 (118.py)"""
        result = std_118.solve_robot_instructions(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版解法輸出不符合預期")
        
    def test_easy_solution(self):
        """測試簡單版解法 (118-easy.py)"""
        result = easy_118.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版解法輸出不符合預期")
        
    def test_empty_input(self):
        """測試空輸入"""
        self.assertEqual(std_118.solve_robot_instructions(""), "")
        self.assertEqual(easy_118.solve_easy(""), "")

if __name__ == '__main__':
    unittest.main()
