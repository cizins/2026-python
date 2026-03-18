"""UVA 10008 的單元測試。

測試重點：
1. 字母數量統計與大小寫轉換是否正確。
2. 出現次數不同時，是否由大到小排序。
3. 出現次數相同時，是否依字母 A 到 Z 排序。
4. 遇到無關字元 (數字、標點、空白) 是否會被過濾掉。
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
MAIN_SOLVER = _load_module("question_10008.py", "question_10008")
EASY_SOLVER = _load_module("question_10008-easy.py", "question_10008_easy")


class TestQuestion10008(unittest.TestCase):
    """針對 UVA 10008 的測試案例。"""

    def test_uva_sample_cases(self):
        """測試 UVA 題目提供的標準範例測資。
        輸入：
        3
        This is a test.
        Count me 1 2 3 4 5.
        Wow!!!! Is this testing?
        
        輸出應為各字母的統計 (略去低於1次的字母，並遵守排序規則)
        """
        text = """3
This is a test.
Count me 1 2 3 4 5.
Wow!!!! Is this testing?
"""
        expected = """S 7
T 6
I 5
E 4
O 3
A 2
H 2
N 2
C 1
G 1
M 1
U 1
W 2"""
        # 注意: 原題範例中 W 出現兩次 ('Wow' 裡有 W 和 w)，所以 W 也是 2，
        # 上述預期輸出的正確順序應為:
        expected = """T 7
S 6
I 5
E 3
H 2
N 2
O 2
W 2
A 1
C 1
G 1
M 1
U 1"""

        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_sort_alphabetical_when_tie(self):
        """測試當字母出現次數相同時，是否會以字母的順序 A~Z 進行排列。"""
        text = "1\nBCA"
        expected = "A 1\nB 1\nC 1"
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)

    def test_ignore_non_letters(self):
        """測試是否成功忽略所有標點符號與數字。"""
        text = "1\n123!@#aA"
        expected = "A 2"
        
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)


if __name__ == "__main__":
    unittest.main()
