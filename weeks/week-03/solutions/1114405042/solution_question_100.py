"""
題目 100 - Collatz 序列 (3n+1 問題) 的解決方案

============================================================
問題背景
============================================================

Collatz 猜想（又稱 3n+1 問題）：
給定任意正整數 n，重複執行以下操作：
1. 若 n = 1，停止
2. 若 n 是奇數，令 n = 3*n + 1
3. 否則（n 是偶數），令 n = n / 2

猜想：對於任何正整數 n，最終都會到達 1。

Cycle-length 定義：
從 n 出發到達 1 為止的步數，包含 n 和 1。

範例：
    n = 22 的序列：22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    cycle-length(22) = 16

============================================================
問題敘述
============================================================

輸入：兩個整數 i, j（0 < i, j < 1,000,000）
輸出：i, j, 以及區間 [min(i,j), max(i,j)] 內所有數的最大 cycle-length

輸入範例：            輸出結果：
1 10                  1 10 20
100 200               100 200 125
201 210               201 210 89
900 1000              900 1000 174

解釋：
- (1, 10)：區間 [1,10] 內，9 的 cycle-length=20 為最大值
- (100, 200)：區間 [100,200] 內，最大值為 125
- (201, 210)：區間 [201,210] 內，最大值為 89
- (900, 1000)：區間 [900,1000] 內，最大值為 174

============================================================
模組結構
============================================================

本模組包含以下主要組件：

1. CollatzSolution 類：
   - __init__()：初始化求解器
   - _get_cycle_length(n)：計算單個數的 cycle-length（私有方法，帶快取）
   - solve(i, j)：求解區間 [i,j] 的最大 cycle-length（公開方法）
   - clear_cache()：清空快取（用於測試或內存管理）

2. main() 函數：
   - 程式入口點
   - 從標準輸入讀取測試用例
   - 輸出結果到標準輸出

3. solve_batch(test_cases) 函數：
   - 批量求解（用於測試或自動化）
   - 接受測試用例列表，返回結果列表

============================================================
性能分析
============================================================

時間複雜度：
- 單次 cycle-length 計算：平均 O(log n)
- 區間 [i, j] 查詢：O((j-i) * log(avg(n)))
- 帶快取時：重複查詢相同值時只需 O(1)

空間複雜度：
- 快取大小：O(總計算過的數個數)

優化策略：
1. 記憶化（Memoization）：存儲已計算的 cycle-length
2. 快取重用：區間查詢時，不同數的序列常有重疊
3. 區間順序無關性：支持任意輸入順序

============================================================
使用範例
============================================================

方法 1：交互式輸入（從標準輸入讀取）
    python solution_question_100.py
    # 輸入：
    # 1 10
    # 100 200
    # 輸出：
    # 1 10 20
    # 100 200 125

方法 2：批量求解程式化方式
    from solution_question_100 import solve_batch
    
    test_cases = [(1, 10), (100, 200), (201, 210)]
    results = solve_batch(test_cases)
    # results = [(1, 10, 20), (100, 200, 125), (201, 210, 89)]

方法 3：單次求解
    from solution_question_100 import CollatzSolution
    
    solver = CollatzSolution()
    i, j, max_cycle = solver.solve(1, 10)
    print(f"最大 cycle-length: {max_cycle}")  # 輸出：20

方法 4：自定義初始化和多次查詢
    solver = CollatzSolution()
    result1 = solver.solve(1, 10)
    result2 = solver.solve(100, 200)  # 複用之前的快取
    solver.clear_cache()  # 清空快取
    result3 = solver.solve(900, 1000)

============================================================
演算法詳解
============================================================

Cycle-length 計算算法（遞迴 + 記憶化）：

def _get_cycle_length(n):
    if n 已在快取中:
        return 快取[n]
    
    if n == 1:
        return 1
    else if n 是奇數:
        result = 1 + _get_cycle_length(3*n + 1)
    else:  # n 是偶數
        result = 1 + _get_cycle_length(n // 2)
    
    快取[n] = result
    return result

區間查詢算法：

def solve(i, j):
    start = min(i, j)
    end = max(i, j)
    max_cycle = 0
    
    for num in range(start, end + 1):
        cycle = _get_cycle_length(num)
        max_cycle = max(max_cycle, cycle)
    
    return (i, j, max_cycle)

============================================================
注意事項
============================================================

1. 輪出輸入順序：solve(i, j) 的返回值中，i 和 j 保持原始輸入順序
2. 區間範圍：計算時會自動將 [i, j] 標準化為 [min(i,j), max(i,j)]
3. 快取共享：多個查詢共享同一個求解器的快取，提高效率
4. 異常安全：main() 函數會跳過格式不正確的輸入行，繼續處理後續輸入

============================================================
"""


