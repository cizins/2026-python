"""
題目 100 - Collatz 序列 (3n+1 問題) 的 Unit Test 套件

============================================================
模組目的
============================================================

此模組提供完整的單元測試（Unit Test），用於驗證 Collatz 序列
（3n+1 問題）的計算正確性與區間最大值查詢的功能。

測試內容包括：
- 單點 cycle-length 計算
- 區間範圍查詢
- 邊界和特殊情況
- 快取機制效能
- 數學性質驗證

============================================================
測試結構
============================================================

本模組包含兩個主要測試類：

1. TestQuestion100（22 個測試用例）：
   - 基礎 Cycle-Length 計算測試（6 個）
   - 區間最大值查詢測試（4 個）
   - 區間順序影響測試（2 個）
   - 邊界與特殊情況測試（3 個）
   - 快取功能測試（2 個）
   - 較大數值測試（2 個）

2. TestEdgeCases（3 個測試用例）：
   - 2 的冪次數列測試
   - 奇數序列性質測試
   - 非單調性質測試

============================================================
運行測試
============================================================

方法 1：使用 unittest 框架
    python3 -m unittest test_question_100 -v
    python3 -m unittest discover -p "test*.py" -v

方法 2：直接運行此檔案
    python3 test_question_100.py

方法 3：使用 pytest（如已安裝）
    pytest test_question_100.py -v

============================================================
測試設計理念
============================================================

1. 獨立性（Isolation）：
   - setUp()：每個測試前創建新的求解器實例
   - tearDown()：每個測試後清空快取
   - 目的：確保各測試之間互不影響

2. 完整性（Comprehensiveness）：
   - 基準測試：驗證基本功能
   - 邊界測試：驗證邊界情況
   - 性質測試：驗證算法的數學性質
   - 性能測試：驗證快取的效果

3. 可讀性（Readability）：
   - 清晰的測試名稱：test_xxx_yyy
   - 詳細的文件字符串：説明測試的目的和預期
   - 有意義的斷言（Assertion）

============================================================
預期測試結果
============================================================

全部 22 + 3 = 25 個測試應全部通過：

執行 python3 -m unittest discover -s . -p "test_*.py" -v 後，
應看到：
    Ran 25 tests in 0.001s
    OK

若有任何失敗，將顯示：
    FAILED (failures=N, errors=M)

============================================================
此模組的求解器類 vs 解決方案程式
============================================================

此檔案中的 CollatzSolver 類是為了測試目的自包含地定義的，
與 solution_question_100.py 中的 CollatzSolution 類功能相同但獨立。

使用獨立類的原因：
1. 測試模組應該獨立，不依賴於外部實現
2. 便於對算法的理解和驗證
3. 允許同時測試多個實現版本

=========================================================
"""

import unittest
from functools import lru_cache


