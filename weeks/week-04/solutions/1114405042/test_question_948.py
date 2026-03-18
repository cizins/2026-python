"""UVA 948 的單元測試。

測試重點：
1. 可以唯一判斷假幣。
2. 無法唯一判斷時輸出 0。
3. 多組測資時，輸出格式要有空白行分隔。
4. 標準版與 easy 版都要通過同一批測資。
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent


def _load_module(file_name: str, module_name: str):
    """從檔案路徑動態載入模組（支援檔名含連字號）。"""
    path = BASE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組: {path}")
    module = importlib.util.module_from_spec(spec)
    # 先註冊到 sys.modules，可避免 dataclass 取不到對應 module namespace。
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


MAIN_SOLVER = _load_module("question_948.py", "question_948")
EASY_SOLVER = _load_module("question_948-easy.py", "question_948_easy")


class TestQuestion948(unittest.TestCase):
    """針對題目邏輯做行為驗證。"""

    def test_unique_coin_by_equal_result(self):
        """1 和 2 被證明是真幣，因此 3 一定是假幣。"""
        text = """1

3 1
1 1 2
=
"""
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), "3")
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), "3")

    def test_ambiguous_should_output_zero(self):
        """同時有多顆硬幣可能是假幣時，必須輸出 0。"""
        text = """1

2 1
1 1 2
<
"""
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), "0")
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), "0")

    def test_inconsistent_should_output_zero(self):
        """若所有假設都無法成立，也要輸出 0。"""
        text = """1

3 2
1 1 2
=
1 2 3
=
"""
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), "0")
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), "0")

    def test_multiple_cases_output_format(self):
        """多組測資輸出需以空白行分隔。"""
        text = """2

3 1
1 1 2
=

2 1
1 1 2
<
"""
        expected = "3\n\n0"
        self.assertEqual(MAIN_SOLVER.solve_from_text(text).strip(), expected)
        self.assertEqual(EASY_SOLVER.solve_from_text(text).strip(), expected)


if __name__ == "__main__":
    unittest.main()
