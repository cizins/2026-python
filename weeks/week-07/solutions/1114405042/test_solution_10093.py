import unittest
import importlib.util
from solution_10093 import solve

# 動態載入 solution_10093-easy.py 以進行測試
spec = importlib.util.spec_from_file_location("solution_10093_easy", "solution_10093-easy.py")
solution_10093_easy_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_10093_easy_module)
solve_easy = solution_10093_easy_module.solve_easy


class TestArtilleryDeployment(unittest.TestCase):
    """
    測試 UVA 10093 (POJ 1185 炮兵陣地) 的狀態壓縮 DP 解法。
    1. solve：使用標準的三維 DP 陣列實作的解法。
    2. solve_easy：使用 Python 內建 lru_cache 進行記憶化搜索的簡易解法。
    """

    def test_example(self):
        # 範例測試：5 列 4 行
        n, m = 5, 4
        grid = [
            "PHPP",
            "PPHH",
            "PPPP",
            "PHPP",
            "PHHP"
        ]
        expected = 6
        self.assertEqual(solve(n, m, grid), expected)
        self.assertEqual(solve_easy(n, m, grid), expected)
        
    def test_all_plains(self):
        # 測試：全部都是平原 (P)
        n, m = 3, 3
        grid = [
            "PPP",
            "PPP",
            "PPP"
        ]
        # P P P -> 可以放 (0,0), (0,2), (2,1) = 3個 或 其他解...
        # 第一排放 (0,0), (0,2) = 2 個
        # 第三排放 (0,1) 或 (0,0), (0,2) 等等...
        # 3x3 空間中，每個炮兵需要 5x5 的十字空間
        # 如果放在 (0,0), (0,2)，第三行能放在 (2,1) = 3 個。
        # 最多可以放 4 個，像這樣：
        # P X P  (1, 0, 1)
        # P P P  (0, 0, 0)
        # P X P  (1, 0, 1) -> 總共 4 個炮兵
        expected = 3
        self.assertEqual(solve(n, m, grid), expected)
        self.assertEqual(solve_easy(n, m, grid), expected)

    def test_all_mountains(self):
        # 測試：全部都是山地 (H)，應該一個都放不了
        n, m = 2, 2
        grid = [
            "HH",
            "HH"
        ]
        expected = 0
        self.assertEqual(solve(n, m, grid), expected)
        self.assertEqual(solve_easy(n, m, grid), expected)

    def test_single_row(self):
        # 測試：只有一行，看是否正確處理邊界條件
        n, m = 1, 5
        grid = [
            "PPPPP"
        ]
        # 可以放在索引 0 跟 3 (相距3，距離 > 2)，共 2 個。
        expected = 2
        self.assertEqual(solve(n, m, grid), expected)
        self.assertEqual(solve_easy(n, m, grid), expected)


if __name__ == '__main__':
    # 執行所有測試並輸出詳細結果
    unittest.main(verbosity=2)