class CollatzSolution:
    """
    Collatz 序列問題的高效求解器。
    
    類的核心職責：
    1. 計算單個數 n 的 cycle-length（通過 _get_cycle_length 方法）
    2. 查詢區間 [i, j] 內的最大 cycle-length（通過 solve 方法）
    3. 使用記憶化快取優化重複計算
    
    主要優化：
    - 記憶化（Memoization）：使用 _cache 字典存儲已計算的 cycle-length
      這在查詢區間時特別有效，因為不同數的序列往往有重疊。
      例如：計算 100~200 區間時，許多序列會交集，快取會重複使用這些結果。
    
    - 區間處理：支持任意順序的區間端點
      solve(1, 10) 和 solve(10, 1) 會得到相同的結果
    
    內部結構：
    - _cache (dict)：鍵是數 n，值是其 cycle-length
      {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, ...}
    
    使用場景：
    - 單次查詢：solver.solve(1, 10)
    - 多次獨立查詢：多次呼叫 solve() 方法
    - 快取清空：調用 clear_cache() 方法重置
    
    時間複雜度分析：
    - 第一次計算 cycle-length(n)：平均 O(log n)
    - 快取命中（重複計算）：O(1)
    - 區間查詢 [i, j]：O((j-i) * log(avg(n)))，但帶快取優化會更快
    
    空間複雜度：
    - O(總計算過的數的個數)，用於存儲快取字典
    """
    
    def __init__(self):
        """
        初始化求解器，建立快取字典。
        
        建立時初始狀態：
        - 快取為空字典（{}）
        - 沒有預先計算任何值
        
        每次創建新的求解器實例都會有獨立的快取，
        這在多個獨立問題求解時很有用。
        
        範例：
            solver1 = CollatzSolution()  # 快取為空
            solver1.solve(1, 10)          # 快取被填充
            solver2 = CollatzSolution()  # 快取為空（獨立實例）
        """
        # 初始化快取字典，用於存儲已計算的 cycle-length
        # 鍵（key）：整數 n
        # 值（value）：n 的 cycle-length
        # 例如：self._cache[22] = 16 表示 22 的 cycle-length 是 16
        self._cache = {}
    
    def _get_cycle_length(self, n):
        """
        遞迴計算 cycle-length，帶有記憶化。
        
        此方法實現 Collatz 序列的長度計算：
        - 基礎情況：當 n=1 時，返回 1（序列長度為 1）
        - 奇數：呼叫 3*n+1 後的結果，並加上 1（當前步驟）
        - 偶數：呼叫 n/2 後的結果，並加上 1（當前步驟）
        
        記憶化優化：使用 _cache 字典存儲已計算的結果，避免重複計算。
        這在查詢區間內多個數時特別有效，因為它們的序列往往有重疊。
        
        Args:
            n (int): 輸入的正整數
            
        Returns:
            int: n 的 cycle-length（從 n 到 1 的步數，包含 n 和 1）
            
        範例：
            cycle-length(22) = 16
            序列：22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        """
        # 快取查詢：若已計算過，直接返回（時間複雜度 O(1)）
        if n in self._cache:
            return self._cache[n]
        
        # 基礎情況：n = 1 時，序列長度為 1
        if n == 1:
            return 1
        
        # 遞迴計算：根據 Collatz 序列規則
        if n % 2 == 1:
            # 奇數情況：n = 3*n + 1
            # 例如 n=5: 5 → 16 → ... （5 是奇數，先變成 3*5+1=16）
            result = 1 + self._get_cycle_length(3 * n + 1)
        else:
            # 偶數情況：n = n / 2
            # 例如 n=10: 10 → 5 → ... （10 是偶數，變成 10/2=5）
            result = 1 + self._get_cycle_length(n // 2)
        
        # 將計算結果存入快取，供未來查詢使用
        # 這是動態規劃中的「備忘錄法」，減少重複計算
        self._cache[n] = result
        return result
    
    def solve(self, i, j):
        """
        求解給定區間的最大 cycle-length。
        
        核心邏輯：
        1. 標準化區間：將 i, j 轉換為 start, end，其中 start ≤ end
        2. 遍歷區間：對區間 [start, end] 內的每個數進行計算
        3. 追蹤最大值：記錄所有 cycle-length 中的最大值
        
        時間複雜度分析：
        - 不帶快取：O((j-i) * log(avg(n)))（avg 表示區間平均值）
        - 帶快取：通常顯著快於上述時間，因為重複的序列會被快取
        
        空間複雜度：O(總計算過的數的個數)，用於存儲快取
        
        Args:
            i (int): 區間端點 1（順序任意）
            j (int): 區間端點 2（順序任意）
            
        Returns:
            tuple: (i, j, max_cycle_length)
            - i, j：原始輸入
            - max_cycle_length：區間內所有數的 cycle-length 最大值
            
        範例：
            solve(1, 10) 會計算 [1,2,3,...,10] 的所有 cycle-length，
            返回最大值（在這個範圍內是 9 的 cycle-length=20）
        """
        # 標準化區間順序，確保 start ≤ end
        # 這樣應對輸入順序顛倒的情況，如 solve(10, 1) 會被轉換為 [1, 10]
        start = min(i, j)
        end = max(i, j)
        
        # 初始化最大值為 0
        # 在區間遍歷中，它會被更新為實際的最大 cycle-length
        max_cycle = 0
        
        # 遍歷區間內的每一個數
        # 範圍是 [start, end]，包含 start 和 end
        for num in range(start, end + 1):
            # 計算當前數的 cycle-length
            # _get_cycle_length 會使用快取來加速計算
            cycle = self._get_cycle_length(num)
            
            # 更新最大值
            # max() 內建函數返回較大的值
            max_cycle = max(max_cycle, cycle)
        
        # 返回原始輸入 i, j（不是標準化後的 start, end）
        # 這是為了保持輸入輸出的對應關係
        return (i, j, max_cycle)
    
    def clear_cache(self):
        """
        清空快取，重置求解器狀態。
        
        使用場景：
        1. 測試之間的獨立性：每個測試前清空快取，確保測試不受其他測試的影響
        2. 內存管理：在處理完大量數據後清空快取，釋放內存
        3. 條件重新開始：需要重新計算但复用同一個求解器實例時
        
        效果：
        - 清空 _cache 字典
        - 求解器回到初始化狀態
        - 後續計算會重新構建快取
        
        範例：
            solver = CollatzSolution()
            solver.solve(1, 100)      # 快取被填充
            solver.clear_cache()       # 快取被清空
            solver.solve(200, 300)     # 硬盤快取，從頭開始計算
        
        時間複雜度：O(n)，其中 n 是快取中的元素個數
        """
        # 清空快取字典（返回空字典）
        # 這會移除所有已存儲的 cycle-length 計算結果
        self._cache.clear()


def main():
    """
    主程式：從標準輸入讀取測試用例，輸出結果。
    
    程式流程：
    1. 初始化求解器（CollatzSolution 實例）
    2. 無限迴圈，逐行讀取標準輸入
    3. 對每行輸入進行解析：期望格式為「整數 整數」
    4. 呼叫 solve() 方法求解
    5. 輸出結果到標準輸出
    6. 遇到 EOF（End of File）時正常終止
    
    輸入格式：
    - 每行包含兩個整數 i, j（用空格分隔）
    - 0 < i, j < 1,000,000（根據題目要求）
    - 示例：
        1 10
        100 200
        201 210
    
    輸出格式：
    - 每行輸出一個結果，格式為：i j max_cycle_length
    - 其中 max_cycle_length 是 [min(i,j), max(i,j)] 區間內的最大 cycle-length
    - 示例：
        1 10 20
        100 200 125
        201 210 89
    
    異常處理：
    - 跳過空行：避免在空白行上產生錯誤
    - 跳過格式錯誤的行：若不是兩個整數，跳過該行
    - 跳過轉換失敗的行：若不能轉換為整數，跳過該行
    - 正常結束：遇到 EOF 時程式正常終止，而不是產生錯誤
    """
    # 創建求解器實例
    # 每次 main() 呼叫都會建立一個新的求解器，有獨立的快取
    solver = CollatzSolution()
    
    try:
        # 無限迴圈讀取標準輸入
        # 直到遇到 EOFError（文件結尾或 Ctrl+D）
        while True:
            # 讀取一行輸入並移除首尾空白（包括換行符）
            line = input().strip()
            
            # 跳過空行
            # 空行通常是誤輸入或格式問題
            if not line:
                continue
            
            # 按空格分割字符串為多個部分
            # 例如 "1 10" 會分割為 ['1', '10']
            parts = line.split()
            
            # 驗證輸入格式：必須恰好有 2 個部分
            # 如果不符合，跳過此行並繼續讀取下一行
            if len(parts) != 2:
                continue
            
            try:
                # 嘗試將字符串轉換為整數
                # 如果轉換失敗（例如輸入非數字），會拋出 ValueError
                i = int(parts[0])
                j = int(parts[1])
                
                # 呼叫求解器的 solve() 方法
                # 返回值是一個三元組 (i, j, max_cycle_length)
                result_i, result_j, max_cycle = solver.solve(i, j)
                
                # 輸出結果到標準輸出
                # 格式化為「i j max_cycle_length」，用空格分隔
                # f-string 是 Python 3.6+ 的格式化方式
                print(f"{result_i} {result_j} {max_cycle}")
                
            except ValueError:
                # 若轉換失敗（非數字輸入），跳過此行
                # 例如輸入 "abc def" 或 "1 def" 都會被跳過
                continue
    
    except EOFError:
        # 遇到 EOF（檔案結尾或 Ctrl+D）時的正常終止
        # 此異常表示沒有更多輸入，這是預期的正常結束情況
        # 不需要輸出任何錯誤訊息，程式簡單地退出
        pass


def solve_batch(test_cases):
    """
    批量求解測試用例（用於測試或自動化）。
    
    此函數適用於需要一次性處理多個測試用例的場景，
    例如單元測試、批量驗證、性能測試等。
    
    與 main() 函數的區別：
    - main()：從標準輸入讀取，逐個輸出到標準輸出
    - solve_batch()：直接接受測試用例列表，返回結果列表
    
    用途：
    - 測試驗證（在單元測試中呼叫）
    - 自動評分系統
    - 批量數據處理
    - 性能基準測試
    
    Args:
        test_cases (list): 包含 (i, j) 元組的列表
                          例如：[(1, 10), (100, 200), (201, 210)]
        
    Returns:
        list: 包含 (i, j, max_cycle_length) 元組的結果列表
             與輸入的順序對應
             例如：[(1, 10, 20), (100, 200, 125), (201, 210, 89)]
    
    時間複雜度：
    - 取決於測試用例的數量和各自的區間大小
    - 多個測試用例共享同一快取，後續查詢會受益於前面的計算結果
    
    範例：
        test_cases = [(1, 10), (100, 200)]
        results = solve_batch(test_cases)
        # results = [(1, 10, 20), (100, 200, 125)]
    """
    # 創建新的求解器實例
    # 多次呼叫 solve_batch() 會創建多個獨立的求解器，各自有獨立的快取
    solver = CollatzSolution()
    
    # 初始化結果列表
    # 將逐個添加每個測試用例的結果
    results = []
    
    # 遍歷所有測試用例
    # 每個測試用例都是一個 (i, j) 元組
    for i, j in test_cases:
        # 呼叫 solve() 方法求解當前測試用例
        # 返回 (i, j, max_cycle_length) 元組
        result = solver.solve(i, j)
        
        # 將結果添加到結果列表
        # 結果列表會保持與輸入的對應順序
        results.append(result)
    
    # 返回所有結果
    return results


if __name__ == '__main__':
    main()
