import unittest
import importlib.util
import os
import sys

# 將當前資料夾加入 sys.path，以利載入 Python 檔案
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 載入兩個版本的解法
try:
    import solution_10221
    # 動態載入帶有橫線的檔案名稱
    spec = importlib.util.spec_from_file_location("solution_10221_easy", os.path.join(os.path.dirname(__file__), "solution_10221-easy.py"))
    solution_10221_easy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_10221_easy)
except Exception as e:
    print(f"Error loading module: {e}")

class TestSatellites10221(unittest.TestCase):
    """
    題目 10221 (UVA 10221 / a214) 的 Unit Test。
    這題主要是測試單位換算 (度/分) 以及基礎的三角幾何運算 (弧長/弦長)。
    同時要檢查大於 180 度的角 (測資中的 200 45 deg 實際上角度較小，因為 200 45 是兩顆星距...)。
    等等，測資範例是 s=200, a=45 deg
    """
    def setUp(self):
        # 準備範例資料
        self.sample_input = (
            "500 30 deg\n"
            "700 60 min\n"
            "200 45 deg\n"
        )
        self.expected_output = (
            "3633.775503 3592.408346\n"
            "124.616509 124.614927\n"
            "5215.043805 5082.035982"
        )

    def test_standard_solution(self):
        """測試標準版解答"""
        result = solution_10221.solve(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "標準版輸出不符預期！")

    def test_easy_solution(self):
        """測試簡單版解答"""
        result = solution_10221_easy.solve_easy(self.sample_input).strip()
        self.assertEqual(result, self.expected_output, "簡單版輸出不符預期！")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