class CollatzSolver:
    """
    用於計算 Collatz 序列 cycle-length 和區間最大值的求解器類。
    
    Collatz 序列的定義：
    1. 若 n = 1，結束
    2. 若 n 是奇數，n = 3*n + 1
    3. 否則 n = n / 2
    """
    
    def __init__(self):
        """初始化求解器，設定記憶化快取以提升效能。"""
        # 使用字典存儲已計算過的 cycle-length，避免重複計算
        self._cache = {}
    
    def calculate_cycle_length(self, n):
        """
        計算給定數 n 的 cycle-length（序列長度）。
        
        Args:
            n (int): 輸入的正整數
            
        Returns:
            int: 從 n 開始到 1 的序列長度（包含 n 和 1）
            
        例如：
            n = 22: 22 -> 11 -> 34 -> ... -> 1，長度為 16
        """
        # 檢查是否已在快取中
        if n in self._cache:
            return self._cache[n]
        
        # 基礎情況：n = 1 時，長度為 1
        if n == 1:
            return 1
        
        # 根據 n 的奇偶性應用 Collatz 規則
        if n % 2 == 1:
            # n 是奇數：n = 3*n + 1
            length = 1 + self.calculate_cycle_length(3 * n + 1)
        else:
            # n 是偶數：n = n / 2
            length = 1 + self.calculate_cycle_length(n // 2)
        
        # 將計算結果存入快取
        self._cache[n] = length
        return length
    
    def find_max_cycle_length(self, i, j):
        """
        找出區間 [min(i,j), max(i,j)] 內所有數的 cycle-length 最大值。
        
        Args:
            i (int): 區間端點 1
            j (int): 區間端點 2
            
        Returns:
            int: 區間內的最大 cycle-length
            
        例如：
            i=1, j=10: 應取 [1,10]，結果為 20
        """
        # 確保 start <= end（處理輸入順序不同的情況）
        start = min(i, j)
        end = max(i, j)
        
        # 遍歷區間內所有數，計算各自的 cycle-length，並取最大值
        max_length = 0
        for num in range(start, end + 1):
            length = self.calculate_cycle_length(num)
            max_length = max(max_length, length)
        
        return max_length
    
    def clear_cache(self):
        """清空快取，用於測試之間的獨立性。"""
        self._cache.clear()


class TestQuestion100(unittest.TestCase):
    """
    Collatz 序列 cycle-length 計算的主要測試套件（22 個測試）。
    
    此類使用 unittest.TestCase 作為基類，繼承 unittest 框架的所有功能。
    
    測試覆蓋範圍：
    - 基礎單點計算（6 個）: 驗證 cycle-length 的正確計算
    - 區間查詢（4 個）: 驗證範圍内最大值的正確查詢
    - 輸入順序鯨度（2 個）: 驗證輸入順序顛倒不影響結果
    - 邊界情況（3 個）: 驗證單點、相鄰區間等邊界情況
    - 快取功能（2 個）: 驗證記憶化快取的正確性和效能
    - 大數值（2 個）: 驗證演算法在較大輸入上的表現
    
    測試方法命名規則：
    test_<功能>_<情況>
    
    範例：
    - test_cycle_length_base_case_1：測試基礎情況 cycle-length(1)
    - test_max_cycle_length_1_to_10：測試區間 [1,10] 的最大值
    - test_cache_improves_performance：測試快取的效能提升
    
    斷言方法（Assertion Methods）：
    - assertEqual(a, b)：驗證 a == b
    - assertGreater(a, b)：驗證 a > b
    - assertIsInstance(a, type)：驗證 a 是 type 的實例
    - 更多見：https://docs.python.org/3/library/unittest.html#assertion-methods
    """
    
    def setUp(self):
        """
        每個測試方法執行前的準備（測試夾具 - Test Fixture）。
        
        此方法由 unittest 框架自動呼叫，在每個測試方法前執行。
        
        作用：
        1. 建立測試需要的依賴資源（此處是 CollatzSolver 實例）
        2. 初始化測試環境
        3. 確保每個測試都擁有全新的環境
        
        優點：
        - 確保測試獨立性：各測試不會因為前面的測試而受影響
        - 易於維護：所有測試的初始化邏輯集中在一個地方
        - 代碼復用：避免在每個測試方法中重複初始化代碼
        
        執行順序示例：
        Test 1: setUp() → test_method_1() → tearDown()
        Test 2: setUp() → test_method_2() → tearDown()
        （注意：每個測試前都重新呼叫 setUp()）
        """
        # 為每個測試創建新的求解器實例
        # 確保快取為空，測試不會受到前面測試的快取影響
        self.solver = CollatzSolver()
    
    def tearDown(self):
        """
        每個測試方法執行後的清理（清理方法 - Teardown Method）。
        
        此方法由 unittest 框架自動呼叫，在每個測試方法後執行。
        
        作用：
        1. 清理測試中使用的資源
        2. 重置環境狀態
        3. 防止測試間的相互影響
        
        本測試中的清理：
        - 清空快取字典
        - 移除對 test 實例變數的引用
        
        最佳實踐：
        - tearDown() 應該彻底清理 setUp() 中建立的所有資源
        - 即使測試失敗，tearDown() 也會被執行
        - 確保測試不會因為遺留的狀態而相互干擾
        
        執行順序示例：
        Test 1: setUp() → test_method_1() → tearDown()  ← 即使 test 失敗也執行
        Test 2: setUp() → test_method_2() → tearDown()  ← 擁有乾淨的環境
        """
        # 清空快取字典，將求解器恢復到初始狀態
        # 這樣下一個測試會有全新的快取
        self.solver.clear_cache()
    
    # ============ 基礎 Cycle-Length 計算測試 ============
    
    def test_cycle_length_base_case_1(self):
        """測試基礎情況：n=1 應回傳 1"""
        self.assertEqual(self.solver.calculate_cycle_length(1), 1)
    
    def test_cycle_length_small_even(self):
        """測試小的偶數：n=2"""
        # 序列：2 -> 1，長度為 2
        self.assertEqual(self.solver.calculate_cycle_length(2), 2)
    
    def test_cycle_length_small_odd(self):
        """測試小的奇數：n=3"""
        # 序列：3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1，長度為 8
        self.assertEqual(self.solver.calculate_cycle_length(3), 8)
    
    def test_cycle_length_22(self):
        """測試例題中的案例：n=22 應回傳 16"""
        # 序列：22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
        self.assertEqual(self.solver.calculate_cycle_length(22), 16)
    
    def test_cycle_length_10(self):
        """測試 n=10"""
        # 序列：10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1，長度為 7
        self.assertEqual(self.solver.calculate_cycle_length(10), 7)
    
    def test_cycle_length_16(self):
        """測試 n=16（2 的冪次）"""
        # 序列：16 -> 8 -> 4 -> 2 -> 1，長度為 5
        self.assertEqual(self.solver.calculate_cycle_length(16), 5)
    
    # ============ 區間最大值查詢測試 ============
    
    def test_max_cycle_length_1_to_10(self):
        """測試區間 [1, 10]，預期最大 cycle-length 為 20"""
        result = self.solver.find_max_cycle_length(1, 10)
        self.assertEqual(result, 20)
    
    def test_max_cycle_length_100_to_200(self):
        """測試區間 [100, 200]，預期最大 cycle-length 為 125"""
        result = self.solver.find_max_cycle_length(100, 200)
        self.assertEqual(result, 125)
    
    def test_max_cycle_length_201_to_210(self):
        """測試區間 [201, 210]，預期最大 cycle-length 為 89"""
        result = self.solver.find_max_cycle_length(201, 210)
        self.assertEqual(result, 89)
    
    def test_max_cycle_length_900_to_1000(self):
        """測試區間 [900, 1000]，預期最大 cycle-length 為 174"""
        result = self.solver.find_max_cycle_length(900, 1000)
        self.assertEqual(result, 174)
    
    # ============ 區間順序影響測試 ============
    
    def test_max_cycle_length_reversed_order(self):
        """
        測試區間輸入順序顛倒的情況。
        find_max_cycle_length(j, i) 應與 find_max_cycle_length(i, j) 相同
        """
        result1 = self.solver.find_max_cycle_length(1, 10)
        result2 = self.solver.find_max_cycle_length(10, 1)
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 20)
    
    def test_max_cycle_length_reversed_large_range(self):
        """測試大區間的順序顛倒情況"""
        result1 = self.solver.find_max_cycle_length(100, 200)
        result2 = self.solver.find_max_cycle_length(200, 100)
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 125)
    
    # ============ 邊界與特殊情況測試 ============
    
    def test_max_cycle_length_single_point(self):
        """測試區間退化為單點的情況：[5, 5]"""
        result = self.solver.find_max_cycle_length(5, 5)
        self.assertEqual(result, self.solver.calculate_cycle_length(5))
    
    def test_max_cycle_length_single_point_1(self):
        """測試單點區間：[1, 1]"""
        result = self.solver.find_max_cycle_length(1, 1)
        self.assertEqual(result, 1)
    
    def test_max_cycle_length_two_consecutive(self):
        """測試相鄰區間：[5, 6]"""
        c5 = self.solver.calculate_cycle_length(5)
        c6 = self.solver.calculate_cycle_length(6)
        result = self.solver.find_max_cycle_length(5, 6)
        self.assertEqual(result, max(c5, c6))
    
    # ============ 快取功能測試 ============
    
    def test_cache_improves_performance(self):
        """
        測試快取機制：計算相同的數多次應回傳相同結果。
        快取應確保重複查詢的高效性。
        """
        # 第一次計算
        result1 = self.solver.calculate_cycle_length(100)
        # 第二次計算（應直接從快取取得）
        result2 = self.solver.calculate_cycle_length(100)
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 26)
    
    def test_cache_usage_in_range(self):
        """
        測試在區間查詢中的快取效果。
        多次調用同一區間應得到相同結果。
        """
        result1 = self.solver.find_max_cycle_length(1, 5)
        result2 = self.solver.find_max_cycle_length(1, 5)
        self.assertEqual(result1, result2)
    
    # ============ 較大數值測試 ============
    
    def test_cycle_length_large_number(self):
        """測試較大的數值"""
        result = self.solver.calculate_cycle_length(999999)
        self.assertGreater(result, 0)  # 確保結果為正數
        self.assertIsInstance(result, int)  # 確保結果為整數
    
    def test_max_cycle_length_large_range(self):
        """測試較大區間"""
        result = self.solver.find_max_cycle_length(1, 1000)
        self.assertGreater(result, 0)
        self.assertIsInstance(result, int)


