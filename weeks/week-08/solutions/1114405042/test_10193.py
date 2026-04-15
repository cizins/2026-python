import unittest
import importlib.util
import os
import sys

# 將當前資料夾加入 sys.path，確保可以導入同目錄的 Python 檔案
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 動態載入標準版與簡單版程式
try:
    import solution_10193
    # 由於檔案名稱有連字號 (hyphen)，必須透過 importlib 動態加載模組
    spec = importlib.util.spec_from_file_location("solution_10193_easy", os.path.join(os.path.dirname(__file__), "solution_10193-easy.py"))
    solution_10193_easy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_10193_easy)
except Exception as e:
    print(f"Error loading module: {e}")

class TestArctan10193(unittest.TestCase):
    """
    題目 10193 (ZeroJudge a186) 的 Unit Test。
    這題是利用 arctan(1/a) = arctan(1/b) + arctan(1/c) 展開。
    主要就是求 b+c 的最小值。
    """
    
    def setUp(self):
        # 準備多筆測試案例的輸入 (包含 a = 1, 2, 等)
        self.sample_input = "1\n2\n"
        # 預期輸出結果，a=1 => 5 (b=2, c=3)
        # a=2 => 10 (b=3, c=7)
        self.expected_output = "5\n10"

    def test_standard_solution(self):
        """測試標準版解法"""
        result = solution_10193.solve(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "標準版輸出不符預期！")

    def test_easy_solution(self):
        """測試簡單版解法 (利用 Python Generator)"""
        result = solution_10193_easy.solve_easy(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "簡單版輸出不符預期！")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
