import unittest
from solution_10252 import solve_10252

class TestProblem10252(unittest.TestCase):
    """
    針對 兩條線的距離最小化問題 (UVA 10252/a245) 進行自動化單元測試。
    幫助確認邏輯與邊界條件。
    """
    
    def test_example(self):
        """
        測試題目給定的範例輸入。
        """
        # TODO: 填入範例資料與預期輸出
        self.assertEqual(solve_10252([]), None)

if __name__ == '__main__':
    unittest.main()
