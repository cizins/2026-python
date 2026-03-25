import unittest
from solution_10055 import solve, FenwickTree

class TestFunctionMonotonicity(unittest.TestCase):
    """
    針對 UVA 10055 單調函數複合增減性的單元測試 (Unit Test)
    這是一題考驗區間和（奇偶性）的問題，使用樹狀陣列來確保大資料量時不會 Timeout。
    """

    def test_example_1(self):
        # 測試案例 1: 兩個函數，一開始都是增(0)
        # N=2, Q=4
        n = 2
        queries = [
            (2, 1, 2), # 查詢 [1, 2]，目前都是增(0)，預期 0
            (1, 1),    # 反轉 f_1，現在 f_1 變為減(1)
            (2, 1, 2), # 查詢 [1, 2]，f_1是減(1)，f_2是增(0)，複合後為減(1)，預期 1
            (1, 2),    # 反轉 f_2，現在 f_2 變為減(1)
            (2, 1, 2)  # 查詢 [1, 2]，都是減(1)，負負得正複合後為增(0)，預期 0
        ]
        expected = [0, 1, 0]
        result = solve(n, queries)
        self.assertEqual(result, expected, "預期輸出為 [0, 1, 0]")

    def test_no_changes(self):
        # 測試案例 2: 若完全沒有更改增減性，所有查詢皆應為 0 (增函數)
        n = 10
        queries = [
            (2, 1, 5),
            (2, 2, 8),
            (2, 1, 10)
        ]
        expected = [0, 0, 0]
        result = solve(n, queries)
        self.assertEqual(result, expected, "未改變狀態時預期皆為增函數(0)")

    def test_multiple_flips(self):
        # 測試案例 3: 多次反轉同一個函數，檢查奇偶性是否正確
        n = 5
        queries = [
            (1, 3), # 第 3 個函數變為減 (1)
            (2, 3, 3), # 查詢 [3, 3] -> 1
            (1, 3), # 第 3 個函數變回增 (0)
            (2, 3, 3), # 查詢 [3, 3] -> 0
            (1, 3), # 第 3 個函數又變為減 (1)
            (2, 1, 5)  # 查詢 [1, 5]，此時只有 f_3 是減，結果應為減 (1)
        ]
        expected = [1, 0, 1]
        result = solve(n, queries)
        self.assertEqual(result, expected, "多次反轉同一函數狀態應正確跳換")

    def test_fenwick_tree_logic(self):
        # 測試案例 4: 直接針對 Fenwick Tree (BIT) 的內部邏輯作驗證
        bit = FenwickTree(5)
        # 初始全是 0
        self.assertEqual(bit.query_range(1, 5), 0)
        # 把第 2 個與第 4 個設定為減函數 (1)
        bit.toggle(2)
        bit.toggle(4)
        # 查詢 [1, 3] 範圍，只有第 2 個是減函數，應有 1 個
        self.assertEqual(bit.query_range(1, 3), 1)
        # 查詢 [2, 4] 範圍，第 2 與第 4 個是減函數，應有 2 個
        self.assertEqual(bit.query_range(2, 4), 2)
        # 查詢 [3, 3] 範圍，第 3 個是增函數，應有 0 個
        self.assertEqual(bit.query_range(3, 3), 0)

if __name__ == '__main__':
    # 執行所有測試案例
    unittest.main()
