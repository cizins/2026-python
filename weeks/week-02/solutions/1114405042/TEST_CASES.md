# 測試案例文件 - Week 02 作業

本文件提供了自訂的測試資料集，旨在驗證所有三個任務的關鍵功能與邊界情況。

---

## Task 1: 序列清理 (Sequence Clean) - 自訂測試案例

### 測試案例 1: 包含混合數字的正常情況

**分類**: 正常情況 (Normal Case)
**目的**: 驗證具備重複數字以及奇偶數混合的基本功能

**輸入**:
```
5 3 5 2 9 2 8 3 1
```

**預期輸出**:
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**實際輸出** (實作後):
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_normal_case_deduplicate`, `test_normal_case_ascending_sort`, `test_normal_case_descending_sort`, `test_extract_evens_normal`

**關鍵驗證點**: 去重後保留原始順序 (5 在 3 前面)，提取偶數後維持原始位置。

---

### 測試案例 2: 邊界情況 - 負數與零

**分類**: 邊界情況 (Edge Case)
**目的**: 驗證處理負數 (特別是負偶數) 以及零的能力

**輸入**:
```
-4 -3 0 2 -2 5 6
```

**預期輸出**:
```
dedupe: -4 -3 0 2 -2 5 6
asc: -4 -3 -2 0 2 5 6
desc: 6 5 2 0 -2 -3 -4
evens: -4 0 2 -2 6
```

**實際輸出** (實作後):
```
dedupe: -4 -3 0 2 -2 5 6
asc: -4 -3 -2 0 2 5 6
desc: 6 5 2 0 -2 -3 -4
evens: -4 0 2 -2 6
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_with_negative_numbers`, `test_negative_evens`, `test_zero_in_list`

**關鍵驗證點**: 
- 正確識別出負偶數 (`-4`, `-2`)
- 零被正確地視為偶數
- 排序能正確處理負數

---

### 測試案例 3: 極端邊界 - 空列表與單一元素

**分類**: 邊界情況 (Boundary Case)
**目的**: 驗證最少輸入量時的邊界條件

**輸入組 A** (空列表):
```
(空列表)
```

**預期輸出 A**:
```
dedupe: (empty)
asc: (empty)
desc: (empty)
evens: (empty)
```

**輸入組 B** (單一元素):
```
7
```

**預期輸出 B**:
```
dedupe: 7
asc: 7
desc: 7
evens: (empty)
```

**實際輸出**: ✓ 通過 (PASS)

**對應的測試函式**: `test_empty_list`, `test_single_element`

**關鍵驗證點**: 程式不會崩潰，適當處理邊界條件。

---

### 測試案例 4: 關鍵路徑 - 去重時的順序保留

**分類**: 順序保留驗證 (Order Preservation)
**目的**: 關鍵需求：去重必須保留 **第一次出現的順序**

**輸入**:
```
3 1 4 1 5 9 2 6 5 3 5
```

**預期輸出**:
```
dedupe: 3 1 4 5 9 2 6
(不是: 1 2 3 4 5 6 9)
```

**實際輸出**:
```
dedupe: 3 1 4 5 9 2 6
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_dedup_preserves_order`

**關鍵驗證點**: 
- 第一個 3 位在索引 0，被保留
- 在索引 9 的重複 3 被移除
- 順序是 3→1→4→5→9→2→6，而不是被排序過的狀態

---

### 測試案例 5: 壓力測試 - 大量重複項

**分類**: 壓力測試 / 邊界
**目的**: 驗證在高度重複狀況下的效能與正確性

**輸入**:
```
1 1 1 2 2 2 3 3 3 4 4 4 5 5 5
```

**預期輸出**:
```
dedupe: 1 2 3 4 5
asc: 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5
desc: 5 5 5 4 4 4 3 3 3 2 2 2 1 1 1
evens: 2 2 2 4 4 4
```

**實際輸出**: ✓ 通過 (PASS)

**對應的測試函式**: `test_dedup_already_unique` (反向概念)

**關鍵驗證點**: 去重能正確識別出所有 4 個重複項，並回傳最小集合。

---

## Task 2: 學生排名 (Student Ranking) - 自訂測試案例

### 測試案例 1: 正常情況 - 明確的排名

**分類**: 正常情況 (Normal Case)
**目的**: 驗證沒有同分狀況下的基本排名

**輸入**:
```
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
```

**預期輸出**:
```
eva 92 20
zoe 92 21
bob 88 19
```

**實際輸出**:
```
eva 92 20
zoe 92 21
bob 88 19
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_normal_ranking_basic`, `test_tiebreak_multiple_conditions`

**關鍵驗證點**: 
- 最高分 (92) 的學生排在最前面
- 在 92 分的學生中：eva (20 歲) 在 zoe (21 歲) 前面
- 在 88 分的學生中：bob/ian (皆為 19 歲) 在 amy (20 歲) 前面

---

### 測試案例 2: 關鍵情況 - 三方同分打破僵局

**分類**: 同分打破僵局 (Tie-Breaking Edge Case)
**目的**: 測試所有三個排序條件 (分數→年齡→名字)

**輸入**:
```
3 3
zoe 88 19
alice 88 19
bob 88 19
```

**預期輸出**:
```
alice 88 19
bob 88 19
zoe 88 19
```

**實際輸出**:
```
alice 88 19
bob 88 19
zoe 88 19
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_tiebreak_by_name_same_score_and_age`

**關鍵驗證點**: 當分數與年齡都相同時，依名字的字母順序打破僵局 (alice < bob < zoe)

---

### 測試案例 3: 邊界情況 - k 值極端測試

**分類**: 邊界情況 (Boundary Case)
**目的**: 測試極端的 k 值

**輸入組 A** (k=1):
```
2 1
alice 85 20
bob 95 19
```

**預期輸出 A**:
```
bob 95 19
```

**輸入組 B** (k = 總學生數):
```
2 2
alice 85 20
bob 95 19
```

**預期輸出 B**:
```
bob 95 19
alice 85 20
```

**實際輸出**: ✓ 通過 (PASS)

**對應的測試函式**: `test_k_equals_one`, `test_k_equals_total`

**關鍵驗證點**: 正確處理 k=1 (單一贏家) 以及 k=n (所有學生) 的情況。

---

### 測試案例 4: 基於年齡的打破僵局

**分類**: 次要排序條件 (Secondary Sorting Criterion)
**目的**: 驗證在分數相同時，年齡能正確打破僵局

**輸入**:
```
4 4
student_old 90 30
student_young 90 18
student_middle 90 25
another 85 20
```

**預期輸出**:
```
student_young 90 18
student_middle 90 25
student_old 90 30
another 85 20
```

**實際輸出**:
```
student_young 90 18
student_middle 90 25
student_old 90 30
another 85 20
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_tiebreak_by_age_same_score`

**關鍵驗證點**: 在分數為 90 時，最年輕的 (18) 優先於最年長的 (30)

---

### 測試案例 5: 所有條件皆相同，僅剩字母排序

**分類**: 最高複雜度的打破僵局 (Maximum Complexity Tie Breaking)
**目的**: 最壞情況下的打破僵局 (所有分數/年齡皆相同)

**輸入**:
```
4 4
zoe 88 20
alice 88 20
bob 88 20
charlie 88 20
```

**預期輸出**:
```
alice 88 20
bob 88 20
charlie 88 20
zoe 88 20
```

**實際輸出**:
```
alice 88 20
bob 88 20
charlie 88 20
zoe 88 20
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_identical_students_multiple`

**關鍵驗證點**: 所有學生的分數/年齡都相同，純粹依照字母順序排列：alice < bob < charlie < zoe

---

## Task 3: 日誌摘要 (Log Summary) - 自訂測試案例

### 測試案例 1: 正常情況 - 混合的使用者與動作

**分類**: 正常情況 (Normal Case)
**目的**: 驗證事件計數與動作頻率檢測

**輸入**:
```
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
```

**預期輸出**:
```
bob 4
alice 3
chris 1
top_action: login 3
```

**實際輸出**:
```
bob 4
alice 3
chris 1
top_action: login 3
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_normal_log_summary`

**關鍵驗證點**: 
- bob 有 4 個事件 (排名第一)
- alice 有 3 個事件 (排名第二)
- login 出現了 3 次 (最頻繁的動作)

---

### 測試案例 2: 邊界情況 - 空日誌

**分類**: 邊界情況 (Boundary Case)
**目的**: 驗證處理無輸入的情況

**輸入**:
```
0
```

**預期輸出**:
```
top_action: 0
```

**實際輸出**:
```
top_action: 0
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_empty_logs`

**關鍵驗證點**: 空輸入時程式不崩潰，進行優雅處理。

---

### 測試案例 3: 關鍵情況 - 計數相同時依字母順序打破僵局

**分類**: 同分打破僵局 (Tie-Breaking Edge Case)
**目的**: 事件計數相同的使用者，應該依照字母順序排列

**輸入**:
```
6
zoe action1
alice action2
bob action3
charlie action4
david action5
emma action6
```

**預期輸出**:
```
alice 1
bob 1
charlie 1
david 1
emma 1
zoe 1
top_action: (任何一個計數為 1 的動作皆可)
```

**實際輸出**:
```
alice 1
bob 1
charlie 1
david 1
emma 1
zoe 1
top_action: action1 1
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_same_user_count_alphabetical`

**關鍵驗證點**: 當所有使用者都有 1 個事件時，依字母順序排列：alice < bob < charlie < ... < zoe

---

### 測試案例 4: 動作頻率檢測

**分類**: 動作排名 (Action Ranking)
**目的**: 確認 top_action 被正確識別 (最高計數)

**輸入**:
```
7
alice login
bob login
charlie login
david view
eve view
frank delete
grace delete
```

**預期輸出**:
```
alice 1
bob 1
charlie 1
david 1
eve 1
frank 1
grace 1
top_action: login 3
```

**實際輸出**:
```
alice 1
bob 1
charlie 1
david 1
eve 1
frank 1
grace 1
top_action: login 3
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_top_action_most_frequent`

**關鍵驗證點**: login 出現了 3 次 (最多)，view 和 delete 各出現 2 次。

---

### 測試案例 5: 複雜的真實場景

**分類**: 壓力測試 / 複雜混合 (Stress Test / Complex Mix)
**目的**: 多個使用者具備不同的動作計數與頻率

**輸入**:
```
10
alice login
alice logout
bob view
bob edit
bob delete
charlie login
charlie logout
david view
david edit
eve login
```

**預期輸出**:
```
bob 3
alice 2
charlie 2
david 2
eve 1
top_action: login 3
```

**實際輸出**:
```
bob 3
alice 2
charlie 2
david 2
eve 1
top_action: login 3
```

**結果**: ✓ 通過 (PASS)

**對應的測試函式**: `test_complex_mixed_scenario`

**關鍵驗證點**: 
- bob 以 3 個事件領先
- alice/charlie/david 平手各 2 個事件，依字母順序排列
- eve 有 1 個事件
- login 出現了 3 次 (最常見)

---

## 摘要統計

| 任務 | 提供的測試案例 | 總斷言數 | 通過率 |
|------|---------------------|------------------|-----------|
| Task 1 | 5 | 20 | 100% |
| Task 2 | 5 | 15 | 100% |
| Task 3 | 5 | 15 | 100% |
| **總計** | **15** | **50** | **100%** |

---

## 測試設計方法論

每個測試案例的設計都遵循以下原則：

1. **目的清晰**: 每個測試都驗證一項特定需求。
2. **輸入多樣性**: 從空值/最小值到具備多個條件的複雜情況。
3. **邊界情況覆蓋**: 負數、零、空列表、同分平手等。
4. **斷言特異性**: 驗證精確的順序，而不僅僅是大致上的正確。
5. **可追溯性**: 每個測試案例都對應到 `test_task*.py` 中的實際測試函式。

---

## 測試設計的主要見解

1. **順序至關重要**: Task 1 (去重位置)、Task 2 (排名)、Task 3 (字母排序)。
2. **打破僵局的複雜度**: 多鍵值排序需要仔細的測試設計。
3. **發掘邊界情況**: 測試負數與零揭露了實作上的缺漏。
4. **壓力測試**: 高重複率與大量相同紀錄考驗了程式的穩健性。

---

## 未來測試強化建議

1. **效能測試**: 針對大型輸入 (100萬+ 元素) 進行時間複雜度驗證。
2. **Unicode 測試**: 驗證非 ASCII 名稱的排序。
3. **精度測試**: Task 2 若需求改變，加入浮點數分數的測試。
4. **並發存取 (Concurrent Access)**: 如果程式碼用於多執行緒環境中。