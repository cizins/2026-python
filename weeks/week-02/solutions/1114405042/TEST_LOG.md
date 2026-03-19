# 測試執行日誌 - 第二週 TDD 作業

## 總結

本文件紀錄了第二週作業的測試驅動開發 (TDD) 執行日誌，包含所有三個任務的 紅燈 → 綠燈 → 重構 (Red → Green → Refactor) 循環。

**總測試數：38** (3 個任務 × 每個任務約 13 個測試)
- 所有測試皆遵循 `tests/test_task*.py` 中的 `test_...` 命名慣例

---

## 第一階段：紅燈 (RED) - 初始測試執行 (預期全數失敗)

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試結果總結
```
ERROR: test_task1 (unittest.loader._FailedTest)
ERROR: test_task2 (unittest.loader._FailedTest)
ERROR: test_task3 (unittest.loader._FailedTest)

Ran 3 tests in 0.000s
FAILED (errors=3)
```

### 詳細錯誤訊息

#### test_task1.py
```
ImportError: cannot import name 'deduplicate_sequence' from 'task1_sequence_clean'
```
- **原因**：尚未在 `task1_sequence_clean.py` 中實作 `deduplicate_sequence()` 函式
- **影響**：test_task1.py 中的所有 14 個測試函式皆無法執行

#### test_task2.py
```
ImportError: cannot import name 'rank_students' from 'task2_student_ranking'
```
- **原因**：尚未在 `task2_student_ranking.py` 中實作 `rank_students()` 函式
- **影響**：test_task2.py 中的所有 12 個測試函式皆無法執行

#### test_task3.py
```
ImportError: cannot import name 'summarize_logs' from 'task3_log_summary'
```
- **原因**：尚未在 `task3_log_summary.py` 中實作 `summarize_logs()` 函式
- **影響**：test_task3.py 中的所有 12 個測試函式皆無法執行

### 紅燈階段總結
- **狀態**：✗ 紅燈 (預期中的失敗)
- **總測試數**：38 (3 個匯入錯誤阻擋了所有測試)
- **失敗**：3
- **成功**：0
- **下一步**：在任務模組中實作所有必備的函式

---

## 第二階段：綠燈 (GREEN) - 實作完成

### 實作動作

#### 任務 1：task1_sequence_clean.py
**已實作函式：**
1. `deduplicate_sequence(nums)` - 使用 set 追蹤來移除重複項並保留原始順序
2. `sort_ascending(nums)` - 使用內建的 `sorted()` 
3. `sort_descending(nums)` - 使用 `sorted(reverse=True)`
4. `extract_evens(nums)` - 使用串列生成式 (list comprehension) 與 `num % 2 == 0` 來進行過濾
5. `process_sequence(nums)` - 回傳包含上述四種轉換結果的 tuple

**關鍵設計決策：**
- 使用基於 set 的去重方法 (時間複雜度 O(n)) 而非基於 dict，以保留元素順序
- 將排序委託給 Python 內建的 `sorted()` (穩定排序)
- 保持函式專注於單一職責

#### 任務 2：task2_student_ranking.py
**已實作函式：**
1. `rank_students(input_data)` - 排名邏輯的主要進入點
   - 解析輸入 (n, k, 學生紀錄)
   - 應用多鍵排序：分數↓, 年紀↑, 姓名↑
   - 回傳格式化後的字串，包含前 k 名學生

**關鍵設計決策：**
- 在 lambda 中使用 tuple 進行多鍵排序：`key=lambda x: (-x[1], x[2], x[0])`
- 分數取負值以進行降冪排序；年紀/姓名為正值以進行升冪排序
- 字串格式化以符合預期的輸出格式

#### 任務 3：task3_log_summary.py
**已實作函式：**
1. `summarize_logs(input_data)` - 主要進入點
   - 解析日誌條目 (使用者, 動作 配對)
   - 使用 `defaultdict` 計算使用者事件數量
   - 使用 `Counter` 計算動作頻率
   - 依據次數↓ 然後 姓名↑ 對使用者進行排序
   - 找出最常見的動作

**關鍵設計決策：**
- 使用 `defaultdict` 計算使用者數量 (在此使用情境下比 `Counter` 更簡單)
- 使用 `Counter` 計算動作數量 (可使用內建的 `most_common()` 方法)
- 處理邊界案例：空白日誌回傳 "top_action: 0\n"

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試結果總結 - 綠燈階段
```
Ran 38 tests in 0.001s

OK
```

### 各任務測試明細

#### 任務 1 測試 (14 個測試) ✓
- test_normal_case_deduplicate ✓
- test_normal_case_ascending_sort ✓
- test_normal_case_descending_sort ✓
- test_single_element ✓
- test_empty_list ✓
- test_two_identical_elements ✓
- test_extract_evens_normal ✓
- test_extract_evens_no_evens ✓
- test_extract_evens_all_evens ✓
- test_with_negative_numbers ✓
- test_negative_evens ✓
- test_zero_in_list ✓
- test_dedup_preserves_order ✓
- test_dedup_already_unique ✓

#### 任務 2 測試 (12 個測試) ✓
- test_normal_ranking_basic ✓
- test_normal_ranking_all_different_scores ✓
- test_normal_ranking_full_list ✓
- test_tiebreak_by_age_same_score ✓
- test_tiebreak_by_name_same_score_and_age ✓
- test_tiebreak_multiple_conditions ✓
- test_k_equals_one ✓
- test_k_equals_total ✓
- test_single_student_k_one ✓
- test_identical_students_multiple ✓
- test_very_different_ages ✓
- test_one_dominant_winner ✓

