import unittest
from solution_10050 import solve

class TestHartals(unittest.TestCase):
    """
    針對 UVA 10050 (Hartals) 題目的單元測試 (Unit Test)
    這個測試類別用來驗證 solve 函式是否能正確計算罷會造成的損失工作天數。
    """

    def test_example_1(self):
        # 測試案例 1: 根據題目範例
        # N = 14 天，P = 3 個政黨
        # 罷會參數為 3, 4, 8
        # 第一個政黨會在第 3, 6, 9, 12 天罷會
        # 第二個政黨會在第 4, 8, 12 天罷會
        # 第三個政黨會在第 8 天罷會
        # 第 6 天是星期五（假日，不扣工作天）
        # 所以真正的罷會日子是 {3, 4, 8, 9, 12}，共計 5 天。
        n = 14
        p = 3
        hartals = [3, 4, 8]
        result = solve(n, p, hartals)
        self.assertEqual(result, 5, "預期損失工作天數為 5")

    def test_example_2(self):
        # 測試案例 2: 另一種常見的測資
        # N = 100 天，P = 4 個政黨
        # 罷會參數為 12, 15, 25, 40
        n = 100
        p = 4
        hartals = [12, 15, 25, 40]
        result = solve(n, p, hartals)
        # 12, 15, 25, 40 的倍數在 100 以內有：
        # 12: 12, 24, 36, 48, 60, 72, 84, 96
        # 15: 15, 30, 45, 60, 75, 90
        # 25: 25, 50, 75, 100
        # 40: 40, 80
        # 去除 7 的倍數為 6 或 0 的日子 (即 %7 == 6 或 0)
        # 例如 84 % 7 == 0 (去除), 48 % 7 == 6 (去除)...
        # 計算後應該是 15 天。
        self.assertEqual(result, 15, "預期損失工作天數為 15")

    def test_all_fridays_saturdays(self):
        # 測試案例 3: 政黨只在假日罷會（極端情況）
        # 如果罷會參數剛好是 7，雖然題目說不可能是 7 的倍數，但若故意設 14，
        # 所有罷會都在假日 (14 % 7 == 0 星期六) 發生。
        n = 28
        p = 1
        hartals = [14]
        result = solve(n, p, hartals)
        self.assertEqual(result, 0, "假日罷會不扣工作天，預期為 0")

    def test_one_day_hartal(self):
        # 測試案例 4: 每天都在罷會
        # 如果罷會參數為 1 (或接近 1)，那麼所有非假日都會損失。
        # 在 14 天內，有 2 個週末 (2個五、2個六)，所以工作天有 10 天，全部罷會。
        n = 14
        p = 1
        hartals = [1]
        result = solve(n, p, hartals)
        self.assertEqual(result, 10, "每工作天都罷會，預期為 10")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
