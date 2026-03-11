"""
============================================================
題目 100 - Collatz 序列簡化版的單元測試

============================================================
測試說明
============================================================

此測試模組驗證簡化版實現的正確性。

相比完整版本，簡化版的測試更加直白：
✓ 只有 1 個測試類（無需複雜的測試組織）
✓ 5 個清晰的測試方法（涵蓋核心功能）
✓ 每個測試針對一個特定場景
✓ 易於理解和記憶

============================================================
測試方法列表
============================================================

1. test_cycle_length_basic
   - 目的：驗證基本的 cycle-length 計算
   - 驗證：1, 2, 3, 22 等單點的正確性
   
2. test_solve_ranges
   - 目的：驗證區間查詢的正確結果
   - 驗證：題目提供的 4 個預期輸出
   
3. test_solve_order_invariant
   - 目的：驗證輸入順序不影響結果
   - 驗證：solve(i,j) == solve(j,i)
   
4. test_single_point
   - 目的：驗證邊界情況（單點區間）
   - 驗證：solve(5,5) 的結果正確
   
5. test_powers_of_two
   - 目的：驗證 2 的冪次的規律
   - 驗證：cycle_length(2^k) = k+1
   - 特點：測試數學規律，有助理解演算法

============================================================
運行測試
============================================================

命令 1：直接運行此檔案
    python3 test_question_100-easy.py

命令 2：使用 unittest 模組運行
    python3 -m unittest test_question_100_easy -v
    (注意：此命令中檔名的連字符會被轉換為下劃線)

命令 3：自動發現並運行所有測試
    python3 -m unittest discover -p "test*.py" -v

============================================================
"""

import unittest
import importlib.util

# 動態加載模組（因為檔名含連字符）
# 標準的 import 無法處理含連字符的模組名
# 因此使用 importlib 動態加載
spec = importlib.util.spec_from_file_location(
    "solution_easy",  # 模組的命名空間（任意名稱）
    "solution_question_100-easy.py"  # 實際檔案位置
)
solution_easy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_easy)

# 從動態加載的模組中提取函數
cycle_length = solution_easy.cycle_length
solve = solution_easy.solve


