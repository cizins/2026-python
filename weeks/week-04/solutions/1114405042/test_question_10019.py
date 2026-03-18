"""UVA 10019 的單元測試。

測試重點：
1. 標準版與 easy 版都能正確計算出 b1 (二進位中 1 的個數) 與 b2 (十六進位中 1 的個數)。
2. 能通過標準的 UVA 範例測資。
"""

import importlib.util
import pathlib
import sys
import unittest

# 取得目前測試檔案所在的目錄
BASE_DIR = pathlib.Path(__file__).resolve().parent

def _load_module(file_name: str, module_name: str):
    """從檔案路徑動態載入模組，解決檔名中有連字號 (-) 無法直接 import 的問題。"""
    path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# 動態載入我們剛寫的兩版解答
MAIN_SOLVER = _load_module("question_10019.py", "question_10019")
EASY_SOLVER = _load_module("question_10019-easy.py", "question_10019_easy")


class TestQuestion10019(unittest.TestCase):
    """針對 UVA 10019 的測試案例。"""

    def test_uva_sample_cases(self):
        """測試 UVA 題目提供的標準範例測資。
        輸入：
        3
        265
        111
        1234
        
        輸出：
        3 5
        6 3
        5 5
        """
        text = "3\n265\n111\n1234\n"
        expected = "3 5\n6 3\n5 5"

        # 驗證標準版邏輯是否正確
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        # 驗證簡單好記版的邏輯是否正確
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_single_digit(self):
        """測試單一數字。因為十進位的 7 與十六進位的 7 長得一樣，所以 1 的數量也要一樣。"""
        text = "1\n7\n"
        expected = "3 3"  # 7 是 0111，有 3 個 '1'
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_zero_case(self):
        """測試邊界情況: 輸入 0 時，1 的數量應該都是 0。"""
        text = "1\n0\n"
        expected = "0 0"
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)


if __name__ == "__main__":
    unittest.main()
