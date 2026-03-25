import unittest
from solution_10056 import solve_probability

class TestWhatIsTheProbability(unittest.TestCase):
    """
    針對 UVA 10056 (What is the Probability?) 題目的單元測試
    驗證無限等比級數公式求和是否正確。
    """

    def test_example_1(self):
        # 測試案例 1: N=2, p=0.166666, I=1
        # 在擲骰子的遊戲中，第一個人獲勝的機率
        n = 2
        p = 0.166666
        i = 1
        result = solve_probability(n, p, i)
        # 用 4 位小數格式化後檢查
        formatted = f"{result:.4f}"
        self.assertEqual(formatted, "0.5455", "預期機率為 0.5455")

    def test_example_2(self):
        # 測試案例 2: N=2, p=0.166666, I=2
        # 在擲骰子的遊戲中，第二個人獲勝的機率
        n = 2
        p = 0.166666
        i = 2
        result = solve_probability(n, p, i)
        formatted = f"{result:.4f}"
        self.assertEqual(formatted, "0.4545", "預期機率為 0.4545")

    def test_zero_probability(self):
        # 測試案例 3: 成功機率為 0 的情況
        # 這種情況下任何人都無法獲勝，機率為 0.0000
        n = 3
        p = 0.0
        i = 1
        result = solve_probability(n, p, i)
        formatted = f"{result:.4f}"
        self.assertEqual(formatted, "0.0000", "p=0 時機率應為 0.0000")

    def test_certainty(self):
        # 測試案例 4: 成功機率為 1 的情況
        # 第 1 個人一定會獲勝，其他人為 0
        n = 4
        p = 1.0
        
        # 測試第一個人的機率
        result1 = solve_probability(n, p, 1)
        self.assertEqual(f"{result1:.4f}", "1.0000", "p=1 時第一個人機率應為 1.0000")
        
        # 測試第二個人的機率，由於第一個人必勝，第二個人沒機會
        result2 = solve_probability(n, p, 2)
        self.assertEqual(f"{result2:.4f}", "0.0000", "p=1 時第二個人機率應為 0.0000")

    def test_large_n(self):
        # 測試案例 5: 大數值 N
        n = 1000
        p = 0.01
        i = 500
        result = solve_probability(n, p, i)
        # 不一定要預期特定值，只確認公式運作且數值合理 (不會大於1)
        self.assertTrue(0 <= result <= 1.0, "計算機率必須在 0 到 1 之間")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