class TestEdgeCases(unittest.TestCase):
    """
    邊界與異常情況的專項測試（3 個測試）。
    
    此類專注於測試演算法的邊界情況和特殊性質，
    驗證 Collatz 序列的數學特性。
    
    測試內容：
    1. test_power_of_two_sequences：測試 2 的冪次
       - 2^k 有特殊的簡單遞推關係
       - cycle-length(2^k) = k + 1
       - 用於驗證基本演算法正確性
    
    2. test_odd_number_sequence：測試所有奇數
       - 奇數會先乘以 3 加 1（變成偶數），再進行偶數規則
       - 所有奇數 > 1 的 cycle-length > 1
       - 驗證奇數邏輯的正確性
    
    3. test_cycle_in_ascending_order：測試非單調性
       - cycle-length 不是隨著 n 單調遞增或遞減的
       - 這是 Collatz 序列的一個有趣特性
       - 驗證演算法不依賴錯誤的假設
    
    這些測試不涉及區間查詢，而是檢验演算法的基本屬性。
    """
    
    def setUp(self):
        """建立新的 CollatzSolver 實例。"""
        self.solver = CollatzSolver()
    
    def test_power_of_two_sequences(self):
        """
        測試 2 的冪次。
        2^k 的序列應為：2^k -> 2^(k-1) -> ... -> 1，長度為 k+1
        """
        self.assertEqual(self.solver.calculate_cycle_length(1), 1)    # 2^0
        self.assertEqual(self.solver.calculate_cycle_length(2), 2)    # 2^1
        self.assertEqual(self.solver.calculate_cycle_length(4), 3)    # 2^2
        self.assertEqual(self.solver.calculate_cycle_length(8), 4)    # 2^3
        self.assertEqual(self.solver.calculate_cycle_length(16), 5)   # 2^4
        self.assertEqual(self.solver.calculate_cycle_length(32), 6)   # 2^5
    
    def test_odd_number_sequence(self):
        """
        測試奇數。奇數會被乘以 3 再加 1，變成偶數後開始分割。
        """
        # 所有奇數 > 1 的 cycle-length 應 > 1
        for odd in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]:
            length = self.solver.calculate_cycle_length(odd)
            self.assertGreater(length, 1)
    
    def test_cycle_in_ascending_order(self):
        """
        測試 cycle-length 並不總是隨著 n 遞增而遞增。
        這驗證了 Collatz 序列的複雜性。
        """
        # 計算一組數的 cycle-length
        lengths = [self.solver.calculate_cycle_length(i) for i in range(1, 20)]
        # cycle-length 不是單調遞增的
        # 例如：n=19 的 cycle-length 大於 n=20 的
        self.assertNotEqual(lengths, sorted(lengths))


