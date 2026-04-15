import unittest
import importlib.util
import os
import sys

# 將當前資料夾加入 sys.path，確保可以導入同一目錄下的 Python 檔案
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 載入標準版與簡單版程式
try:
    import solution_10189
    # 動態加載 solution_10189-easy (因為檔案名稱有中線 '-' 不能直接 import)
    spec = importlib.util.spec_from_file_location("solution_10189_easy", os.path.join(os.path.dirname(__file__), "solution_10189-easy.py"))
    solution_10189_easy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_10189_easy)
except Exception as e:
    print(f"Error loading module: {e}")

class TestMinesweeper10189(unittest.TestCase):
    """
    題目 10189 的 Unit Test。
    使用題目給定的範例輸入與輸出進行測試。
    """
    def setUp(self):
        # 準備題目提供的測試案例輸入
        self.sample_input = (
            "4 4\n"
            "*...\n"
            "....\n"
            ".*..\n"
            "....\n"
            "3 5\n"
            "**...\n"
            ".....\n"
            ".*...\n"
            "0 0\n"
        )
        # 準備預期的正確輸出 (注意中間需要空行)
        self.expected_output = (
            "Field #1:\n"
            "*100\n"
            "2210\n"
            "1*10\n"
            "1110\n"
            "\n"
            "Field #2:\n"
            "**100\n"
            "33200\n"
            "1*100"
        )

    def test_standard_solution(self):
        """測試標準版解法"""
        result = solution_10189.solve(self.sample_input)
        self.assertEqual(result, self.expected_output, "標準版輸出不符預期！")

    def test_easy_solution(self):
        """測試簡單版 (Padding技巧) 解法"""
        result = solution_10189_easy.solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output, "簡單版輸出不符預期！")

if __name__ == '__main__':
    # 執行所有測試
    unittest.main()
