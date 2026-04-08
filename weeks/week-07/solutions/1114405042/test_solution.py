import unittest
from solution import solve
import importlib.util

# 載入 solution_easy 以進行測試
spec = importlib.util.spec_from_file_location("solution_easy", "solution-easy.py")
solution_easy_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_easy_module)
solve_easy = solution_easy_module.solve_easy


class TestCowSorting(unittest.TestCase):
    """
    測試 UVA 10062 變形 - 乳牛排隊問題 (Lost Cows) 的兩個解法。
    我們有兩種實作方式：
    1. solve：使用 Binary Indexed Tree (BIT) 的 O(N log N) 標準算法。
    2. solve_easy：使用 Python 內建 list 進行 pop 的 O(N^2) 簡單算法。
    """

    def test_example_1(self):
        # 範例 1：5 頭牛，輸入的 count 為 [1, 2, 1, 0]
        # 解釋：
        # 最後一頭牛前面有 0 個比牠小，所以是剩下(1,2,3,4,5)中的第0小(從0算起) => 1。剩下 [2,3,4,5]
        # 第四頭牛前面有 1 個比牠小，所以是剩下(2,3,4,5)中的第1小 => 3。剩下 [2,4,5]
        # 第三頭牛前面有 2 個比牠小，所以是剩下(2,4,5)中的第2小 => 5。剩下 [2,4]
        # 第二頭牛前面有 1 個比牠小，所以是剩下(2,4)中的第1小 => 4。剩下 [2]
        # 第一頭牛前面有 0 個比牠小，所以是剩下(2)中的第0小 => 2。剩下 []
        # 結果為 [2, 4, 5, 3, 1]
        n = 5
        counts = [1, 2, 1, 0]
        expected = [2, 4, 5, 3, 1]
        
        # 測試標準版 (BIT)
        self.assertEqual(solve(n, counts), expected)
        # 測試簡易版 (List)
        self.assertEqual(solve_easy(n, counts), expected)

    def test_small_case(self):
        # 測試只有一頭牛的邊界條件 (此時 counts 為空)
        n = 1
        counts = []
        expected = [1]
        
        self.assertEqual(solve(n, counts), expected)
        self.assertEqual(solve_easy(n, counts), expected)

    def test_ordered_case(self):
        # 測試已經照順序排好的情況 [1, 2, 3] -> 第二個前面1個比牠小，第三個前面2個比牠小
        n = 3
        counts = [1, 2]
        expected = [1, 2, 3]
        
        self.assertEqual(solve(n, counts), expected)
        self.assertEqual(solve_easy(n, counts), expected)
        
    def test_reverse_case(self):
        # 測試反向排列的情況 [3, 2, 1] -> 前面比牠小的數量皆為 0
        n = 3
        counts = [0, 0]
        expected = [3, 2, 1]
        
        self.assertEqual(solve(n, counts), expected)
        self.assertEqual(solve_easy(n, counts), expected)


if __name__ == '__main__':
    # 執行所有測試並輸出詳細結果
    unittest.main(verbosity=2)