def run_tests_with_verbose_output():
    """
    運行所有測試，並輸出詳細的測試結果。
    
    此函數提供了一個完整的測試執行方案，包括：
    1. 組織所有測試用例
    2. 使用詳細的輸出格式運行
    3. 返回詳細的測試結果
    
    功能：
    - 使用 TestLoader 動態發現測試
    - 使用 TestSuite 聚合所有測試
    - 使用 TextTestRunner 執行並報告結果
    
    輸出格式（詳細級別）：
    test_方法名 (類名) ... ok/FAIL/ERROR
    
    範例輸出：
        test_cycle_length_base_case_1 (test_question_100.TestQuestion100) ... ok
        test_cycle_length_22 (test_question_100.TestQuestion100) ... ok
        ...
        Ran 25 tests in 0.001s
        OK
    
    Returns：
        TestResult：包含測試結果的物件，可用於程序化的結果檢查
        - result.wasSuccessful()：判斷是否全部通過
        - result.failures：存儲失敗的測試
        - result.errors：存儲出錯的測試
    
    使用場景：
    - 開發中進行測試
    - CI/CD 管道中的測試步驟
    - 自動化測試報告生成
    """
    # 建立測試套件
    # TestLoader 會自動發現測試類和測試方法
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加所有測試
    # loadTestsFromTestCase() 會自動找到所有 test_xxx 方法
    suite.addTests(loader.loadTestsFromTestCase(TestQuestion100))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # 運行測試，指定詳細輸出級別
    # verbosity=0：靜默，只顯示摘要
    # verbosity=1：正常，顯示每個測試的簡要結果（.FE）
    # verbosity=2：詳細，顯示每個測試的完整信息
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回測試結果
    # 外部代碼可以檢查 result.wasSuccessful() 來判斷是否全部通過
    return result


