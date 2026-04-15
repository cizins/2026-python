import unittest
import importlib.util
import os
import sys

# 將當前資料夾加入 sys.path，以利載入 Python 檔案
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 動態載入兩個版本的解法
try:
    import solution_10222
    # 載入帶有橫線的檔案名稱
    spec = importlib.util.spec_from_file_location("solution_10222_easy", os.path.join(os.path.dirname(__file__), "solution_10222-easy.py"))
    solution_10222_easy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_10222_easy)
except Exception as e:
    print(f"Error loading module: {e}")

class TestDecodeMadMan10222(unittest.TestCase):
    """
    題目 10222 (UVA 10222 / a215) 的 Unit Test。
    這題是將輸入在 QWERTY 鍵盤上向左平移 2 格。
    """
    def setUp(self):
        # UVA 10222 標準範例資料
        # "k[r dyt i[o ?" 對應 "how are you ?"
        self.sample_input = "k[r dyt i[o ?"
        self.expected_output = "how are you ?"

    def test_standard_solution(self):
        """測試標準版解答"""
        # 注意 strip() 以去除尾部換行等雜訊
        result = solution_10222.solve(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "標準版輸出不符預期！")

    def test_easy_solution(self):
        """測試簡單版解答 (str.translate)"""
        result = solution_10222_easy.solve_easy(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "簡單版輸出不符預期！")
        
    def test_case_insensitive(self):
        """測試大小寫轉換 (UVA 10222 要求全小寫)"""
        input_data = "K[R DYT I[O ?"
        result = solution_10222_easy.solve_easy(input_data).strip()
        self.assertEqual(result, self.expected_output, "大小寫轉換失敗！")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