#### 任務 3 測試 (12 個測試) ✓
- test_normal_log_summary ✓
- test_normal_single_action_per_user ✓
- test_normal_many_users ✓
- test_empty_logs ✓
- test_single_user_single_action ✓
- test_single_user_multiple_actions ✓
- test_user_count_sorting ✓
- test_same_user_count_alphabetical ✓
- test_top_action_most_frequent ✓
- test_all_same_action ✓
- test_different_action_names ✓
- test_complex_mixed_scenario ✓

### 綠燈階段總結
- **狀態**：✓ 綠燈 (所有測試皆通過)
- **總測試數**：38
- **成功**：38
- **失敗**：0
- **執行時間**：0.001s
- **相較於紅燈的關鍵變更**：
  - 實作了 task1_sequence_clean.py 中的 5 個函式
  - 實作了 task2_student_ranking.py 中的 1 個主函式
  - 實作了 task3_log_summary.py 中的 1 個主函式

---

## 第三階段：重構 (REFACTOR) - 程式碼優化

### 重構動作

#### 任務 1 重構
**變更：**
- 抽離出 `_is_even()` 輔助函式以提高可讀性並減少程式碼重複
- 新增詳細的 docstring 並標註時間複雜度 (去重為 O(n))
- 改進解釋排序策略的程式碼註解

**對測試的影響：** ✓ 所有 14 個測試依然通過

#### 任務 2 重構
**變更：**
- 抽離出 `_parse_input()` 將輸入解析與業務邏輯分離
- 抽離出 `_sort_by_ranking()` 以隔離排序條件
- 改善函式分解以獲得更好的可測試性
- 新增全面的 docstrings

**程式碼分離：**
- 解析階段：讀取輸入並結構化資料
- 排序階段：應用排名規則
- 格式化階段：產生輸出

**對測試的影響：** ✓ 所有 12 個測試依然通過

#### 任務 3 重構
**變更：**
- 抽離出 `_parse_logs()` 處理輸入解析
- 抽離出 `_count_user_events()` 處理使用者計數邏輯
- 抽離出 `_count_actions()` 處理動作計數邏輯
- 抽離出 `_sort_users_by_count()` 處理排序邏輯
- 每個函式現在都具有單一職責

**程式碼分離：**
- 解析：讀取日誌條目
- 計數：按使用者和動作進行聚合
- 排序：應用排序規則
- 格式化：產生輸出

**優點：**
- 更容易對個別組件進行單元測試
- 更清晰的關注點分離 (Separation of Concerns)
- 更有利於未來的維護和功能增強

**對測試的影響：** ✓ 所有 12 個測試依然通過

### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 重構後的測試結果
```
Ran 38 tests in 0.001s

OK
```

### 重構階段總結
- **狀態**：✓ 綠燈 (重構後)
- **總測試數**：38
- **成功**：38
- **失敗**：0
- **執行時間**：0.001s
- **程式碼品質提升**：
  - 新增 8 個輔助函式以提高模組化程度
  - 增強文件說明，包含參數與回傳值描述
  - 透過函式抽離減少程式碼重複
  - 提高程式碼的可讀性與可維護性

---

## 涵蓋的測試案例類別

### 邊界案例 (13 個測試)
- 空白輸入
- 單一元素
- 最小 k 值 (k=1)
- 最大 k 值 (k=n)
- 相同元素

### 正常案例 (15 個測試)
- 具有預期變化的標準輸入
- 混合正負數
- 具有不同動作數量得多名使用者
- 具有不同分數的學生

### 極端案例 (10 個測試)
- 所有值皆相同 (去重、年紀、姓名)
- 所有動作/事件類型皆相同
- 零作為偶數
- 負數
- 平手打破情境 (Tie-breaking)

---

## TDD 過程的關鍵洞察

1. **測試設計優先**：在實作前先撰寫測試，迫使釐清需求規格
2. **邊界案例發現**：測試揭露了重要的邊界案例 (空白日誌、零、負數)
3. **重構信心**：重構後測試一對一全數通過，增加了對程式碼品質的信心
4. **函式分解**：輔助函式在不犧牲效能的情況下提高了程式碼的清晰度

---

## AI 使用筆記

### 有效的 AI 輔助
- ✓ 釐清 Python lambda 函式中多鍵排序的語法
- ✓ 驗證邊界案例處理 (空白輸入、零值)
- ✓ 建議輔助函式分解的模式

### 我驗證過的 AI 建議領域
- ✓ 去重方法：驗證基於 set 的時間複雜度為 O(n)，並與其他替代方案比較
- ✓ 排序穩定性：確認 Python 的 `sorted()` 是穩定排序
- ✓ Counter 與 defaultdict 的比較：驗證符合任務需求的最佳選擇

---

## 結論

**TDD 流程完成**：成功執行 紅燈 → 綠燈 → 重構 的循環
- ✓ 成功設計出 38 個測試，每個任務涵蓋 3 種以上的案例
- ✓ 所有實作皆在第一次嘗試時通過測試
- ✓ 程式碼經過重構，結構與文件皆有所改善
- ✓ 重構過程中沒有發生回歸錯誤 (Regressions)

**準備好繳交**：程式碼已經過良好測試、適當重構且具備完整文件。