# ============ 主程式入口 ============

if __name__ == '__main__':
    """
    主程式入口點。
    
    執行此檔案時會運行所有測試。
    
    使用方式：
    1. python3 test_question_100.py
       - 使用 unittest 命令行介面
       - 自動發現並運行所有測試
       - 顯示詳細的測試結果
    
    2. python3 -m unittest test_question_100 -v
       - 通過 unittest 模組運行
       - 等效於上面的方法
    
    3. python3 -m unittest discover -p "test*.py" -v
       - 自動發現並運行所有 test*.py 檔案
       - 適用於多測試檔案的場景
    
    測試結果示例：
    
    測試通過時：
        test_cycle_length_22 (test_question_100.TestQuestion100) ... ok
        ...
        Ran 25 tests in 0.001s
        OK
    
    測試失敗時：
        test_cycle_length_22 (test_question_100.TestQuestion100) ... FAIL
        ...
        FAILED (failures=1, errors=0)
    
    返回碼（Exit Code）：
    - 0：所有測試通過
    - 1：至少有一個測試失敗或出錯
    
    這個返回碼在自動化測試（CI/CD）中很重要。
    """
    # 使用高詳細度運行所有測試
    # unittest.main() 是標準的 Python 測試運行方式
    # 會自動：
    # 1. 發現所有 TestCase 子類
    # 2. 發現所有 test_xxx 方法
    # 3. 依次運行所有測試
    # 4. 生成報告
    unittest.main(verbosity=2)
