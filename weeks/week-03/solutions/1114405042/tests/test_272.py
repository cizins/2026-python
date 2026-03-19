import unittest
import importlib.util
import os
import sys

# 將當前目錄加入 sys.path 以便載入模組
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# 透過 importlib 手動匯入模組，解決檔名包含特殊字元 '-' 的問題
spec_std = importlib.util.spec_from_file_location("std_272", os.path.join(current_dir, "..", "272.py"))
if spec_std and spec_std.loader:
    std_272 = importlib.util.module_from_spec(spec_std)
    spec_std.loader.exec_module(std_272)

spec_easy = importlib.util.spec_from_file_location("easy_272", os.path.join(current_dir, "..", "272-easy.py"))
if spec_easy and spec_easy.loader:
    easy_272 = importlib.util.module_from_spec(spec_easy)
    spec_easy.loader.exec_module(easy_272)

class TestUVA272(unittest.TestCase):
    """
    針對 UVA 272 (TEX Quotes) 進行單元測試
    確保標準版 (272.py) 與簡單版 (272-easy.py) 都能正確替換雙引號
    """
    
    def setUp(self):
        # 設定 UVA 272 題目中的範例測資
        self.sample_input = (
            '"To be or not to be," quoth the bard, "that\n'
            'is the question."\n'
            'The programming contestant replied: "I must disagree.\n'
            'To `C\' or not to `C\', that is The Question!"\n'
        )
        
        # 題目預期的正確輸出結果
        self.expected_output = (
            '``To be or not to be,\'\' quoth the bard, ``that\n'
            'is the question.\'\'\n'
            'The programming contestant replied: ``I must disagree.\n'
            'To `C\' or not to `C\', that is The Question!\'\'\n'
        )
        
    def test_standard_solution(self):
        """測試標準版解法 (272.py)"""
        result = std_272.solve_tex_quotes(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版解法輸出不符合預期")
        
    def test_easy_solution(self):
        """測試簡單版解法 (272-easy.py)"""
        result = easy_272.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版解法輸出不符合預期")
        
    def test_empty_input(self):
        """測試空字串輸入，不應產生錯誤且輸出應為空"""
        self.assertEqual(std_272.solve_tex_quotes(""), "")
        self.assertEqual(easy_272.solve_easy(""), "")
        
    def test_no_quotes(self):
        """測試沒有雙引號的一般文字，應保持原樣"""
        text = "Hello, world! This is a simple test without any quotes."
        self.assertEqual(std_272.solve_tex_quotes(text), text)
        self.assertEqual(easy_272.solve_easy(text), text)

    def test_multiple_nested_quotes(self):
        """測試多組雙引號出現時是否能夠正確交替 (不考慮現實排版合理性)"""
        input_text = '"""Hello"""'
        # 預期：``, '', `` 接著 Hello 再來 '', ``, ''
        expected = "``''``Hello''``''"
        self.assertEqual(std_272.solve_tex_quotes(input_text), expected)
        self.assertEqual(easy_272.solve_easy(input_text), expected)

if __name__ == '__main__':
    unittest.main()
