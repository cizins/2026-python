# Week 02 作業 - 序列與排名問題解決方案

## 作業總覽

本作業使用 **測試驅動開發 (Test-Oriented Development, TDD)** 方法實作了三個任務：

1. **Task 1: 序列清理 (Sequence Clean)** - 去重、排序與過濾操作
2. **Task 2: 學生排名 (Student Ranking)** - 多鍵值排序與同分判定
3. **Task 3: 日誌摘要 (Log Summary)** - 事件計數與資料聚合

---

## 完成檢查表

- [x] Task 1: 序列清理 - 已完成
- [x] Task 2: 學生排名 - 已完成
- [x] Task 3: 日誌摘要 - 已完成
- [x] 測試套件: 38 個測試 (14 + 12 + 12) - 全部通過
- [x] TEST_LOG.md: 記錄紅燈 → 綠燈 → 重構 (Red → Green → Refactor) 流程
- [x] TEST_CASES.md: 自訂測試資料與分析
- [x] AI_USAGE.md: AI 輔助使用紀錄

---

## 執行說明

### Python 版本
```
Python 3.9.6
```

### 執行程式範例

#### Task 1: 序列清理
```bash
python task1_sequence_clean.py
# 輸入: 5 3 5 2 9 2 8 3 1
# 輸出:
# dedupe: 5 3 2 9 8 1
# asc: 1 2 2 3 3 5 5 8 9
# desc: 9 8 5 5 3 3 2 2 1
# evens: 2 2 8
```

#### Task 2: 學生排名
```bash
python task2_student_ranking.py
# 輸入:
# 6 3
# amy 88 20
# bob 88 19
# zoe 92 21
# ian 88 19
# leo 75 20
# eva 92 20
#
# 輸出:
# eva 92 20
# zoe 92 21
# bob 88 19
```

#### Task 3: 日誌摘要
```bash
python task3_log_summary.py
# 輸入:
# 8
# alice login
# bob login
# alice view
# alice logout
# bob view
# bob view
# chris login
# bob logout
#
# 輸出:
# bob 4
# alice 3
# chris 1
# top_action: login 3
```

### 執行所有測試
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試執行結果
```
Ran 38 tests in 0.001s

OK
```

---

## 資料結構選擇與理由

### Task 1: 序列清理

**去重方法**: 基於 Set 並保留原本 List 順序
```python
seen = set()
result = []
for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)
```
- **理由**: 擁有 O(n) 的時間複雜度，同時能保留元素第一次出現的順序
- **捨棄的方案**: 使用 `dict.fromkeys()` 雖然可行，但在表達去重順序上不夠直覺

**排序**: 內建 `sorted()` 函數
- **理由**: Python 的 Timsort 演算法具備 O(n log n) 複雜度且穩定 (stable)，完全符合需求
- **為何不手寫排序**: 重新發明排序容易出錯，應信任標準函式庫

**偶數過濾**: 使用列表生成式 (List comprehension) 加上取餘數檢查
- **理由**: 簡潔、易讀、符合 Python 慣用語。O(n) 掃描即可保持原有順序

---

### Task 2: 學生排名

**多鍵值排序**: 使用 lambda tuple 作為 key
```python
sorted(students, key=lambda x: (-x[1], x[2], x[0]))
```
- **理由**: 單次排序搭配 Tuple 解包，能一次處理三個條件
- **分數取負值**: `-x[1]` 能夠達成降序排序，同時保持其他條件為升序
- **為何不使用多次排序**: 反向進行多次排序效率較低且難以閱讀

**捨棄的方案**: 使用 `functools.cmp_to_key` 或 `operator.itemgetter` - 在這裡使用 lambda 更加清晰

---

### Task 3: 日誌摘要

**使用者計數**: `defaultdict(int)` 
- **理由**: 遇到未見過的使用者時隱式初始化為 0；具備 O(1) 的尋找/插入時間
- **為何不用 Counter**: Counter 更適合用於動作計數，因為它有 `most_common()` 方法

**動作計數**: collections 中的 `Counter`
- **理由**: 內建的 `most_common(1)` 非常有效率；避免手動尋找最大值
- **為何不用 dict**: Counter 擁有專門的方法，且意圖更加明確

**使用者排序**: 使用 lambda 搭配負數計數
```python
sorted(..., key=lambda x: (-x[1], x[0]))
```
- **理由**: 與 Task 2 的多鍵值模式類似；計數降序，名稱升序

---

## 遇到的 Bug 與解決方法

### Bug: Task 1 - 負數的偶數判定

**問題**: 初始程式碼遇到負數時，可能會因為 Python 的地板除法行為而有問題
```python
# 初始版本: if num % 2 == 0:  # 其實這運作正常，但需要經過測試確認
```

**觀察到的錯誤**: 剛開始沒有錯誤 (取餘數行為有明確定義)，但測試揭露了覆蓋率不足的問題。

**根本原因**: 測試案例 `test_negative_evens` 突顯出必須確保負偶數 (`-4`, `-2`) 也被包含進去。

**應用的解決方案**: 
```python
def _is_even(num):
    return num % 2 == 0
```

