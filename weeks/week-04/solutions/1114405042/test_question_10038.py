"""UVA 10038 的單元測試。

測試重點：
1. 標準 Jolly 的情況。
2. 非 Jolly 的情況 (可能包含超出範圍的差值、或重複的差值)。
3. n = 1 的邊界條件 (這是一個陷阱，n=1 應該要判斷為 Jolly，因為 1 到 0 的集合是空的)。
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
MAIN_SOLVER = _load_module("question_10038.py", "question_10038")
EASY_SOLVER = _load_module("question_10038-easy.py", "question_10038_easy")


class TestQuestion10038(unittest.TestCase):
    """針對 UVA 10038 的測試案例。"""

    def test_uva_sample_cases(self):
        """測試 UVA 題目提供的標準範例測資。
        輸入：
        4 1 4 2 3
        5 1 4 2 -1 6
        
        輸出：
        Jolly
        Not jolly
        """
        text = "4 1 4 2 3\n5 1 4 2 -1 6\n"
        expected = "Jolly\nNot jolly"

        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_n_equals_one(self):
        """測試 n=1 的邊界條件。
        當 n=1 時，完全沒有「相鄰」的數字，差值集合為空。
        預期應該要跟 set(range(1, 1)) (也就是空集合) 相等，所以應該是 Jolly。
        """
        text = "1 99\n"
        expected = "Jolly"
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_duplicate_differences(self):
        """測試差值重複但沒有涵蓋全部情況的序列。
        例如 4 1 2 3 4
        差值都是 1，缺少了 2 和 3，所以應該是 Not jolly。
        """
        text = "4 1 2 3 4\n"
        expected = "Not jolly"
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)


if __name__ == "__main__":
    unittest.main()