class TestCollatz(unittest.TestCase):
    """
    Collatz 序列簡化版的單元測試類。
    
    測試框架選擇 unittest（Python 標準庫）的原因：
    ✓ 無需額外安裝（Python 內建）
    ✓ 簡潔易懂（特別適合學員）
    ✓ 功能完整（足以應對大多數測試需求）
    
    測試設計原則：
    ✓ 獨立性：每個測試無相互依賴
    ✓ 簡潔性：每個測試專注於單一功能
    ✓ 直觀性：測試名稱和邏輯清晰易懂
    """
    
    def test_cycle_length_basic(self):
        """
        測試基本的 cycle-length 計算。
        
        驗證內容：
        - cycle-length(1) = 1：終止條件
        - cycle-length(2) = 2：最簡單的序列 2→1
        - cycle-length(3) = 8：包含奇數規則的序列
        - cycle-length(22) = 16：題目提供的例子
        
        這些測試涵蓋了演算法的：
        - 基礎情況（n=1）
        - 偶數規則（n=2）
        - 奇數規則（n=3）
        - 複雜序列（n=22）
        """
        # assertEqual(a, b)：驗證 a == b，若不相等則失敗
        self.assertEqual(cycle_length(1), 1)
        self.assertEqual(cycle_length(2), 2)
        self.assertEqual(cycle_length(3), 8)
        self.assertEqual(cycle_length(22), 16)
    
    def test_solve_ranges(self):
        """
        測試區間查詢的正確性。
        
        驗證內容：
        這 4 個測試用例來自題目本身，是官方的預期輸出。
        若此測試通過，表示解決方案完全正確。
        
        測試用例：
        - [1, 10]：較小區間，最大值為 20
        - [100, 200]：中等區間，最大值為 125
        - [201, 210]：小區間，最大值為 89
        - [900, 1000]：較大區間，最大值為 174
        
        這些測試覆蓋了不同大小的區間，
        有助驗證演算法的一般性和正確性。
        """
        # solve 函數返回三元組，[2] 索引表示第 3 個元素（最大值）
        self.assertEqual(solve(1, 10)[2], 20)
        self.assertEqual(solve(100, 200)[2], 125)
        self.assertEqual(solve(201, 210)[2], 89)
        self.assertEqual(solve(900, 1000)[2], 174)
    
    def test_solve_order_invariant(self):
        """
        測試輸入順序無關性（Order Invariance）。
        
        核心概念：
        solve(i, j) 和 solve(j, i) 應返回相同的結果。
        
        原因：
        題目要求的區間是 [min(i,j), max(i,j)]，
        所以輸入順序不應該影響結果
        （除了返回值中的 i, j 順序會改變）。
        
        這是一個很好的特性測試：
        ✓ 驗證程式的健壯性
        ✓ 驗證邊界情況的處理正確
        ✓ 增強對演算法的信心
        """
        # solve(1, 10) 和 solve(10, 1) 應返回相同的最大值
        # 使用 [2] 索引提取最大值進行比較
        self.assertEqual(solve(1, 10)[2], solve(10, 1)[2])
        self.assertEqual(solve(100, 200)[2], solve(200, 100)[2])
    
    def test_single_point(self):
        """
        測試單點區間的邊界情況。
        
        邊界情況測試的重要性：
        ✓ 驗證程式在邊界條件下的表現
        ✓ 單點區間是最簡化的區間
        ✓ 此時最大值就是該點本身的 cycle-length
        
        驗證邏輯：
        solve(5, 5) 應返回的最大值等於 cycle-length(5)
        因為區間內只有一個數字，其 cycle-length 就是最大值
        """
        # 先計算 5 的 cycle-length
        expected = cycle_length(5)
        # 再驗證 solve(5, 5) 的結果
        # solve 返回 (5, 5, max_len)，[2] 索引是最大值
        result = solve(5, 5)
        # assertEqual：驗證相等
        self.assertEqual(result[2], expected)
    
    def test_powers_of_two(self):
        """
        測試 2 的冪次的 cycle-length 規律。
        
        數學規律：
        cycle-length(2^k) = k + 1
        
        原因分析：
        2^k 的序列是：2^k → 2^(k-1) → ... → 2 → 1
        共 k+1 個數，所以 cycle-length = k+1
        
        例示：
        - 2^0 = 1：1 → stop，長度 1 = 0+1 ✓
        - 2^1 = 2：2 → 1，長度 2 = 1+1 ✓
        - 2^2 = 4：4 → 2 → 1，長度 3 = 2+1 ✓
        - 2^3 = 8：8 → 4 → 2 → 1，長度 4 = 3+1 ✓
        
        此測試的用途：
        ✓ 驗證偶數規則的正確性
        ✓ 測試數學性質，有助理解演算法
        ✓ 快速檢測計算的正確性
        """
        # 遍歷 k = 0, 1, 2, 3, 4, 5
        for k in range(6):
            # 計算 2^k
            n = 2 ** k
            # 驗證 cycle_length(2^k) == k+1
            self.assertEqual(cycle_length(n), k + 1)


# ============================================================
# 程式入口
# ============================================================

if __name__ == '__main__':
    """
    此塊在檔案被直接執行時運行。
    
    unittest.main() 的作用：
    1. 自動發現此模組中的所有 TestCase 子類
    2. 發現每個子類中的所有 test_xxx 方法
    3. 依次執行所有測試
    4. 生成詳細的測試報告
    
    verbosity=2 參數：
    - 0：靜默模式，只顯示摘要
    - 1：正常模式，顯示每個測試的簡要結果（. F E）
    - 2：詳細模式，顯示每個測試的完整信息（推薦用於學習）
    
    輸出示例（verbosity=2）：
        test_cycle_length_basic (__main__.TestCollatz)
        測試基本的 cycle-length 計算。 ... ok
        
        test_powers_of_two (__main__.TestCollatz)
        測試 2 的冪次的 cycle-length 規律。 ... ok
        
        ...（其他測試）...
        
        Ran 5 tests in 0.001s
        OK
    
    返回碼（Exit Code）：
    - 0：所有測試通過
    - 1：至少有一個測試失敗或出錯
    
    此返回碼在自動化測試中很重要（如 CI/CD 管道）。
    """
    # 運行所有測試，詳細輸出模式
    unittest.main(verbosity=2)