**為何有效**: Python 對於負數的取餘數規則是：`-4 % 2 == 0` 和 `-3 % 2 == 1`，所以偶數檢測能夠正確運作。

**測試覆蓋率**: 加入了 `test_negative_evens()` 與 `test_zero_in_list()` 來驗證正確性。

---

## TDD 流程總結

### Task 1: 序列清理

**紅燈階段 (RED Phase)**:
- 撰寫 14 個測試，涵蓋正常情況 (去重、升降序、偶數)、邊界情況 (空列表、單一元素) 以及極端情況 (負數、零)。
- 所有測試一開始都因缺少函式而失敗。

**綠燈階段 (GREEN Phase)**:
- 實作了 5 個函式，撰寫最少量的程式碼。
- 14 個測試立刻全部通過。

**重構階段 (REFACTOR Phase)**:
- 抽離出 `_is_even()` 輔助函式以減少重複程式碼。
- 擴充 docstrings 加上複雜度說明。
- 所有測試依然通過；程式碼變得更易維護。

### Task 2: 學生排名

**紅燈階段 (RED Phase)**:
- 撰寫 12 個測試，專注於多鍵值排序與同分處理。
- 測試涵蓋了正常排名、年齡/名字的打破僵局規則、以及 k 值的邊界情況。
- 所有測試均失敗 (函式尚未實作)。

**綠燈階段 (GREEN Phase)**:
- 實作主函式，將輸入解析與排序在一次流程中完成。
- 使用 lambda tuple key 進行優雅的多條件排序。
- 12 個測試第一次執行就全數通過。

**重構階段 (REFACTOR Phase)**:
- 抽離出 `_parse_input()` 和 `_sort_by_ranking()` 以提升清晰度。
- 關注點分離 (Separation of concerns)：解析 → 排序 → 格式化。
- 測試全過；模組化更佳，有利於未來擴充。

### Task 3: 日誌摘要

**紅燈階段 (RED Phase)**:
- 撰寫 12 個測試，針對使用者計數、動作頻率與排序。
- 涵蓋空日誌、使用者計數平手、以及尋找最常出現的動作等極端情況。
- 測試初始皆為失敗。

**綠燈階段 (GREEN Phase)**:
- 使用 defaultdict + Counter 實作主函式。
- 確保計數降序、名稱升序的正確排序邏輯。
- 12 個測試順利通過。

**重構階段 (REFACTOR Phase)**:
- 抽離出 4 個輔助函式：parse, count_users, count_actions, sort_users。
- 每個函式都具有單一職責 (Single responsibility)。
- 測試全過；程式碼可測試性與文件化程度提升。

### 整體統計

| 階段 | 總測試數 | 通過 | 失敗 | 耗時 |
|-------|-------------|--------|--------|------|
| RED   | 38          | 0      | 38*    | N/A  |
| GREEN | 38          | 38     | 0      | 0.001s |
| REFACTOR | 38       | 38     | 0      | 0.001s |

*RED 階段的失敗是因為匯入錯誤 (函式尚未實作)，而非斷言失敗。

---

## 測試覆蓋率分析

### 依類型
- **正常情況** (15 個測試): 標準輸入與預期內的變化
- **邊界情況** (13 個測試): 空陣列/單一元素/極大極小值
- **極端情況** (10 個測試): 負數、平手、零、完全相同的數值

### 依面向
- **正確性**: 所有測試都在第一次 GREEN 嘗試中通過
- **邊界處理**: 涵蓋了空列表、零、負數與重複數值
- **排序穩定性**: 透過多個相同的紀錄進行驗證
- **輸出格式**: 字串呈現完全符合規格要求

---

## 主要學習與心得

1. **TDD 強制提升清晰度**: 先寫測試迫使我在實作前釐清需求與極端情況。
2. **重構的信心**: 重構後測試全數通過，確保了沒有發生退化 (Regression)。
3. **輔助函式的重要性**: 抽離 `_is_even()`, `_parse_input()` 等函式，在不影響效能的前提下大幅提升可讀性。
4. **多鍵值排序**: Lambda tuple 的方法在處理排名問題時既優雅又高效。
5. **發掘極端情況**: 測試過程揭露了處理空輸入、零與負數的重要性。

---

## 提交檔案清單

```
weeks/week-02/solutions/1114405042/
├── task1_sequence_clean.py       # 88 行, 5 個函式
├── task2_student_ranking.py      # 81 行, 3 個函式
├── task3_log_summary.py          # 105 行, 5 個函式
├── tests/
│   ├── test_task1.py             # 14 個測試函式
│   ├── test_task2.py             # 12 個測試函式
│   └── test_task3.py             # 12 個測試函式
├── TEST_LOG.md                   # 詳盡的 RED→GREEN→REFACTOR 記錄
├── TEST_CASES.md                 # 5 組自訂測試資料
├── AI_USAGE.md                   # AI 輔助文件
└── README.md                     # 本檔案
```

---

## 結論

本次作業成功展示了測試驅動開發 (TDD) 方法，完成了完整的 紅燈 → 綠燈 → 重構 循環。總計 38 個測試全部通過，程式碼經過良好重構並具備清晰的關注點分離，同時提供了完善的文件以供未來參考。