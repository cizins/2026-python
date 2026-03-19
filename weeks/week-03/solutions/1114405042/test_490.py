import unittest
import importlib.util
import os
import sys

# 將當前目錄加入 sys.path 以便載入模組
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# 透過 importlib 手動匯入模組，解決檔名包含特殊字元 '-' 的問題
spec_std = importlib.util.spec_from_file_location("std_490", os.path.join(current_dir, "490.py"))
if spec_std and spec_std.loader:
    std_490 = importlib.util.module_from_spec(spec_std)
    spec_std.loader.exec_module(std_490)

spec_easy = importlib.util.spec_from_file_location("easy_490", os.path.join(current_dir, "490-easy.py"))
if spec_easy and spec_easy.loader:
    easy_490 = importlib.util.module_from_spec(spec_easy)
    spec_easy.loader.exec_module(easy_490)


class TestUVA490(unittest.TestCase):
    """
    針對 UVA 490 (Rotating Sentences) 進行單元測試
    確保標準版 (490.py) 與簡單版 (490-easy.py) 都能正確旋轉字串並處理空白補齊
    """
    
    def setUp(self):
        # 官方提供的範例測資
        self.sample_input = (
            "Rene Decartes once said,\n"
            '"I think, therefore I am."'
        )
        
        # 官方預期的正確輸出
        self.expected_output = (
            '"R\n'
            'Ie\n'
            ' n\n'
            'te\n'
            'h \n'
            'iD\n'
            'ne\n'
            'kc\n'
            ',a\n'
            ' r\n'
            'tt\n'
            'he\n'
            'es\n'
            'r \n'
            'eo\n'
            'fn\n'
            'oc\n'
            're\n'
            'e \n'
            ' s\n'
            'Ia\n'
            ' i\n'
            'ad\n'
            'm,\n'
            '. \n'
            '" '
        )
        
    def test_standard_solution(self):
        """測試標準版解法 (490.py)"""
        result = std_490.solve_rotating_sentences(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版解法輸出不符合預期")
        
    def test_easy_solution(self):
        """測試簡單版解法 (490-easy.py)"""
        result = easy_490.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版解法輸出不符合預期")
        
    def test_empty_input(self):
        """測試空輸入"""
        self.assertEqual(std_490.solve_rotating_sentences(""), "")
        self.assertEqual(easy_490.solve_easy(""), "")

    def test_different_lengths_with_middle_short(self):
        """測試中間句子較短，需要正確填補空白的情況"""
        # 輸入三行：
        # abc
        # d
        # efgh
        input_data = "abc\nd\nefgh"
        
        # 最長長度為 4 (efgh)
        # 反向順序：efgh (長4), d (長1), abc (長3)
        # i=0: e, d, a -> eda
        # i=1: f, ' ', b -> f b
        # i=2: g, ' ', c -> g c
        # i=3: h, ' ', ' ' -> h  
        expected = "eda\nf b\ng c\nh  "
        
        self.assertEqual(std_490.solve_rotating_sentences(input_data), expected)
        self.assertEqual(easy_490.solve_easy(input_data), expected)

if __name__ == '__main__':
    unittest.main()
