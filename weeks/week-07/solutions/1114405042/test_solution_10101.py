import unittest
import importlib.util
from solution_10101 import solve

# 動態載入 solution_10101-easy.py 以進行測試
spec = importlib.util.spec_from_file_location("solution_10101_easy", "solution_10101-easy.py")
solution_10101_easy_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_10101_easy_module)
solve_easy = solution_10101_easy_module.solve_easy


class TestMatchstickEquation(unittest.TestCase):
    """
    測試 UVA 10101 變形 - 火柴棒等式問題。
    1. solve：使用正規表達式加上內部字典對應，有系統性的窮舉解答。
    2. solve_easy：簡易版的字元替換寫法，非常直覺且好寫。
    """

    def test_internal_move(self):
        # 測試：單一數字內部移動一根火柴棒
        # 例如 2+3=6 -> 把 2 變成 3 -> 3+3=6
        eq = "2+3=6#"
        expected = "3+3=6#"
        self.assertEqual(solve(eq), expected)
        self.assertEqual(solve_easy(eq), expected)
        
    def test_external_move(self):
        # 測試：一根火柴棒從一個數字移到另一個數字
        # 0+1=8 -> 0 增加一根變成 8，8 減少一根變成 9 -> 8+1=9
        eq = "0+1=8#"
        expected = "8+1=9#"
        self.assertEqual(solve(eq), expected)
        self.assertEqual(solve_easy(eq), expected)

    def test_no_solution(self):
        # 測試：無法只移動一根火柴棒就成立的等式
        eq = "1+1=0#"
        expected = "No"
        self.assertEqual(solve(eq), expected)
        self.assertEqual(solve_easy(eq), expected)

    def test_leading_zero(self):
        # 測試：修改後產生前導零的情況 (題目允許)
        # 例如 68-8=0 -> 6 可以內部移動火柴棒變成 0 -> 08-8=0 (值為 0)
        eq = "68-8=0#"
        expected = "08-8=0#"
        self.assertEqual(solve(eq), expected)
        self.assertEqual(solve_easy(eq), expected)


if __name__ == '__main__':
    # 執行所有測試並輸出詳細結果
    unittest.main(verbosity=2)
