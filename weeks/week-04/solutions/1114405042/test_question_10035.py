"""UVA 10035 的單元測試。

測試重點：
1. 長度不同時的進位是否正確 (例如 9999 + 1)。
2. 長度相同時的進位是否正確 (例如 555 + 555)。
3. 完全沒有進位的情況 (例如 123 + 456)。
4. 遇到 0 0 必須停止計算。
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

# 動態載入標準版與 Easy 版
MAIN_SOLVER = _load_module("question_10035.py", "question_10035")
EASY_SOLVER = _load_module("question_10035-easy.py", "question_10035_easy")


class TestQuestion10035(unittest.TestCase):
    """針對 UVA 10035 的測試案例。"""

    def test_uva_sample_cases(self):
        """測試 UVA 題目提供的標準範例測資。
        輸入：
        123 456
        555 555
        123 594
        0 0
        
        輸出：
        No carry operation.
        3 carry operations.
        1 carry operation.
        """
        text = "123 456\n555 555\n123 594\n0 0\n"
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."

        # 驗證標準版與 easy 版結果是否相同
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_different_lengths_carry(self):
        """測試長度不同的進位 (連鎖進位效應)。
        999 + 1 = 1000 (會有 3 次進位)
        """
        text = "999 1\n0 0\n"
        expected = "3 carry operations."
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_no_carry(self):
        """測試完全沒有進位的情況，並且終止符 `0 0` 要生效。"""
        text = "0 0\n"
        expected = ""
        
        # 什麼都沒算，應該回傳空字串
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_large_numbers(self):
        """測試十位數長度的大數字。
        10 個 5 加上 10 個 5 = 1111111110 (會有 10 次進位)
        """
        text = "5555555555 5555555555\n0 0\n"
        expected = "10 carry operations."
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)


if __name__ == "__main__":
    unittest.main()
