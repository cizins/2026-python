import unittest
import importlib.util
from solution_10170 import solve

# 動態載入 solution_10170-easy.py 以進行測試
spec = importlib.util.spec_from_file_location("solution_10170_easy", "solution_10170-easy.py")
solution_10170_easy_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_10170_easy_module)
solve_easy = solution_10170_easy_module.solve_easy


class TestInfiniteRooms(unittest.TestCase):
    """
    測試 UVA 10170 The Hotel with Infinite Rooms 問題。
    1. solve：使用 Binary Search (二分搜尋法) 可以在 O(log N) 的極快時間內算出答案。
    2. solve_easy：使用 while 迴圈 O(sqrt(D)) 的方式遞減，簡單暴力好記憶。
    """

    def test_example_1(self):
        # 範例測試 1：S=1, D=6
        # 第1天: 1人團 (共住1天) => 累積1天
        # 第2~3天: 2人團 (共住2天) => 累積3天
        # 第4~6天: 3人團 (共住3天) => 累積6天
        # 所以第6天是 3 人團
        s, d = 1, 6
        expected = 3
        self.assertEqual(solve(s, d), expected)
        self.assertEqual(solve_easy(s, d), expected)
        
    def test_example_2(self):
        # 範例測試 2：S=3, D=10
        # 第1~3天: 3人團 (共住3天) => 累積3天
        # 第4~7天: 4人團 (共住4天) => 累積7天
        # 第8~12天: 5人團 (共住5天) => 累積12天
        # 第10天是 5 人團
        s, d = 3, 10
        expected = 5
        self.assertEqual(solve(s, d), expected)
        self.assertEqual(solve_easy(s, d), expected)

    def test_example_3(self):
        # 範例測試 3：S=3, D=14
        # 第1~3天: 3人團 (累積3天)
        # 第4~7天: 4人團 (累積7天)
        # 第8~12天: 5人團 (累積12天)
        # 第13~18天: 6人團 (累積18天)
        # 所以第14天是 6 人團
        s, d = 3, 14
        expected = 6
        self.assertEqual(solve(s, d), expected)
        self.assertEqual(solve_easy(s, d), expected)

    def test_large_case(self):
        # 測試極大數值：D = 10^14，此時 N 會大概是 1.4 * 10^7。
        # Binary Search 會非常快，但 while 迴圈在 Python 裡大約會耗時 0.5 到 1 秒。
        # 我們測試一個中大型的值來確保兩者演算法無誤
        s, d = 10, 100000000  # 一億天
        # 預期答案會是幾萬
        # 我們就只比對這兩個寫法出來的答案是否一致即可
        ans_standard = solve(s, d)
        ans_easy = solve_easy(s, d)
        self.assertEqual(ans_standard, ans_easy)

    def test_edge_case(self):
        # 邊界條件：D 剛好等於起始的 S (第一天)
        s, d = 100, 1
        expected = 100
        self.assertEqual(solve(s, d), expected)
        self.assertEqual(solve_easy(s, d), expected)

    def test_edge_case_2(self):
        # 邊界條件：D 剛好是起始 S 的最後一天
        s, d = 100, 100
        expected = 100
        self.assertEqual(solve(s, d), expected)
        self.assertEqual(solve_easy(s, d), expected)


if __name__ == '__main__':
    # 執行所有測試並輸出詳細結果
    unittest.main(verbosity=2)
