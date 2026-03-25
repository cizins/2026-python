import unittest
from solution import solve

class TestVitosFamily(unittest.TestCase):
    """
    針對 UVA 10041 (Vito's Family) 題目的單元測試 (Unit Test)
    這個測試類別用來驗證 solve 函式是否能正確計算最小總距離。
    """

    def test_example_1(self):
        # 測試案例 1: 兩個親戚，住在門牌號碼 2 和 4
        # 預期輸出: 中位數為 4 (或 2)，總距離為 |2-4| + |4-4| = 2
        relatives = [2, 4]
        result = solve(relatives)
        self.assertEqual(result, 2, "預期距離為 2")

    def test_example_2(self):
        # 測試案例 2: 三個親戚，住在門牌號碼 2, 4, 6
        # 預期輸出: 中位數為 4，總距離為 |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        relatives = [2, 4, 6]
        result = solve(relatives)
        self.assertEqual(result, 4, "預期距離為 4")

    def test_multiple_identical_houses(self):
        # 測試案例 3: 多個親戚住在同一個門牌號碼
        # 預期輸出: 中位數為 10，總距離為 |10-10| + |10-10| + |10-10| = 0
        relatives = [10, 10, 10]
        result = solve(relatives)
        self.assertEqual(result, 0, "全部住在同一個地方，預期距離為 0")

    def test_random_order(self):
        # 測試案例 4: 輸入未排序的門牌號碼
        # 預期輸出: 排序後為 [1, 2, 3, 5, 9]，中位數為 3
        # 總距離為 |1-3| + |2-3| + |3-3| + |5-3| + |9-3| = 2 + 1 + 0 + 2 + 6 = 11
        relatives = [9, 2, 1, 5, 3]
        result = solve(relatives)
        self.assertEqual(result, 11, "預期距離為 11")

    def test_empty_input(self):
        # 測試案例 5: 如果沒有親戚的情況（雖然題目說有 r > 0，但我們可以防呆測試）
        # 預期輸出: 總距離為 0
        relatives = []
        result = solve(relatives)
        self.assertEqual(result, 0, "無親戚時預期距離為 0")

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
