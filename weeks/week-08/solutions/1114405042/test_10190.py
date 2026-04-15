import unittest
import importlib.util
import os
import sys

# 確保可以 import 同層的模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import solution_10190
    spec = importlib.util.spec_from_file_location("solution_10190_easy", os.path.join(os.path.dirname(__file__), "solution_10190-easy.py"))
    solution_10190_easy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_10190_easy)
except Exception as e:
    print(f"Error loading modules: {e}")

class TestRainUmbrella10190(unittest.TestCase):
    """
    題目 UVA 10190 (ZeroJudge a183 自動傘) 的 Unit Test。
    使用從 ZeroJudge 抓取到的範例輸入輸出驗證程式的正確性。
    """
    def setUp(self):
        # 準備範例資料
        self.sample_input = (
            "2 4 3 10\n"
            "0 1 1\n"
            "3 1 -1\n"
        )
        self.expected_output = "65.00"

    def test_standard_exact_solution(self):
        """測試標準版解法 (Event-Driven Exact Integral)"""
        result = solution_10190.solve(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "精確版輸出不符預期！")

    def test_easy_numerical_solution(self):
        """測試簡單版 (梯形數值積分) 解法"""
        result = solution_10190_easy.solve_easy(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "數值積分版輸出不符預期！")

if __name__ == '__main__':
    unittest.main()
