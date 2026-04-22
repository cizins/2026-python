import unittest
from solution_10268 import solve_water_balloons
# 也可以引入 easy 版一起測試
easy_module = __import__("solution_10268-easy")
solve_easy = easy_module.solve_easy

class TestWaterBalloons(unittest.TestCase):
    """
    針對丟水球問題的單元測試。
    測試多種邊界條件與一般情況，確保程式邏輯正確。
    """
    
    def test_basic_cases(self):
        # 基礎測試案例
        self.assertEqual(solve_water_balloons(2, 100), 14)
        self.assertEqual(solve_easy(2, 100), 14)
        
    def test_more_than_63(self):
        # 超過 63 次的測試案例
        # 例如 1 個水球測 100 層樓，需要 100 次，會大於 63
        self.assertEqual(solve_water_balloons(1, 100), "More than 63 trials needed.")
        self.assertEqual(solve_easy(1, 100), "More than 63 trials needed.")

if __name__ == '__main__':
    # 執行測試
    unittest.main()
