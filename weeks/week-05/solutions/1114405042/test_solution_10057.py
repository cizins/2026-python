import unittest
from solution_10057 import solve

class TestMidSummerNightsDream(unittest.TestCase):
    """
    針對 UVA 10057 (Mid-Summer Night's Dream) 題目的單元測試
    """

    def test_example_1_odd(self):
        # 測試案例 1: 奇數個數字
        # 排序後 [1, 2, 3, 4, 5]
        # 中位數只有 3 (min_a=3, max_a=3)
        # 輸入中有 1 個數字落在 [3, 3] 中 (就是 3 本身)
        # 有 (3 - 3 + 1) = 1 種可能的 A
        n = 5
        arr = [5, 4, 3, 2, 1]
        ans1, ans2, ans3 = solve(n, arr)
        self.assertEqual((ans1, ans2, ans3), (3, 1, 1), "奇數個元素應只有 1 種可能 A")

    def test_example_2_even(self):
        # 測試案例 2: 偶數個數字
        # 排序後 [1, 2, 2, 3, 4, 4]
        # 總共 6 個數字，中間是第 2 和第 3 個 (0-based: index 2 和 3)，為 2 和 3
        # 所以 min_A = 2, max_A = 3
        # 陣列中落在 [2, 3] 之間的有 2, 2, 3，共 3 個數字
        # 可能的整數 A 有 2, 3，共 (3 - 2 + 1) = 2 種
        n = 6
        arr = [1, 2, 2, 4, 4, 3]
        ans1, ans2, ans3 = solve(n, arr)
        self.assertEqual((ans1, ans2, ans3), (2, 3, 2), "偶數個元素應正確計算區間與個數")

    def test_identical_elements(self):
        # 測試案例 3: 所有數字相同
        # 排序後 [10, 10, 10, 10]
        # min_A = 10, max_A = 10
        # 落在區間內有 4 個數字
        # 可能的 A 有 1 種
        n = 4
        arr = [10, 10, 10, 10]
        ans1, ans2, ans3 = solve(n, arr)
        self.assertEqual((ans1, ans2, ans3), (10, 4, 1), "全部數字相同應返回自身")

    def test_gap_in_middle(self):
        # 測試案例 4: 中間兩個中位數差距很大
        # 排序後 [10, 20]
        # min_A = 10, max_A = 20
        # 陣列中落在 [10, 20] 之間的有 10, 20 共 2 個數字
        # 可能的 A 有 20 - 10 + 1 = 11 種 (10, 11, ..., 20)
        n = 2
        arr = [10, 20]
        ans1, ans2, ans3 = solve(n, arr)
        self.assertEqual((ans1, ans2, ans3), (10, 2, 11), "中位數有差距時應正確計算出多種可能 A")

if __name__ == '__main__':
    unittest.main()
