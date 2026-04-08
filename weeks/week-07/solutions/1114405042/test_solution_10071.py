import unittest
from solution_10071 import solve
import importlib.util

# 動態載入 solution_10071-easy.py 以進行測試
spec = importlib.util.spec_from_file_location("solution_10071_easy", "solution_10071-easy.py")
solution_10071_easy_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_10071_easy_module)
solve_easy = solution_10071_easy_module.solve_easy


class TestEquation(unittest.TestCase):
    """
    測試 UVA 10071 變形 - 方程式解數量 (a + b + c + d + e = f) 的兩個解法。
    1. solve：使用原生的迴圈及字典 (dict) 的 O(N^3) 標準算法。
    2. solve_easy：使用 Python 內建 itertools 及 collections 的簡潔算法。
    """

    def test_example_1(self):
        # 範例 1：1 個數字。如果是 [0]，那 0+0+0+0+0=0，成立 1 種。
        n = 1
        s = [0]
        expected = 1
        
        # 測試標準版 (迴圈)
        self.assertEqual(solve(n, s), expected)
        # 測試簡易版 (itertools)
        self.assertEqual(solve_easy(n, s), expected)

    def test_example_2(self):
        # 範例 2：集合包含正負數 (因為 a+b+c+d+e = f)
        # s = [-1, 0, 1]
        n = 3
        s = [-1, 0, 1]
        
        # -1, 0, 1 組合比較多，直接比較兩者答案是否一致。
        ans_standard = solve(n, s)
        ans_easy = solve_easy(n, s)
        self.assertEqual(ans_standard, ans_easy)
        
    def test_example_3(self):
        # 範例 3：集合元素較多的情況
        n = 5
        s = [-5, -2, 1, 3, 7]
        
        # 先自己手刻一個暴力的窮舉看答案正不正確
        # 這個寫法非常慢，但 n=5 時 5^6 = 15625 種可能，還可以接受
        count_expected = 0
        for f in s:
            for d in s:
                for e in s:
                    for a in s:
                        for b in s:
                            for c in s:
                                if a + b + c + d + e == f:
                                    count_expected += 1
                                    
        self.assertEqual(solve(n, s), count_expected)
        self.assertEqual(solve_easy(n, s), count_expected)


if __name__ == '__main__':
    # 執行所有測試並輸出詳細結果
    unittest.main(verbosity=2)
